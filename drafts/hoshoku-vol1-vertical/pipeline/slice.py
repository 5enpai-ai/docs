"""Cut a rendered strip into Webtoon slices (800x1280) and Canva parts (<=7600px, cut on dark gutters).
usage: python3 slice.py out/ep_full.png out"""
import sys, os
import numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
src, outdir = sys.argv[1], sys.argv[2]
s = Image.open(src).convert('RGB'); W, H = s.size
os.makedirs(f'{outdir}/webtoon', exist_ok=True); os.makedirs(f'{outdir}/canva', exist_ok=True)
n = 0
for y in range(0, H, 1280):
    n += 1; s.crop((0, y, W, min(H, y + 1280))).save(f'{outdir}/webtoon/hoshoku_v1_ch1-2_{n:03d}.jpg', quality=90)
a = np.asarray(s).astype(int); dark = (a.max(axis=2).max(axis=1) <= 14)
cuts = [0]; y = 0
while H - y > 7600:
    lim = y + 7600; c = None
    for r in range(lim, y + 3000, -1):
        if dark[r]: c = r; break
    c = c or lim; cuts.append(c); y = c
cuts.append(H)
for i in range(len(cuts) - 1):
    s.crop((0, cuts[i], W, cuts[i + 1])).save(f'{outdir}/canva/hoshoku_v1_part{i + 1:02d}.png')
print('webtoon slices', n, '| canva parts', len(cuts) - 1)
