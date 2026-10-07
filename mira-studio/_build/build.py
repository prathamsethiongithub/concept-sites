#!/usr/bin/env python3
"""
Assemble the Mira Studio concept site.

Concatenates _build/p1..p4, grades + crops the licensed source images,
writes optimised responsive assets (jpg + webp, 440/880 px), generates
the strand-QR (segno -> assets/mira-qr.svg + matrix injected into the
page for the canvas), and writes ../index.html.

Run from anywhere:  python _build/build.py
"""
import base64, json, os, re
from PIL import Image, ImageEnhance

BUILD = os.path.dirname(os.path.abspath(__file__))          # .../mira-studio/_build
ROOT  = os.path.dirname(BUILD)                              # .../mira-studio
SRC   = os.path.join(os.path.dirname(ROOT), '_direction', 'mira-studio', 'img')
ASSETS = os.path.join(ROOT, 'assets')
os.makedirs(ASSETS, exist_ok=True)

QR_URL = 'https://prathamsethiongithub.github.io/concept-sites/mira-studio/#/contact'


def crop_ratio(im, r, cx=0.5, cy=0.5, zoom=1.0):
    W, H = im.size
    if W / H > r:
        ch = H / zoom; cw = ch * r
    else:
        cw = W / zoom; ch = cw / r
    x0 = max(0, min(W - cw, cx * W - cw / 2))
    y0 = max(0, min(H - ch, cy * H - ch / 2))
    return im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch)))


def grade(im, sat=0.86, warm=0.08, bright=1.01, contrast=1.02):
    im = ImageEnhance.Color(im).enhance(sat)
    im = ImageEnhance.Contrast(im).enhance(contrast)
    w = Image.new('RGB', im.size, (246, 238, 226))
    im = Image.blend(im, w, warm)
    im = ImageEnhance.Brightness(im).enhance(bright)
    return im


JOBS = {
    'hero':  dict(src='u_lowbun.jpg',    ratio=4/5, cx=0.50, cy=0.36, zoom=1.00),
    'story': dict(src='p_hairlight.jpg', ratio=3/4, cx=0.50, cy=0.45, zoom=1.00),
    'g1':    dict(src='n1.jpg',          ratio=4/5, cx=0.44, cy=0.50, zoom=1.04),
    'g2':    dict(src='19239103.jpg',    ratio=4/5, cx=0.42, cy=0.52, zoom=1.32),
    'g3':    dict(src='p_hands.jpg',     ratio=4/5, cx=0.50, cy=0.45, zoom=1.00),
}
GRADE_OVERRIDES = {
    'g2': dict(sat=0.80, warm=0.10, bright=1.02, contrast=1.00),
    'g3': dict(sat=0.78, warm=0.11, bright=1.03, contrast=0.97),
}
SIZES = [440, 880]

# ---- images ----------------------------------------------------------------
for key, j in JOBS.items():
    path = os.path.join(SRC, j['src'])
    if not os.path.exists(path):
        raise SystemExit('missing source image: ' + path)
    im = Image.open(path).convert('RGB')
    im = crop_ratio(im, j['ratio'], j['cx'], j['cy'], j['zoom'])
    g = dict(sat=0.86, warm=0.08, bright=1.01, contrast=1.02)
    g.update(GRADE_OVERRIDES.get(key, {}))
    im = grade(im, **g)
    for w in SIZES:
        nh = int(round(w / j['ratio']))
        r = im.resize((w, nh), Image.LANCZOS)
        r.save(os.path.join(ASSETS, 'mira-%s-%d.jpg' % (key, w)), quality=80, optimize=True, progressive=True)
        r.save(os.path.join(ASSETS, 'mira-%s-%d.webp' % (key, w)), quality=78, method=6)
    print('%-5s -> assets/mira-%s-{%s}.{jpg,webp}' % (key, key, ','.join(map(str, SIZES))))

# remove the old single-size files from the inlined era
for key in JOBS:
    old = os.path.join(ASSETS, 'mira-%s.jpg' % key)
    if os.path.exists(old):
        os.remove(old)
        print('removed old inline asset:', os.path.basename(old))

# ---- QR --------------------------------------------------------------------
import segno
qr = segno.make(QR_URL, error='m')
qr.save(os.path.join(ASSETS, 'mira-qr.svg'), kind='svg', dark='#2B2118', light='#F4EEE3', border=4, scale=8)
rows = [''.join(str(int(v)) for v in row) for row in qr.matrix]
qr_json = json.dumps({'m': rows}, separators=(',', ':'))
print('QR: %s modules (version %s) -> assets/mira-qr.svg' % (qr.symbol_size(scale=1, border=0)[0], qr.version))

# ---- assemble --------------------------------------------------------------
parts = []
for p in ['p1.html', 'p2.html', 'p3.html', 'p4.html']:
    with open(os.path.join(BUILD, p), encoding='utf-8') as f:
        parts.append(f.read())
html = '\n'.join(parts)

if '__QR_MATRIX__' not in html:
    raise SystemExit('QR token missing from p4')
html = html.replace('__QR_MATRIX__', qr_json)

left = re.findall(r'__[A-Z_]+__', html)
if left:
    raise SystemExit('unreplaced tokens: %r' % left)

out_path = os.path.join(ROOT, 'index.html')
with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(html)
print('WROTE %s  (%d KB)' % (out_path, os.path.getsize(out_path) // 1024))
