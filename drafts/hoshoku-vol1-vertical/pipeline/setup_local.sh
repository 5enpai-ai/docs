#!/usr/bin/env bash
# Rebuild the HOSHOKU vertical edition on your own machine (0 credits).
# Run from this folder:  bash setup_local.sh
set -euo pipefail
cd "$(dirname "$0")"
python3 -m pip install --quiet pillow numpy
mkdir -p gen out
# Download the generated panels listed in panel_sources.json into gen/v_<id>.png
python3 - <<'PY'
import json, os, urllib.request
for k, u in json.load(open('panel_sources.json')).items():
    dst = f'gen/v_{k}.png'
    if os.path.exists(dst): continue
    print('fetch', k); urllib.request.urlretrieve(u, dst)
PY
python3 build.py spec_full.json out/ep_full.png
HOSHOKU_SOURCE_CAPTIONS=1 python3 build.py spec_full.json out/ep_full_source_captions.png
python3 slice.py out/ep_full.png out
echo "Done: out/ep_full.png, out/webtoon/*.jpg, out/canva/*.png"
