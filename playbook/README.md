# Flag football playbook app

A self contained Django app that adds four pages to ebustamante.dev.

```
/playbook/                 rules, personnel, formations, penalties, drills, glossary
/playbook/offense/         route depths, 22 plays with filters, reading the defense
/playbook/defense/         8 coverages, adjustments, technique
/playbook/special-teams/   punting, extra point maths, clock, call sheet
/playbook/card/            sideline card, print first
```

No models and no migrations. The field diagrams are inline SVG generated in Python at
render time, which is what lets the position filter recolour individual route lines.

## Layout

```
playbook/
  diagrams.py    SVG engine, field coordinates and route shape helpers
  plays.py       formations, 17 plays, 5 trick plays
  coverages.py   8 defensive calls and the adjustment list
  content.py     rules, prose blocks and reference tables
  tags.py        filter metadata per play, beginner explainers, glossary,
                 penalty chart, drills, and which plays go on the game card
  views.py       four views, no database access
  urls.py
  templates/playbook/
    _base.html   the only file that touches your base template
    _play.html _coverage.html _assign.html _pairs.html _table.html
    index.html offense.html defense.html special.html
  static/playbook/
    playbook.css
    playbook.js
```

## Install

1. Copy the `playbook/` folder into the repo alongside your other apps.

2. Add it to `INSTALLED_APPS` in settings.

   ```python
   INSTALLED_APPS = [
       # ...
       "playbook",
   ]
   ```

3. Add the routes to the project `urls.py`.

   ```python
   from django.urls import include, path

   urlpatterns = [
       # ...
       path("playbook/", include("playbook.urls")),
   ]
   ```

4. Nothing else. `_base.html` is a full document and does not extend `base.html`, so there
   are no block names to match and no edit to your base template at all.

5. Do not add a nav link. These pages are unlisted on purpose. Reach them by typing or
   pasting the URL.

6. Run it locally and click through all four pages, including the position chips.

   ```bash
   python manage.py check
   python manage.py runserver
   ```

7. Collect static and deploy the usual way.

   ```bash
   python manage.py collectstatic --noinput
   git add playbook && git commit -m "Add flag football playbook pages"
   git push
   # on site-server
   sudo bash update.sh
   ```

## Security and the unlisted decision

**These pages are unlisted, which is not the same as private.** There is no authentication
on them. Anyone who has the URL can read them, and anyone who guesses `/playbook/` can too.
That is the right trade for a flag football playbook and the wrong trade for anything else.
If you ever want real access control, the cheapest option is a Cloudflare Access policy on
the `/playbook/*` path, the same mechanism already gating `/admin/`, with the team added by
email.

Four things keep the pages out of the way.

* `<meta name="robots" content="noindex, nofollow, noarchive, nosnippet">` in `_base.html`.
* No link from anywhere on the site. The only outbound link on a playbook page is the
  `eb.dev` brand back to `/`.
* Not in the sitemap. If you add these to `sitemap.xml` later you have undone the noindex.
* **Not in `robots.txt`.** A `Disallow: /playbook/` line would advertise the path to every
  scraper that reads it, which is the opposite of what you want. `noindex` is the correct
  tool here and `robots.txt` is not.

Two things worth checking on your side.

* The command palette. `cmdk_search` returns static pages plus title matched writeups. If
  its static page list is built from URL patterns rather than a hand written list, the
  playbook will show up in it. Confirm it does not.
* Referrer leakage. `_base.html` sets `<meta name="referrer" content="same-origin">`, so
  even though there are no outbound links, nothing would carry the URL off site.

**Injection surface.** There is none worth the name. No forms, no query parameters, no
database, no user supplied content anywhere. The templates use `|safe` on the content
constants because the diagrams are generated SVG and a few strings carry `<strong>` tags,
and every one of those strings is a first party Python literal in `content.py`, `plays.py`
or `coverages.py`. If you ever make this content editable from the admin, `|safe` becomes a
real XSS hole and has to come out first.

**CSP.** No inline `<script>` and no inline `<style>` anywhere, so nothing needs a nonce and
the strict `script-src` stays intact. `playbook.js` loads externally with `defer`.

**The filter script.** It only ever writes values that appear in an allow list built from
the buttons Django rendered. A tampered `localStorage` value fails validation, gets deleted
from storage and is never written into an attribute. No `innerHTML`, no `eval`, no string
built selectors.

**ManifestStaticFilesStorage.** Both static files go through `{% static %}` and get content
hashed URLs, so any edit to `playbook.css` or `playbook.js` needs a `collectstatic` before
it shows up in production.

**Colours.** `playbook.css` defines the `--pb-*` tokens itself so the page stands alone. Each
one still falls back through your names first, for example
`var(--ac-bright, var(--ac, #10b981))`, so if you uncomment the `main.css` link in
`_base.html` the playbook follows a site wide retheme.

## The position filter

Two independent selections, one offense and one defense, held on the `.pb` wrapper as
`data-off` and `data-def` and mirrored into `localStorage` under `pb-pos-off` and
`pb-pos-def` so they survive a move between the four pages.

Dimming is scoped per group. Picking an offense position never greys out the defense
assignments, and the other way round. The generated rules at the bottom of `playbook.css`
put all the dim rules first and all the match rules second, because they share specificity
and source order is what decides.

## The play filters

Every play carries five categories, defined at the top of `tags.py`.

```
depth      quick, intermediate, deep
family     pass, run, screen, trick
beats      man, cover 2, cover 3, cover 4, blitz
situ       1st down, 3rd & short, 3rd & long, red zone, goal line, 2 minute, backed up
form       Deuce, Trey, Bunch, Empty, Split
```

They render onto each card as `data-` attributes and the filter is client side. Multiple
chips in one row widen the result, chips across rows narrow it. Group headings collapse when
every play under them is filtered out, and there is an empty state when nothing matches.

**The separator is a pipe, not a space.** Several values contain a space of their own, so
`data-beats="man|cover 2"` and the script splits on `|`. If you add a value containing a
pipe the filter breaks, so do not.

Selections persist in `localStorage` under `pb-play-filters` and are validated against an
allow list built from the rendered buttons, same as the position chips.

## Beginner explainers

Every play and every coverage carries an optional `basics` string in `tags.py`, rendered as
a collapsed `<details>` block. Collapsed is the default, so the page stays clean for people
who already know the game and the explanation is one tap away for people who do not.

The "explain the basics" button in the toolbar opens or closes all of them at once, and the
choice persists across pages. The glossary on the overview page uses the same component, so
the button opens all thirty eight terms too.

Native `<details>` was deliberate. It needs no JavaScript to work, it is keyboard accessible
and screen reader friendly for free, and it survives the script failing to load.

## Editing the content later

Adding a play means adding one `play(...)` call in `plays.py`. The route helpers take field
coordinates where `x` is yards left or right of the middle and `d` is yards downfield from
the line of scrimmage, so `hitch(9, 0, depth=6)` is a hitch by a receiver nine yards right
of the ball. Anything a route draws is clamped to the sideline automatically.

Everything else, the rules list, the tables, the technique blocks, lives in `content.py` as
plain lists of tuples.
