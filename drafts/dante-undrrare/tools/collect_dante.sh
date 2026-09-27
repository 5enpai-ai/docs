#!/usr/bin/env bash
# Phase 1 collector. Needs network access to the video hosts (see ../README.md).
# For each URL: download the video, list metadata, extract scene-change frames,
# and produce a timestamped transcript. You still watch each video; the output
# feeds the video record (../schema/video-record.schema.json).
#
# Usage: tools/collect_dante.sh [url-file] [out-dir]
# Needs: pip install yt-dlp imageio-ffmpeg faster-whisper
set -euo pipefail

URLS="${1:-$(dirname "$0")/seed-urls.txt}"
OUT="${2:-./dante-raw}"
FFMPEG="$(python3 -c 'import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())')"
mkdir -p "$OUT"

# 1. Expand feeds into individual video entries and save metadata for all of them.
grep -v '^#' "$URLS" | sed '/^$/d' | while read -r url; do
  yt-dlp --flat-playlist --print "%(webpage_url)s\t%(id)s\t%(title)s\t%(duration)s\t%(upload_date)s\t%(uploader)s" \
    "$url" >> "$OUT/index.tsv" || echo "UNVERIFIABLE	$url" >> "$OUT/unverifiable.tsv"
done
sort -u "$OUT/index.tsv" -o "$OUT/index.tsv"

# 2. Download each video with its info JSON (captions/descriptions included).
cut -f1 "$OUT/index.tsv" | while read -r v; do
  yt-dlp -q --no-overwrites --write-info-json -f "mp4/best" \
    -o "$OUT/%(id)s/%(id)s.%(ext)s" "$v" || echo "UNVERIFIABLE	$v" >> "$OUT/unverifiable.tsv"
done

# 3. Scene-change frames and cut timestamps, plus a timestamped transcript.
for dir in "$OUT"/*/; do
  f="$(ls "$dir"*.mp4 2>/dev/null | head -1)" || continue
  [ -n "$f" ] || continue
  "$FFMPEG" -hide_banner -loglevel error -i "$f" \
    -vf "select='gt(scene,0.3)',showinfo" -vsync vfr "$dir/cut_%03d.jpg" 2> "$dir/cuts.log" || true
  grep -o 'pts_time:[0-9.]*' "$dir/cuts.log" | cut -d: -f2 > "$dir/cut_times.txt" || true
  "$FFMPEG" -hide_banner -loglevel error -i "$f" -vf fps=2,scale=360:-1 "$dir/f2fps_%04d.jpg"
  python3 - "$f" "$dir/transcript.tsv" <<'PY'
import sys
from faster_whisper import WhisperModel
m = WhisperModel("small", compute_type="int8")
segs, _ = m.transcribe(sys.argv[1], word_timestamps=False)
with open(sys.argv[2], "w") as o:
    for s in segs:
        o.write(f"{s.start:.2f}\t{s.end:.2f}\t{s.text.strip()}\n")
PY
done
echo "Done. Index: $OUT/index.tsv   Unreachable: $OUT/unverifiable.tsv"
