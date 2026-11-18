# Generates the app icon files (run by GitHub Actions). Author: Md. Mehedi Hasan
import math, os
from PIL import Image, ImageDraw
S = 1024; c = S // 2
os.makedirs("assets", exist_ok=True)

def background():
    im = Image.new("RGBA", (S, S)); g = ImageDraw.Draw(im)
    for y in range(S):
        t = y / S
        g.line([(0, y), (S, y)], fill=(int(255 - 20 * t), int(190 - 60 * t), int(60 + 20 * t), 255))
    return im

def art(sc):
    L = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    P = lambda x, y: (c + x * sc, c + y * sc + 30 * sc)
    d.ellipse([P(-330, 250), P(330, 330)], fill=(0, 0, 0, 50))
    pg = (255, 250, 235, 255); ed = (40, 120, 230, 255)
    d.polygon([P(-340, -200), P(-10, -130), P(-10, 250), P(-340, 190)], fill=ed)
    d.polygon([P(340, -200), P(10, -130), P(10, 250), P(340, 190)], fill=ed)
    d.polygon([P(-315, -215), P(-6, -150), P(-6, 215), P(-315, 160)], fill=pg)
    d.polygon([P(315, -215), P(6, -150), P(6, 215), P(315, 160)], fill=pg)
    for i, col in enumerate([(255, 87, 87), (255, 190, 40), (60, 200, 120), (40, 150, 255)]):
        y = -90 + i * 60
        d.line([P(-270, y - 20), P(-60, y + 25)], fill=col + (255,), width=int(22 * sc))
        d.line([P(270, y - 20), P(60, y + 25)], fill=col + (255,), width=int(22 * sc))
    cx, cy = P(0, -300); R = 150 * sc; pts = []
    for k in range(10):
        r = R if k % 2 == 0 else R * 0.48; a = -math.pi / 2 + k * math.pi / 5
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=(255, 236, 70, 255), outline=(255, 255, 255, 255))
    e = int(14 * sc)
    for dx in (-52, 52):
        d.ellipse([cx + dx * sc - e, cy - 10 * sc - e, cx + dx * sc + e, cy - 10 * sc + e], fill=(70, 40, 20, 255))
    d.arc([cx - 45 * sc, cy - 5 * sc, cx + 45 * sc, cy + 55 * sc], 20, 160, fill=(70, 40, 20, 255), width=int(10 * sc))
    for r in (40, 75):
        d.arc([cx + 150 * sc - r * sc, cy - r * sc, cx + 150 * sc + r * sc, cy + r * sc], -50, 50, fill=(255, 255, 255, 255), width=int(12 * sc))
        d.arc([cx - 150 * sc - r * sc, cy - r * sc, cx - 150 * sc + r * sc, cy + r * sc], 130, 230, fill=(255, 255, 255, 255), width=int(12 * sc))
    return L

bg = background(); bg.save("assets/icon-background.png")
art(0.62).save("assets/icon-foreground.png")
full = bg.copy(); full.alpha_composite(art(0.9)); full.convert("RGB").save("assets/icon-only.png")
print("icons ready")
