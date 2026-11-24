#!/usr/bin/env python3
"""Draw the meme for make.fun bounty u-myronera-post-the-meme-win-the-feed-2de960bf.

Two-panel "ME vs MY AGENT" meme, 1200x675 PNG. Every pixel is drawn here
with PIL shapes and system-local DejaVu fonts; no downloaded images, no
external assets. See ../design/DIRECTION.md for the art direction.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 675
BG = (14, 17, 22)
LEFT_FILL = (27, 34, 48)
LEFT_BORDER = (46, 58, 77)
LEFT_TEXT = (138, 151, 168)
RIGHT_FILL = (15, 43, 26)
RIGHT_BORDER = (34, 197, 94)
RIGHT_TEXT = (232, 255, 241)
ACCENT = (163, 230, 53)
GREEN = (34, 197, 94)
STRIP = (22, 163, 74)
GOLD = (245, 197, 24)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
BOLD = f"{FONT_DIR}/DejaVuSans-Bold.ttf"
REG = f"{FONT_DIR}/DejaVuSans.ttf"
MONO_B = f"{FONT_DIR}/DejaVuSansMono-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text(draw, xy, s, fnt, fill, anchor="la"):
    draw.text(xy, s, font=fnt, fill=fill, anchor=anchor)


def center_x(draw, cx, y, s, fnt, fill):
    draw.text((cx, y), s, font=fnt, fill=fill, anchor="ma")


def glow(img, cx, cy, max_r, color, steps=48, alpha_max=70):
    """Radial glow: concentric ellipses of falling alpha (Aceternity Spotlight)."""
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for i in range(steps, 0, -1):
        r = max_r * i / steps
        a = int(alpha_max * (1 - i / steps) ** 2)
        od.ellipse([cx - r, cy - r * 0.62, cx + r, cy + r * 0.62],
                   fill=color + (a,))
    img.alpha_composite(overlay)


def rounded_panel(draw, box, fill, outline, width, radius=24):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_meme(path):
    img = Image.new("RGBA", (W, H), BG + (255,))
    draw = ImageDraw.Draw(img)

    # --- Spotlight glow behind the winning (right) panel ---
    glow(img, 890, 290, 330, (34, 197, 94), alpha_max=60)
    draw = ImageDraw.Draw(img)

    # --- Panels ---
    rounded_panel(draw, [40, 40, 580, 540], LEFT_FILL, LEFT_BORDER, 3)
    rounded_panel(draw, [620, 40, 1160, 540], RIGHT_FILL, RIGHT_BORDER, 4)

    # --- LEFT: ME ---
    text(draw, (72, 66), "ME", font(BOLD, 64), (226, 232, 240))
    text(draw, (72, 160), "I'll build", font(REG, 40), LEFT_TEXT)
    text(draw, (72, 212), "one bot", font(REG, 40), LEFT_TEXT)
    text(draw, (72, 264), "this weekend.", font(REG, 40), LEFT_TEXT)

    # Slumped figure at a laptop (bottom of left panel)
    # desk line
    draw.line([(90, 470), (530, 470)], fill=(70, 82, 100), width=6)
    # laptop: trapezoid screen + base
    draw.polygon([(330, 392), (410, 392), (425, 440), (315, 440)],
                 fill=(30, 40, 56), outline=(90, 104, 124))
    draw.rounded_rectangle([305, 440, 435, 468], radius=6, fill=(46, 58, 77),
                           outline=(90, 104, 124), width=3)
    # slumped head resting on the laptop's left edge
    draw.ellipse([258, 388, 312, 442], fill=(196, 160, 120))
    draw.arc([258, 388, 312, 442], 0, 360, fill=(120, 90, 60), width=3)
    # slumped torso + arm, draped over the desk
    draw.line([(258, 436), (150, 468)], fill=(90, 104, 124), width=14)
    draw.line([(250, 448), (196, 470)], fill=(70, 82, 100), width=9)
    # "z z z" floating up
    text(draw, (330, 330), "z", font(BOLD, 26), (120, 132, 152))
    text(draw, (362, 306), "z", font(BOLD, 32), (140, 152, 172))
    text(draw, (398, 276), "Z", font(BOLD, 40), (160, 172, 192))

    # --- RIGHT: MY AGENT ---
    text(draw, (652, 66), "MY AGENT", font(BOLD, 58), WHITE)
    # "3 AM" pill, top-right of the panel
    pill = [1020, 78, 1128, 122]
    draw.rounded_rectangle(pill, radius=20, fill=ACCENT)
    center_x(draw, 1074, 84, "3 AM", font(MONO_B, 26), (15, 43, 26))

    lines = ["built 4 bots", "entered 12 bounties",
             "#1 on the leaderboard", "paid in USDC"]
    y = 168
    for line in lines:
        text(draw, (652, y), "\u2713", font(BOLD, 34), GREEN)
        text(draw, (694, y), line, font(REG, 34), RIGHT_TEXT)
        y += 56

    # Robot with raised arms (bottom-right of right panel)
    rx, ry = 950, 382  # head top-left
    # antenna
    draw.line([(rx + 55, ry), (rx + 55, ry - 34)], fill=(163, 230, 53), width=5)
    draw.ellipse([rx + 44, ry - 48, rx + 66, ry - 26], fill=ACCENT)
    # arms raised
    draw.line([(rx - 6, ry + 70), (rx - 44, ry + 6)], fill=(232, 255, 241), width=10)
    draw.line([(rx + 116, ry + 70), (rx + 154, ry + 6)], fill=(232, 255, 241), width=10)
    # head
    draw.rounded_rectangle([rx, ry, rx + 110, ry + 96], radius=18,
                           fill=(232, 255, 241), outline=GREEN, width=4)
    draw.ellipse([rx + 22, ry + 34, rx + 44, ry + 56], fill=(14, 17, 22))
    draw.ellipse([rx + 66, ry + 34, rx + 88, ry + 56], fill=(14, 17, 22))
    draw.arc([rx + 34, ry + 60, rx + 76, ry + 84], 0, 180, fill=(14, 17, 22), width=4)
    # body
    draw.rounded_rectangle([rx + 8, ry + 100, rx + 102, ry + 140], radius=12,
                           fill=(34, 197, 94))
    # gold coins
    for (cx, cy, r) in [(700, 470, 26), (790, 500, 20), (880, 440, 16)]:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD,
                     outline=(180, 140, 10), width=3)
        center_x(draw, cx, cy - r + 4, "$", font(BOLD, r), (120, 90, 0))
    # confetti dots
    for (cx, cy, c) in [(660, 420, ACCENT), (1140, 180, GOLD), (1120, 470, ACCENT),
                        (660, 500, (96, 165, 250)), (760, 380, GOLD)]:
        draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=c)

    # --- Bottom strip: the punchline ---
    draw.rounded_rectangle([40, 560, 1160, 635], radius=20, fill=STRIP)
    center_x(draw, 600, 578, "make.fun \u2014 build bots. win bounties. get paid.",
             font(BOLD, 40), WHITE)

    img.convert("RGB").save(path, "PNG")
    print(f"saved {path}")


if __name__ == "__main__":
    draw_meme("meme.png")
