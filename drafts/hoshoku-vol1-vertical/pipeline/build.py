import json, sys
from PIL import Image, ImageDraw
from letter import *

def title_card(kind, lines):
    h = 900 if kind == 'open' else 600
    im = Image.new('RGBA', (W, h), BG + (255,)); d = ImageDraw.Draw(im)
    e = emblem(220); im.paste(e, ((W - e.width) // 2, 120), e)
    y = 120 + e.height + 50
    for i, (txt, f, col) in enumerate(lines):
        fnt = {'logo': SFX(96), 'mono': CAP_HEAD(30), 'marker': CAP_BODY(44)}[f]
        tw = d.textlength(txt, font=fnt)
        d.text(((W - tw) / 2, y), txt, font=fnt, fill=tuple(col)); y += fnt.getmetrics()[0] + fnt.getmetrics()[1] + 22
    # red/blue stitched rule
    d.rectangle((120, h - 90, W // 2, h - 84), fill=CRIMSON); d.rectangle((W // 2, h - 90, W - 120, h - 84), fill=RENARD)
    for sx in range(W // 2 - 6, W // 2 + 8, 14): pass
    d.line((W // 2, h - 100, W // 2, h - 74), fill=BONE, width=3)
    return im

def render(spec, out):
    blocks = []
    for b in spec:
        t = b['type']
        if t == 'gap': blocks.append(Image.new('RGBA', (W, b['h']), BG + (255,))); continue
        if t == 'card': blocks.append(title_card(b['kind'], [tuple(x) for x in b['lines']])); continue
        if t == 'black':
            im = Image.new('RGBA', (W, b.get('h', 900)), (4, 4, 6, 255))
        elif t == 'endcard':
            im = title_card('end', [tuple(x) for x in b['lines']])
        else:
            im = load_panel(b['img'], b.get('crop'))
        pw, ph = im.size
        for L in b.get('letters', []):
            k = L['k']; x, y = L['x'] * pw, L['y'] * ph
            tgt = (L['tx'] * pw, L['ty'] * ph) if 'tx' in L else None
            if k == 'caption': caption(im, L.get('head', ''), L.get('body', ''), x, y, L.get('maxw', 520))
            elif k == 'sfx': sfx(im, L['t'], x, y, L.get('size', 90), L.get('big', True), L.get('rot', -8))
            elif k == 'num':
                d=ImageDraw.Draw(im); f=CAP_BODY(L.get('size',64)); d.text((x,y),L['t'],font=f,fill=tuple(L.get('col',[40,40,48])))
            elif k == 'ambient': ambient(im, L['t'], x, y, L.get('size', 30), L.get('alpha', 150))
            else: bubble(im, k, L['t'], x, y, L.get('maxw', 300), tgt, L.get('size', 30))
        blocks.append(im)
    H = sum(b.height for b in blocks)
    strip = Image.new('RGB', (W, H), BG); y = 0
    for b in blocks: strip.paste(b.convert('RGB'), (0, y)); y += b.height
    strip.save(out); return strip

if __name__ == '__main__':
    spec = json.load(open(sys.argv[1])); s = render(spec, sys.argv[2]); print(s.size)
