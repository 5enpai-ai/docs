"""HOSHOKU webtoon lettering + assembly engine (800px vertical strips)."""
import json, math, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W = 800
F = 'f/'
INK = (10, 10, 10); BONE = (245, 240, 232); CRIMSON = (196, 20, 20)
RENARD = (17, 73, 196); THOUGHT = (85, 85, 119); BG = (10, 10, 10)
def font(name, size): return ImageFont.truetype(F + name, size)
DIALOG = lambda s: font('nunito-latin-800-normal.woff', s)
DIALOG_OTHER = lambda s: font('nunito-latin-700-normal.woff', s)
THINK = lambda s: font('nunito-latin-700-italic.woff', s)
SHOUT = lambda s: font('nunito-latin-900-normal.woff', s)
SFX = lambda s: font('anton-latin-400-normal.woff', s)
CAP_HEAD = lambda s: font('space-mono-latin-700-normal.woff', s)
CAP_BODY = lambda s: font('permanent-marker-latin-400-normal.woff', s)
AMBIENT = lambda s: font('nunito-latin-600-italic.woff', s)

def wrap(draw, text, fnt, maxw):
    lines = []
    for para in text.split('\n'):
        cur = ''
        for word in para.split(' '):
            t = (cur + ' ' + word).strip()
            if draw.textlength(t, font=fnt) <= maxw or not cur: cur = t
            else: lines.append(cur); cur = word
        lines.append(cur)
    return lines

def text_block(draw, lines, fnt, spacing=1.18):
    asc, desc = fnt.getmetrics(); lh = int((asc + desc) * spacing)
    w = max(draw.textlength(l, font=fnt) for l in lines); return w, lh * len(lines), lh

def draw_lines(draw, lines, fnt, cx, top, lh, fill, stroke=0, stroke_fill=None):
    for i, l in enumerate(lines):
        tw = draw.textlength(l, font=fnt)
        draw.text((cx - tw / 2, top + i * lh), l, font=fnt, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)

def tail(draw, box, target, width, fill, outline, ow, maxlen=85):
    x0, y0, x1, y1 = box; cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    tx, ty = target; dx, dy = tx - cx, ty - cy; dist = math.hypot(dx, dy) or 1
    ux, uy = dx / dist, dy / dist
    rx, ry = (x1 - x0) / 2, (y1 - y0) / 2
    # distance from centre to box edge along direction
    e = min(rx / abs(ux) if ux else 1e9, ry / abs(uy) if uy else 1e9)
    bx, by = cx + ux * (e - 12), cy + uy * (e - 12)
    L = min(maxlen, max(10, dist - e))
    tipx, tipy = cx + ux * (e + L), cy + uy * (e + L)
    px, py = -uy, ux
    pts = [(bx + px * width, by + py * width), (tipx, tipy), (bx - px * width, by - py * width)]
    draw.polygon(pts, fill=fill, outline=outline, width=ow)
    return pts

def bubble(img, kind, text, x, y, maxw=300, target=None, size=30):
    """x,y = centre of bubble in px. kind: broly | other | thought | shout"""
    d = ImageDraw.Draw(img)
    if kind == 'thought':
        fnt = THINK(size)
    elif kind == 'shout':
        fnt = SHOUT(size)
    elif kind == 'broly':
        fnt = DIALOG(size)
    else:
        fnt = DIALOG_OTHER(size)
    lines = wrap(d, text, fnt, maxw); tw, th, lh = text_block(d, lines, fnt)
    px, py = (34, 26) if kind != 'shout' else (52, 44)
    box = (x - tw / 2 - px, y - th / 2 - py, x + tw / 2 + px, y + th / 2 + py)
    if kind == 'broly':
        # style guide: plain white, thick black border, one corner clipped
        x0, y0, x1, y1 = box; c = 22
        poly = [(x0, y0), (x1 - c, y0), (x1, y0 + c), (x1, y1), (x0, y1)]
        if target: tail(d, box, target, 16, 'white', INK, 5)
        d.polygon(poly, fill='white', outline=INK, width=5)
        if target:  # re-cover tail base
            pass
        draw_lines(d, lines, fnt, x, y - th / 2, lh, INK)
    elif kind == 'other':
        if target: tail(d, box, target, 14, 'white', INK, 3)
        d.ellipse((box[0] - 10, box[1] - 6, box[2] + 10, box[3] + 6), fill='white', outline=INK, width=3)
        draw_lines(d, lines, fnt, x, y - th / 2, lh, INK)
    elif kind == 'thought':
        ov = Image.new('RGBA', img.size, (0, 0, 0, 0)); o = ImageDraw.Draw(ov)
        x0, y0, x1, y1 = box; rnd = random.Random(len(text))
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2; rx, ry = (x1 - x0) / 2, (y1 - y0) / 2
        for k in range(14):
            a = 2 * math.pi * k / 14; r = rnd.uniform(0.28, 0.38) * min(rx, ry) + 18
            ex, ey = cx + math.cos(a) * rx * 0.86, cy + math.sin(a) * ry * 0.8
            o.ellipse((ex - r, ey - r, ex + r, ey + r), fill=(255, 255, 255, 235))
        o.ellipse((x0 + 6, y0 + 4, x1 - 6, y1 - 4), fill=(255, 255, 255, 235))
        if target:
            tx, ty = target
            for k, s in enumerate((13, 9, 6)):
                f = 0.55 + 0.17 * k
                ex, ey = cx + (tx - cx) * f, cy + (ty - cy) * f
                o.ellipse((ex - s, ey - s, ex + s, ey + s), fill=(255, 255, 255, 235))
        img.alpha_composite(ov) if img.mode == 'RGBA' else img.paste(ov, (0, 0), ov)
        d = ImageDraw.Draw(img)
        draw_lines(d, lines, fnt, x, y - th / 2, lh, THOUGHT)
    elif kind == 'shout':
        x0, y0, x1, y1 = box; cx, cy = x, y; rx, ry = (x1 - x0) / 2 + 12, (y1 - y0) / 2 + 12
        rnd = random.Random(sum(map(ord, text))); pts = []
        n = 22
        for k in range(n):
            a = 2 * math.pi * k / n
            f = 1.0 if k % 2 == 0 else rnd.uniform(0.72, 0.8)
            pts.append((cx + math.cos(a) * rx * f, cy + math.sin(a) * ry * f))
        if target: tail(d, (cx - 40, cy - 40, cx + 40, cy + 40), target, 14, 'white', INK, 4)
        d.polygon(pts, fill='white', outline=INK, width=4)
        draw_lines(d, lines, fnt, x, y - th / 2, lh, INK)
    return box

def sfx(img, text, x, y, size=90, big=True, rot=-8):
    fnt = SFX(size); tmp = Image.new('RGBA', (int(size * len(text) * 0.8) + 80, int(size * 1.6)), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    if big:
        d.text((40, 10), text, font=fnt, fill=CRIMSON, stroke_width=max(4, size // 14), stroke_fill='white')
    else:
        d.text((40, 10), text, font=fnt, fill='white', stroke_width=max(3, size // 16), stroke_fill=INK)
    tmp = tmp.rotate(rot, expand=True, resample=Image.BICUBIC)
    px = min(max(int(x - tmp.width / 2), -20), img.width - tmp.width + 20)
    img.paste(tmp, (px, int(y - tmp.height / 2)), tmp)

def ambient(img, text, x, y, size=30, alpha=150):
    ov = Image.new('RGBA', img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    d.text((x, y), text, font=AMBIENT(size), fill=(200, 200, 210, alpha))
    img.paste(ov, (0, 0), ov)

EMBLEM = None
def emblem(sz):
    global EMBLEM
    if EMBLEM is None: EMBLEM = Image.open('split_v2.png').convert('RGBA')
    e = EMBLEM.crop((40, 250, 1560, 1330)); e.thumbnail((sz, sz)); return e

def caption(img, head, body, x, y, maxw=520):
    """HOSHOKU caption: bone box, red LEFT edge / blue RIGHT edge, stitched top seam, emblem tag.
    head = short mono label (the original caption info), body = Broly's voice line."""
    d = ImageDraw.Draw(img)
    hf, bf = CAP_HEAD(22), CAP_BODY(30)
    blines = wrap(d, body, bf, maxw) if body else []
    hw = d.textlength(head, font=hf) if head else 0
    bw, bh, blh = text_block(d, blines, bf, 1.12) if blines else (0, 0, 0)
    w = max(hw, bw) + 64; h = (30 if head else 0) + bh + 40
    x0, y0 = int(x), int(y); x1, y1 = x0 + int(w), y0 + int(h)
    d.rectangle((x0 + 4, y0 + 5, x1 + 4, y1 + 5), fill=(0, 0, 0))  # hard shadow
    d.rectangle((x0, y0, x1, y1), fill=BONE, outline=INK, width=3)
    d.rectangle((x0, y0, x0 + 9, y1), fill=CRIMSON); d.rectangle((x1 - 9, y0, x1, y1), fill=RENARD)
    d.rectangle((x0, y0, x1, y1), outline=INK, width=3)
    # stitched seam along the top edge
    for sx in range(x0 + 20, x1 - 16, 16):
        d.line((sx, y0 - 5, sx + 8, y0 + 5), fill=INK, width=2); d.line((sx + 8, y0 - 5, sx, y0 + 5), fill=INK, width=2)
    ty = y0 + 16
    if head:
        d.text((x0 + 28, ty), head, font=hf, fill=CRIMSON); ty += 32
    for i, l in enumerate(blines):
        d.text((x0 + 28, ty + i * blh), l, font=bf, fill=INK)
    e = emblem(44); img.paste(e, (x1 - e.width // 2 - 6, y0 - e.height // 2 - 2), e)
    return (x0, y0, x1, y1)

def load_panel(path, crop=None):
    im = Image.open(path).convert('RGB')
    if crop: im = im.crop(crop)
    h = round(im.height * W / im.width); return im.resize((W, h), Image.LANCZOS).convert('RGBA')
