"""SVG chalk-diagram engine for the flag football playbook."""

import math

# Field coordinate helpers -------------------------------------------------
# x: yards from middle of field (-20 .. +20)   -> px 0..400
# d: yards downfield from LOS (-8 .. +23)      -> px 300..70

W, H = 400.0, 300.0
PX_X = 10.0
PX_Y = 10.0
LOS_Y = 230.0


def sx(x):
    return 200.0 + x * PX_X


def sy(d):
    return LOS_Y - d * PX_Y


def pt(p):
    return (sx(p[0]), sy(p[1]))


def _fmt(v):
    return ("%.1f" % v).rstrip("0").rstrip(".")


def _poly(points):
    return " ".join("%s,%s" % (_fmt(a), _fmt(b)) for a, b in points)


def arrowhead(p_from, p_to, size=9.0, cls="rt-head"):
    x1, y1 = p_from
    x2, y2 = p_to
    ang = math.atan2(y2 - y1, x2 - x1)
    # pull the tip back slightly so the stroke doesn't poke through
    tipx, tipy = x2, y2
    left = (tipx - size * math.cos(ang - 0.42), tipy - size * math.sin(ang - 0.42))
    right = (tipx - size * math.cos(ang + 0.42), tipy - size * math.sin(ang + 0.42))
    return '<polygon class="%s" points="%s"/>' % (cls, _poly([(tipx, tipy), left, right]))


def endbar(p_from, p_to, length=11.0, cls="rt-bar"):
    x1, y1 = p_from
    x2, y2 = p_to
    ang = math.atan2(y2 - y1, x2 - x1) + math.pi / 2
    dx, dy = math.cos(ang) * length / 2, math.sin(ang) * length / 2
    return '<line class="%s" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (
        cls, _fmt(x2 - dx), _fmt(y2 - dy), _fmt(x2 + dx), _fmt(y2 + dy))


def _clamp(p):
    x = max(-18.8, min(18.8, p[0]))
    d = max(-7.2, min(21.5, p[1]))
    return (x, d)


def route_svg(pts_, tag, end="arrow", style="solid"):
    """pts_ in field coords. tag = position letter for filtering."""
    if len(pts_) < 2:
        return ""
    px = [pt(_clamp(p)) for p in pts_]
    cls = "rt rt-%s" % tag
    if style == "dash":
        cls += " rt-dash"
    out = ['<polyline class="%s" points="%s"/>' % (cls, _poly(px))]
    if end == "arrow":
        out.append('<g class="rt rt-%s">%s</g>' % (tag, arrowhead(px[-2], px[-1])))
    elif end == "bar":
        out.append('<g class="rt rt-%s">%s</g>' % (tag, endbar(px[-2], px[-1])))
    return "".join(out)


def player_svg(tag, x, d, side="off", label=None):
    cx, cy = sx(x), sy(d)
    label = label if label is not None else tag
    shape_cls = "pl pl-%s %s" % (tag, "pl-off" if side == "off" else "pl-def")
    fs = 11 if len(label) < 3 else 9
    body = '<circle class="%s" cx="%s" cy="%s" r="11"/>' % (shape_cls, _fmt(cx), _fmt(cy))
    if side == "def":
        body = ('<rect class="%s" x="%s" y="%s" width="22" height="22" rx="4"/>'
                % (shape_cls, _fmt(cx - 11), _fmt(cy - 11)))
    txt = ('<text class="pl-txt pl-%s" x="%s" y="%s" font-size="%d">%s</text>'
           % (tag, _fmt(cx), _fmt(cy + 4), fs, label))
    return body + txt


def zone_svg(tag, x, d, rx, ry, label):
    cx, cy = sx(x), sy(d)
    return ('<ellipse class="zn zn-%s" cx="%s" cy="%s" rx="%s" ry="%s"/>'
            '<text class="zn-txt zn-%s" x="%s" y="%s">%s</text>'
            % (tag, _fmt(cx), _fmt(cy), _fmt(rx), _fmt(ry),
               tag, _fmt(cx), _fmt(cy + 3.5), label))


def note_svg(x, d, text, anchor="middle"):
    if d < -6.5:          # bottom of frame is off-canvas; float it to the top instead
        d = 21.3
    return ('<text class="fld-note" x="%s" y="%s" text-anchor="%s">%s</text>'
            % (_fmt(sx(x)), _fmt(sy(d)), anchor, text))


FIELD_BG = []
for _yd in range(-5, 25, 5):
    if _yd == 0:
        continue
    FIELD_BG.append('<line class="yl" x1="0" y1="%s" x2="400" y2="%s"/>'
                    % (_fmt(sy(_yd)), _fmt(sy(_yd))))
FIELD_BG.append('<line class="sl" x1="8" y1="0" x2="8" y2="300"/>')
FIELD_BG.append('<line class="sl" x1="392" y1="0" x2="392" y2="300"/>')
FIELD_BG.append('<line class="los" x1="0" y1="%s" x2="400" y2="%s"/>'
                % (_fmt(LOS_Y), _fmt(LOS_Y)))
FIELD_BG = "".join(FIELD_BG)


def diagram(players, routes=(), zones=(), notes=(), side="off", title=""):
    """players: list of (tag, x, d) or (tag, x, d, label)
       routes:  list of (tag, pts, end, style)"""
    parts = ['<svg class="fld" viewBox="0 0 400 300" role="img" aria-label="%s">' % title,
             '<rect class="turf" x="0" y="0" width="400" height="300" rx="10"/>',
             FIELD_BG]
    for z in zones:
        parts.append(zone_svg(*z))
    for r in routes:
        tag, ptsl = r[0], r[1]
        end = r[2] if len(r) > 2 else "arrow"
        style = r[3] if len(r) > 3 else "solid"
        parts.append(route_svg(ptsl, tag, end, style))
    for p in players:
        tag, x, d = p[0], p[1], p[2]
        lbl = p[3] if len(p) > 3 else None
        sd = p[4] if len(p) > 4 else side
        parts.append(player_svg(tag, x, d, sd, lbl))
    for n in notes:
        parts.append(note_svg(*n))
    parts.append("</svg>")
    return "".join(parts)


# Route shape helpers ------------------------------------------------------

def go(x, d, top=19):
    return [(x, d), (x, top)]


def stemgo(x, d, top=19, lean=0.0):
    return [(x, d), (x, d + 4), (x + lean, top)]


def hitch(x, d, depth=6, back=1.4):
    return [(x, d), (x, depth), (x, depth - back)]


def slant(x, d, dirn, depth=3, run=8):
    return [(x, d), (x, d + depth), (x + dirn * run, d + depth + run * 0.75)]


def out(x, d, depth=8, run=9, dirn=1):
    return [(x, d), (x, depth), (x + dirn * run, depth + 0.6)]


def indig(x, d, depth=11, run=11, dirn=1):
    return [(x, d), (x, depth), (x + dirn * run, depth + 0.4)]


def corner(x, d, depth=10, run=8, rise=8, dirn=1):
    return [(x, d), (x, depth), (x + dirn * run, depth + rise)]


def post(x, d, depth=10, run=8, rise=9, dirn=1):
    return [(x, d), (x, depth), (x + dirn * run, depth + rise)]


def flat(x, d, dirn=1, run=9, rise=1.5):
    return [(x, d), (x + dirn * run, d + rise)]


def swing(x, d, dirn=1):
    return [(x, d), (x + dirn * 4, d - 1), (x + dirn * 10, d + 1.5)]


def drag(x, d, dirn=1, depth=4.5, run=18):
    return [(x, d), (x, depth), (x + dirn * run, depth + 1.2)]


def wheel(x, d, dirn=1, top=18):
    return [(x, d), (x + dirn * 5, d + 0.5), (x + dirn * 7, d + 3), (x + dirn * 8, top)]


def comeback(x, d, depth=13, dirn=1):
    return [(x, d), (x, depth), (x + dirn * 2.5, depth - 3)]


def double(x, d, brk1, dx1, brk2, dx2, top=18):
    return [(x, d), (x, brk1), (x + dx1, brk1 + 1.5), (x + dx1 + dx2, top)]
