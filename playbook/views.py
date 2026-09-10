"""Static playbook pages. No models, no database, just rendered content."""

from django.shortcuts import render

from . import content, coverages, plays, tags

NAV = [
    ("index", "overview", "playbook:index"),
    ("offense", "offense", "playbook:offense"),
    ("defense", "defense", "playbook:defense"),
    ("special", "special teams", "playbook:special"),
    ("card", "game card", "playbook:card"),
]

# Which filter token each defensive call belongs to, used for the
# "what beats this" cross links on the coverage cards.
COVERAGE_TOKEN = {"two": "cover 2", "pipe": "cover 2", "three": "cover 3",
                  "four": "cover 4", "one": "man", "zero": "man",
                  "dog": "blitz", "trap": "cover 2"}


def _beaten_by(cov_id):
    token = COVERAGE_TOKEN.get(cov_id)
    if not token:
        return []
    return [(p["name"], p["id"]) for p in plays.P + plays.TRICK
            if token in p.get("beats", [])]


def tbl(heads, rows):
    """Pair every cell with its column label.

    The templates emit that label as data-label so the mobile stylesheet can
    stack a table into labelled rows instead of forcing a sideways scroll.
    """
    return {"heads": heads, "rows": [list(zip(heads, r)) for r in rows]}


def _base(page, title, lede):
    """Context every playbook page needs."""
    keys = [n[0] for n in NAV]
    i = keys.index(page)
    return {
        "pb_page": page,
        "pb_title": title,
        "pb_lede": lede,
        "pb_nav": NAV,
        "off_pos": content.OFF_POS,
        "def_pos": content.DEF_POS,
        "pb_prev": NAV[i - 1] if i > 0 else None,
        "pb_next": NAV[i + 1] if i < len(NAV) - 1 else None,
    }


def index(request):
    ctx = _base(
        "index", "the playbook",
        "Every play, every coverage, and exactly what your position does on each one, "
        "written against our actual league rules rather than generic flag football.",
    )
    ctx.update(
        rules=content.RULES,
        glossary=tags.GLOSSARY,
        penalty_5=tags.PENALTY_5,
        penalty_10=tags.PENALTY_10,
        drills=tags.DRILLS,
        pregame=content.PREGAME,
        off_pos=content.OFF_POS,
        def_pos=content.DEF_POS,
        formations=plays.FORMATIONS,
        t_offpos=tbl(content.H_OFF_POS, content.OFF_POS),
        t_defpos=tbl(content.H_DEF_POS, content.DEF_POS),
        t_pen5=tbl(content.H_PENALTY, tags.PENALTY_5),
        t_pen10=tbl(content.H_PENALTY, tags.PENALTY_10),
        install=content.INSTALL,
        core_off=content.CORE_EIGHT_OFF,
        core_def=content.CORE_EIGHT_DEF,
    )
    return render(request, "playbook/index.html", ctx)


def offense(request):
    ctx = _base(
        "offense", "offense",
        "Route depths, the plays, and how to read what the defense is showing you before "
        "the ball is snapped.",
    )
    groups = []
    for p in plays.P:
        if p["group"] not in groups:
            groups.append(p["group"])
    ctx.update(
        filter_groups=tags.FILTER_GROUPS,
        play_count=len(plays.P) + len(plays.TRICK),
        route_rows=content.ROUTE_ROWS,
        t_routes=tbl(content.H_ROUTES, content.ROUTE_ROWS),
        t_convert=tbl(content.H_CONVERT, content.CONVERT_ROWS),
        t_qbread=tbl(content.H_QB_READ, content.QB_READ_ROWS),
        route_rules=content.ROUTE_RULES,
        convert_rows=content.CONVERT_ROWS,
        groups=[(g, [p for p in plays.P if p["group"] == g]) for g in groups],
        tricks=plays.TRICK,
        qb_ladder=content.QB_LADDER,
        qb_read_rows=content.QB_READ_ROWS,
        qb_post_snap=content.QB_POST_SNAP,
    )
    return render(request, "playbook/offense.html", ctx)


def defense(request):
    ctx = _base(
        "defense", "defense",
        "Eight calls out of one set of personnel, how deep to line up on each of them, and "
        "how to read a receiver instead of guessing.",
    )
    ctx.update(
        coverages=[(c, _beaten_by(c["id"])) for c in coverages.D],
        adjustments=coverages.ADJUSTMENTS,
        depth_rows=content.DEF_DEPTH_ROWS,
        t_depth=tbl(content.H_DEF_DEPTH, content.DEF_DEPTH_ROWS),
        man_tech=content.MAN_TECH,
        read_ladder=content.READ_LADDER,
        zone_tech=content.ZONE_TECH,
        rush_tech=content.RUSH_TECH,
        flag_tech=content.FLAG_TECH,
    )
    return render(request, "playbook/defense.html", ctx)


def special(request):
    ctx = _base(
        "special", "special teams and situations",
        "Punting, the extra point maths, the clock, and what we call from every spot on "
        "the field.",
    )
    ctx.update(
        punt_rules=content.PUNT_RULES,
        t_punt=tbl(content.H_PUNT, content.PUNT_POLICY),
        t_pat=tbl(content.H_PAT, content.PAT_ROWS),
        t_situ=tbl(content.H_SITU, content.SITU_ROWS),
        punt_policy=content.PUNT_POLICY,
        pat_rows=content.PAT_ROWS,
        pat_notes=content.PAT_NOTES,
        clock_notes=content.CLOCK_NOTES,
        situ_rows=content.SITU_ROWS,
    )
    return render(request, "playbook/special.html", ctx)


def card(request):
    """Sideline card. Deliberately short, print first, no explainers."""
    by_id = {p["id"]: p for p in plays.P + plays.TRICK}
    cov_by_id = {c["id"]: c for c in coverages.D}
    ctx = _base(
        "card", "game card",
        "The eight calls and three coverages we run most, plus the numbers worth knowing "
        "on the sideline. Print this one.",
    )
    ctx.update(
        card_plays=[by_id[i] for i in tags.CARD_PLAYS if i in by_id],
        card_coverages=[cov_by_id[i] for i in tags.CARD_COVERAGES if i in cov_by_id],
        pat_rows=content.PAT_ROWS,
        situ_rows=content.SITU_ROWS,
        punt_policy=content.PUNT_POLICY,
        t_pat=tbl(content.H_PAT, content.PAT_ROWS),
        t_situ=tbl(content.H_SITU, content.SITU_ROWS),
        t_punt=tbl(content.H_PUNT, content.PUNT_POLICY),
    )
    return render(request, "playbook/card.html", ctx)
