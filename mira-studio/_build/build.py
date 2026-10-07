#!/usr/bin/env python3
"""
Assemble the Mira Studio concept site.

Concatenates _build/p1..p4, grades + crops the licensed source images,
inlines them as base64 data URIs, and writes ../index.html (self-contained).
"""
import base64, os, re
from PIL import Image, ImageEnhance

BUILD = os.path.dirname(os.path.abspath(__file__))          # .../mira-studio/_build
ROOT  = os.path.dirname(BUILD)                              # .../mira-studio
SRC   = os.path.join(os.path.dirname(ROOT), '_direction', 'mira-studio', 'img')
ASSETS = os.path.join(ROOT, 'assets')
os.makedirs(ASSETS, exist_ok=True)


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
    'hero':  dict(src='u_lowbun.jpg',    ratio=4/5, cx=0.50, cy=0.36, zoom=1.00, w=1100, q=80),
    'story': dict(src='p_hairlight.jpg', ratio=3/4, cx=0.50, cy=0.45, zoom=1.00, w=960,  q=80),
    'g1':    dict(src='n1.jpg',          ratio=4/5, cx=0.44, cy=0.50, zoom=1.04, w=880,  q=80),
    'g2':    dict(src='19239103.jpg',    ratio=4/5, cx=0.42, cy=0.52, zoom=1.32, w=880,  q=80),
    'g3':    dict(src='p_hands.jpg',     ratio=4/5, cx=0.50, cy=0.45, zoom=1.00, w=880,  q=80),
}
GRADE_OVERRIDES = {
    'g2': dict(sat=0.80, warm=0.10, bright=1.02, contrast=1.00),
    'g3': dict(sat=0.78, warm=0.11, bright=1.03, contrast=0.97),
}

data_uris = {}
for key, j in JOBS.items():
    path = os.path.join(SRC, j['src'])
    if not os.path.exists(path):
        raise SystemExit('missing source image: ' + path)
    im = Image.open(path).convert('RGB')
    im = crop_ratio(im, j['ratio'], j['cx'], j['cy'], j['zoom'])
    w = j['w']; nh = int(w / j['ratio'])
    im = im.resize((w, nh))
    g = dict(sat=0.86, warm=0.08, bright=1.01, contrast=1.02)
    g.update(GRADE_OVERRIDES.get(key, {}))
    im = grade(im, **g)
    out = os.path.join(ASSETS, 'mira-%s.jpg' % key)
    im.save(out, quality=j['q'], optimize=True)
    b = open(out, 'rb').read()
    data_uris[key] = 'data:image/jpeg;base64,' + base64.b64encode(b).decode('ascii')
    print('%-5s -> %s  %d KB  (%dx%d)' % (key, out, len(b) // 1024, w, nh))

parts = []
for p in ['p1.html', 'p2.html', 'p3.html', 'p4.html']:
    with open(os.path.join(BUILD, p), encoding='utf-8') as f:
        parts.append(f.read())
html = '\n'.join(parts)

for key, uri in data_uris.items():
    tok = '__IMG_' + key.upper() + '__'
    n = html.count(tok)
    print('token %s: %d occurrence(s)' % (tok, n))
    html = html.replace(tok, uri)

left = re.findall(r'__IMG_[A-Z0-9]+__', html)
if left:
    raise SystemExit('unreplaced tokens: %r' % left)

out_path = os.path.join(ROOT, 'index.html')
with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(html)
print('WROTE %s  (%d KB)' % (out_path, os.path.getsize(out_path) // 1024))
