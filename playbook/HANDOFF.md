# Playbook app, implementation handoff

For the Claude Code agent working in `C:\Sites\ebustamante` (repo
`github.com/Eduardo-Sec/EduardoSec.github.io`, deployed to `site-server` at 10.10.10.60).

This document has two jobs. The first half tells you exactly what to do. The second half
tells you why every decision was made, so you do not "improve" something that was
deliberate and break it.

Read the whole thing before touching a file.

---

## 1. What this is

A self contained Django app called `playbook` that adds five unlisted pages to
ebustamante.dev. It is a flag football playbook for Eduardo's UNO intramural team, written
against the actual UNO Competitive Sports rules sheet rather than generic flag football.

```
/playbook/                 rules, personnel, formations, penalties, drills, glossary
/playbook/offense/         route depths, 22 plays with client side filters, coverage reads
/playbook/defense/         8 coverages, adjustments, technique
/playbook/special-teams/   punting, extra point maths, clock, call sheet
/playbook/card/            sideline card, built to print
```

No models. No migrations. No database access. No new dependencies. Nothing outside the
`playbook/` folder needs to change except two lines in settings and one line in the root
URLconf.

---

## 2. Hard constraints, do not violate these

These come from how the site is already built. Every one of them will silently break
something if you ignore it.

**No inline `<script>` and no inline `<style>`, ever.** The site ships a per request nonce
middleware with a strict `script-src`. The app deliberately has zero inline script and zero
inline style so nothing needs a nonce at all. If you add an inline block you have to nonce
it, and if you forget, it fails silently rather than throwing, which is the worst failure
mode there is. Do not add one.

**Every static asset goes through `{% static %}`.** The site uses
`ManifestStaticFilesStorage`, so files get content hashed URLs. A hardcoded
`/static/playbook/playbook.css` will 404 in production even though it works in DEBUG. Any
edit to the CSS or JS needs a `collectstatic` before it appears behind Cloudflare.

**Do not add a link to these pages anywhere on the site.** No nav entry, no footer, no
sitemap. They are unlisted on purpose and Eduardo asked for this explicitly.

**Do not add `Disallow: /playbook/` to robots.txt.** That file is public and a disallow line
advertises the path to every scraper that reads it, which is the exact opposite of the
intent. The `<meta name="robots" content="noindex, nofollow, noarchive, nosnippet">` in
`_base.html` is the correct tool. Leave it in place.

**Do not make `_base.html` extend `base.html`.** See section 6 for why.

**No new pip packages.** This repo has a history of Dependabot bumping past what the server
Python can support. The app uses only the standard library plus Django. Keep it that way.

**Python floor.** Nothing in the app uses syntax newer than Python 3.6, so it imports
cleanly under whatever version `django-check.yml` pins in CI. Do not introduce match
statements, walrus operators or `X | Y` type unions.

**Prose style.** Eduardo's writing rules apply to all content in this app because it lives
on his site. No em dashes, no standalone dashes, no semicolons, no colons in prose, commas
instead. Tone is casual but college level. All existing content already follows this. Match
it if you write more.

---

## 3. File map and what each file is for

```
playbook/
  __init__.py
  apps.py            standard AppConfig, name = "playbook"
  urls.py            five routes, app_name = "playbook"
  views.py           five function views, no DB, no forms, no request data used
  diagrams.py        SVG engine, field coordinates, route shape helpers
  plays.py           5 formations, 17 plays, 5 trick plays, as data
  coverages.py       8 defensive calls plus the adjustment list, as data
  content.py         rules, prose blocks, reference tables, table headers
  tags.py            filter metadata per play, beginner explainers, glossary,
                     penalty chart, drills, and which items go on the game card
  templates/playbook/
    _base.html       full HTML document, the shell every page uses
    _play.html       one play card
    _coverage.html   one coverage card
    _assign.html     the "who does what" rows
    _filterbar.html  filter chips, count, empty state, jump index
    _pairs.html      heading plus paragraph list
    _table.html      generic table
    index.html offense.html defense.html special.html card.html
  static/playbook/
    playbook.css     all styling including the generated highlight rules
    playbook.js      position filter, play filters, beginner mode, print
README.md            same information as this doc, shorter, keep it in the repo
```

---

## 4. Implementation steps

**Step 1.** Copy the `playbook/` folder into the repo alongside the other apps. Copy
`README.md` in as `playbook/README.md` so it travels with the code.

**Step 2.** Add the app to settings.

```python
INSTALLED_APPS = [
    # ...
    "playbook",
]
```

**Step 3.** Add the routes to the project URLconf.

```python
from django.urls import include, path

urlpatterns = [
    # ...
    path("playbook/", include("playbook.urls")),
]
```

**Step 4.** Nothing else. There is no base template edit, no context processor, no
middleware, no settings flag.

**Step 5.** Verify locally before committing. Run every item in section 5.

**Step 6.** Commit. Signed commits require the desktop GPG key `C40C15BD0B031356`, so do this
over RDP through Tailscale rather than on the laptop. If you are on the laptop, disable
signing locally first with `git config --local commit.gpgsign false` and expect an unverified
commit.

```bash
git add playbook
git commit -m "Add unlisted flag football playbook pages"
git push
```

**Step 7.** Deploy on site-server.

```bash
sudo bash update.sh
```

`update.sh` handles git pull, pip, `manage.py` steps and the gunicorn restart with the
privilege separation already built into it. `collectstatic` runs as part of that. Confirm the
hashed CSS and JS URLs resolve after the deploy rather than assuming.

---

## 5. Verification checklist

Do not skip the last three. They are the ones that catch real problems.

```bash
python manage.py check
python manage.py check --deploy
python manage.py collectstatic --noinput
```

- [ ] All five routes return 200. `/playbook/`, `/playbook/offense/`, `/playbook/defense/`,
      `/playbook/special-teams/`, `/playbook/card/`
- [ ] Zero console errors and zero CSP violations on all five pages. The app should produce
      no nonce warnings at all, because it has nothing inline.
- [ ] Position chips. Pick one offense letter and one defense letter, navigate to another
      playbook page, confirm both are still selected and still highlighting.
- [ ] Play filters. On the offense page, "3rd & long" alone should show 7 of 22. Adding
      "trick" on top should narrow further. "reset filters" returns to 22.
- [ ] Filter empty state. Pick "run" and "2 minute" together, confirm the message appears
      rather than a blank page.
- [ ] Beginner mode. The "explain the basics" button opens every `<details>` on the page and
      the state survives a page change.
- [ ] Tamper test. In the console, run
      `localStorage.setItem('pb-pos-off','"><img src=x onerror=alert(1)>')` and reload. The
      value must be dropped, `data-off` must be absent, and storage must be cleared.
- [ ] Mobile width at 390px. No horizontal scroll except inside `.pb-tw` tables, which are
      intentionally scrollable.
- [ ] Print preview on `/playbook/card/` looks like a usable sheet.
- [ ] **The command palette does not surface these pages.** `cmdk_search` returns static
      pages plus title matched writeups. If its static page list is derived from URL patterns
      rather than a hand written list, the playbook will appear in it and the whole unlisted
      decision is undone. Check this specifically.
- [ ] **The sitemap does not include `/playbook/`.**
- [ ] **robots.txt was not modified.**

---

## 6. Why every decision was made

### Why the pages are unlisted rather than authenticated

The content is a flag football playbook. The realistic threat is an opposing intramural team
reading our plays, which is mildly annoying and not worth an auth layer. Unlisted with
`noindex` and no inbound links is proportionate.

Be honest about what it is. It is obscurity, not access control. Anyone with the URL reads
it. If Eduardo ever wants that to change, the cheapest correct answer is a Cloudflare Access
policy on `/playbook/*` gated by email, the same mechanism already sitting in front of
`/admin/`. Do not invent a homegrown password gate.

### Why `_base.html` is a full document instead of extending `base.html`

Two reasons, and both matter.

First, the requirement. Extending `base.html` renders the site nav, the command palette
trigger and the footer links on every playbook page. Eduardo wants the only outbound link on
these pages to be the `eb.dev` brand going back to `/`. Overriding a nav block would need to
know that block's name and would break the day it gets renamed.

Second, coupling. Extending means depending on three names staying stable, the template
filename, the content block and a head block. Standing alone means the app has zero coupling
to the rest of the templates and cannot be broken by an unrelated change to the site chrome.

The cost is that the playbook will not follow a site wide retheme automatically. That is
mitigated below.

### Why the colours are tokenised the way they are

`playbook.css` defines its own `--pb-*` tokens so the page stands alone, but every one of
them falls back through Eduardo's names first.

```css
--pb-ac: var(--ac-bright, var(--ac, #10b981));
```

If `main.css` is loaded, the playbook follows the site. If it is not, the literal emerald and
gold values apply. There is a commented out `main.css` link in `_base.html` for exactly this.
Uncommenting it is the one line switch between the two behaviours. Do not hardcode the hex
values in place of the token chain.

### Why the SVG diagrams are generated in Python instead of being static files

The position highlight recolours individual route lines and individual player markers. That
requires the SVG to be inline in the document so page CSS can reach into it. An `<img>`
pointing at an `.svg` file cannot be styled from the parent page, so the whole highlight
feature would die.

Generating from data also means adding a play is one function call rather than hand authoring
a diagram. `diagrams.py` uses a field coordinate system where `x` is yards left or right of
the middle of the field and `d` is yards downfield from the line of scrimmage, so
`hitch(9, 0, depth=6)` is a hitch by a receiver nine yards right of the ball. Routes are
clamped to the sideline automatically, and a note placed at negative depth floats itself to
the top of the frame because the area below the line of scrimmage is outside the viewBox.

One detail worth knowing before you optimise anything. The diagrams are built when
`plays.py` and `coverages.py` are imported, not per request, because the `svg=diagram(...)`
call sits inside the module level data. Cost per request is therefore zero and the only
work at request time is template rendering. Do not add caching for it.

### Why the content is Python data instead of database records

Writeups are DB backed because they are published on a schedule and edited from the admin.
The playbook is not. It is a fixed reference that changes a few times a season, it is edited
by the same person who edits the code, and keeping it in Python means it is versioned,
diffable and reviewable in a pull request.

This also keeps the `|safe` usage honest, which is the next point.

### Why `|safe` is on nearly every content field, and when that becomes a bug

The templates apply `|safe` to the play descriptions, the assignments, the coverage text and
the generated SVG. That is normally a smell. It is acceptable here for one specific reason,
every one of those strings is a first party Python literal in `content.py`, `plays.py`,
`coverages.py` or `tags.py`. Some of them carry `<strong>` tags and HTML entities, and the
SVG is markup by definition.

**If anyone ever makes this content editable from the admin, or accepts it from a form, or
loads it from a file a user can write, `|safe` becomes a live stored XSS hole and must come
out first.** That is the single most important sentence in this document. Leave a comment if
you touch it.

### Why the position filter has two independent groups

A player has one offense position and one defense position. Forcing a single selection meant
he had to keep switching to see his own defensive job. Two selections live on the `.pb`
wrapper as `data-off` and `data-def`.

Dimming is deliberately scoped per group. Picking an offense letter must not grey out the
defense assignments, otherwise the defense page goes blank for someone who only picked their
offense position. The generated rules at the bottom of `playbook.css` list the offense
letters and the defense letters separately for this reason.

Inside that generated block, **all the dim rules come first and all the match rules come
second.** They share specificity, so source order is the only thing deciding the winner. If
you regenerate that block, preserve the order.

### Why the filter tokens use a pipe separator

Several filter values contain a space of their own, `cover 2` and `3rd & long`. Joining with
spaces silently broke matching for those values, and it looked like the filter simply found
nothing. The attributes are pipe delimited now, `data-beats="man|cover 2"`, and the script
splits on `|`. Never add a filter value containing a pipe.

### Why `<details>` for the beginner explainers

Eduardo asked for the explanation to be optional rather than always visible. Native
`<details>` gives collapsed by default, keyboard access and screen reader semantics for free,
and it keeps working if the JavaScript fails to load. The "explain the basics" toggle only
sets the `open` property in bulk, so the script is an enhancement rather than a requirement.
Do not reimplement this with a div and a click handler.

### Why the JS validates against an allow list

`localStorage` is attacker controllable if there is ever an XSS anywhere else on the origin,
and it is user controllable trivially through devtools. The script builds its allow list from
the buttons Django actually rendered, and any stored value that is not on that list is
dropped and deleted from storage rather than written into an attribute. There is no
`innerHTML`, no `eval`, no string built selectors and no reading of query parameters
anywhere.

This is more care than a football playbook strictly needs. It is there because this repo is
public, linked from LinkedIn, and read as a work sample.

### Why the game card is a separate page

`/playbook/card/` exists to be printed and folded into a pocket. It repeats eight plays,
three coverages and the key numbers with no explanation. Everything on it appears in more
detail elsewhere, which is intentional. Do not try to deduplicate it, the redundancy is the
feature.

### Why the scheme is what it is

Worth knowing so you do not "fix" content that is correct.

The UNO rules sheet says four downs to reach the next twenty yard zone line, not ten yards,
so the playbook is weighted toward plays that gain twelve or more on one snap. Only four
offensive players have to be on the line at the snap, so the app uses one fixed rule, C, X, Y
and Z are always on the line and QB, H and R are always off it. That keeps every formation
legal and makes H the only legal motion man. Backward passes are unlimited and a fumble is
dead where it lands with the fumbling team keeping possession, which is why the trick play
package is unusually large, those plays cannot turn the ball over. Any contact with the
quarterback is an automatic first down, which is why the rushing technique section is written
the way it is.

---

## 7. Matching the site more closely

Everything in the app was built from the live site and two of the writeups, not from the
actual source. That means the palette and the feel are right but the details are guesses.
Reconcile them against the real files. Open `main.css`, `base.html` and `main.js` and work
through the list below.

### First, make the standalone versus extend decision explicitly

Right now the app stands alone and does not load `main.css`. That was the correct default
because it guarantees no site nav renders on an unlisted page and it removes all coupling to
template block names. It also means the playbook does not inherit the site font, the custom
cursor, the hero texture or anything else.

Two ways forward. Pick one and say which.

**Option A, stay standalone and pull in the site stylesheet.** Uncomment the `main.css`
link already sitting in `_base.html`. The `--pb-*` tokens immediately resolve against the
real variables, the font family and any global resets come along, and the page still has no
site nav because the markup for it is not there. This is the recommended option. The risk is
that a `main.css` rule scoped to something like `body` or a global container could fight the
playbook layout, so check for that after you flip it.

**Option B, extend `base.html` and override the nav.** Only do this if `base.html` already
has a block wrapping the nav, or can cleanly get one. It gives perfect visual consistency for
free. It costs coupling to three block names and it means a future nav change can leak links
onto an unlisted page without anyone noticing. If you take this route, verify the command
palette trigger is also inside whatever block you suppress.

### The logo

The brand in `_base.html` is currently the plain text `eb.dev`. The site has a real mark, the
eb hexagon shield monogram SVG, already sitting in static and already used for the header and
for the Wazuh dashboard branding. Swap the text for the actual mark.

- Reference it with `{% static %}` so it gets a hashed URL.
- Keep it as the only link on the page and keep it pointing at `/`.
- Inline SVG is fine and avoids a request, an `<img>` is fine too. If you inline it, do not
  add an inline `<style>` block inside the SVG, put any styling in `playbook.css`.
- Give it an accessible name, `aria-label="eb.dev, home"` or a `<title>` inside the SVG.
- Match the size and spacing of the header mark on the rest of the site rather than picking a
  new one.

While you are there, add the site favicon and web manifest links to `_base.html`. They are
missing entirely because the app does not extend `base.html`. That is a visible bug in a
browser tab.

### Verify the token names

`playbook.css` falls back through names taken from a writeup, not from the source.

```css
--pb-ac:     var(--ac-bright, var(--ac, #10b981));
--pb-gold:   var(--gold-bright, var(--gold, #c9a227));
--pb-bg:     var(--bg, #0a0d0b);
--pb-panel:  var(--bg-card, #0d1210);
--pb-muted:  var(--text-dim, #8d9d95);
```

Open `main.css` and confirm each of those names actually exists. If a name is wrong the page
silently uses the hardcoded fallback and looks close enough that nobody notices, which is the
failure mode to watch for. The site also has `--warn` and `--info` tokens the playbook does
not use. The gold callouts in the app are the kind of thing `--warn` might be intended for,
so check whether reusing it is more correct than the current `--gold` usage.

### The colour rule, emerald is never a text colour

This is a standing instruction from Eduardo, not a preference to revisit. **Do not use the
emerald accent as a text colour anywhere in this app.** Text is white, neutral grey or gold.

Emerald is still the accent, it just only ever appears as a fill, a border, a focus ring or a
route line in a diagram.

```
white   --pb-text     body copy, headings, table keys, links at rest
grey    --pb-muted    secondary copy, hints, captions
grey    --pb-label    small labels and eyebrows, brighter than --pb-muted
gold    --pb-gold     play calls, group headings, the trailing period, explainer
                      summaries, link hover
emerald --pb-ac       fills, borders, focus rings, highlighted routes. Never text.
```

Two consequences worth knowing.

`--pb-muted` is deliberately **not** chained to the site's `--text-dim`. Every other token
falls through to Eduardo's variables first, that one does not, because `--text-dim` may carry
the site's emerald cast and the whole point of this rule is neutral greys. It is a hardcoded
`#9aa0a2` with a comment saying why. Do not "fix" the inconsistency by adding the fallback
back in.

Links are white at rest with a faint underline and go gold on hover, rather than emerald.

If you add a new component, check it against `grep -nE "color: var\(--pb-ac" playbook.css`
before you commit. That should only ever return border and background declarations.

### Typography

The app uses a system font stack. The site sets its own family in `main.css`. Once Option A
is in place that resolves itself, but confirm the heading weights and letter spacing in
`playbook.css` still look right against the real face rather than against system UI. The
playbook headings currently use `font-weight: 750` and negative tracking, which was tuned
against a system stack and may need adjusting.

### Details the site does that the playbook does not

Reuse rather than reinvent. In rough order of value.

- **The trailing period treatment.** Site headings end with a period in solid `var(--ac)`.
  The playbook copies this with `.pb-period`, verify it matches exactly rather than
  approximately.
- **The hero grid texture.** The site hero has a repeating linear gradient at low opacity
  under a radial glow, masked to fade toward the bottom, pure CSS. The playbook hero is flat.
  Lifting that treatment would do more for consistency than anything else on this list.
- **The `▸` disclosure markers and lowercase section labels.** The playbook already imitates
  these. Check whether the site has real component classes for them and use those instead of
  the duplicated styles in `playbook.css`.
- **The custom cursor.** It lives in `main.js`, which the playbook does not load. Its absence
  is the most noticeable inconsistency for anyone who lands here from the rest of the site.
  Loading `main.js` would fix it but also drags in the command palette, which we do not want
  on an unlisted page. Decide deliberately. Leaving it off is defensible.
- **The reading progress bar.** Used on writeup pages. The offense page is long enough that
  it would genuinely help, and it is the same component.
- **The print stylesheet.** The site already has one for the resume that hides nav, cursor
  and chrome. The playbook has its own minimal print block. Merge the approaches rather than
  maintaining two.
- **The 404 page.** A typo under `/playbook/` currently falls through to the site 404, which
  is correct behaviour and worth confirming rather than changing.

---

## 8. Mobile, and why it is built the way it is

The phone is the primary surface. Most of the team will never open this on a laptop, they
will open it once in a group chat and again on the sideline. Everything in the mobile block
at the bottom of `playbook.css` either buys back vertical space, makes a tap target big
enough to hit, or stops something scrolling sideways. Do not treat that block as
optional polish.

The breakpoint is 759px. There is one, deliberately, because two would double the surface
that needs testing for very little gain.

### Cards collapse, and the markup ships expanded

Each play and coverage card is now ordered header, diagram, assignments, then a toggle
holding everything else. On a phone the card is roughly one screen, which was the point.

**The HTML ships fully expanded and the script collapses it.** That ordering matters. With
no JavaScript at all, every word is on the page, which is the good failure state. If it
shipped collapsed and the script failed, half the playbook would be unreachable. The script
adds `.pb-js` to the wrapper before hiding anything, and the toggle button is invisible until
that class exists.

Desktop is untouched. On load the script collapses only if the viewport is narrow, follows
a rotation or resize, and stops following the viewport the moment the reader makes a choice
by hand, which is stored under `pb-cards`.

### Assignments lead the card, and everybody else's are hidden

The assignment rows moved above the toggle rather than inside it, so a collapsed card still
shows your job. Then, on a phone only, selecting a position sets non matching rows to
`display: none` rather than dimming them.

That is the single biggest change in this pass. A dimmed row costs the same vertical space as
a lit one, and with seven of them per card that was most of the screen. Measured on the
offense page at 390px, picking a position takes it from about 41,600px of scroll to about
26,300px, and an individual card from 1,428px to 690px.

The dim behaviour is still what desktop gets, because a desktop has the room and seeing the
other assignments in context is useful there.

### Everything else in the mobile block

- **Tables stack into labelled rows.** Every cell carries `data-label` with its column
  heading, emitted by `_table.html` from data pre zipped in `views.tbl()`. On a phone the
  header row is hidden and each cell renders its own label above it. This is why the view
  helper exists, and it is why table data now arrives as one `t` object rather than separate
  `heads` and `rows`. Before this, tables had a 540px minimum width and scrolled sideways.
- **Diagrams go edge to edge**, negative margins cancelling the card padding, which is about
  twelve percent more width for the thing people actually squint at.
- **Section tabs become one scrolling row** instead of wrapping to two, and the hero, section
  padding and headings all shrink. Together that is roughly a hundred pixels of chrome
  recovered above the first card.
- **Tap targets** are at least 32 to 38px on every chip, toggle and index entry.
- **A back to top button** appears past 900px of scroll, positioned inside
  `env(safe-area-inset-*)` so it clears a notch or a home indicator. It moves focus to the
  first position chip, not just the viewport.
- **`scroll-margin-top`** on sections and play cards so a jump or an anchor does not land
  underneath the sticky position bar.
- **A hash target opens itself.** Landing on `#p-flood` expands that card, unhides it if a
  filter had hidden it, and scrolls to it. This is the fix for the deep link bug listed as
  outstanding in the previous version of this document. Sending one play to one teammate is
  the main sharing path, so it needed to work.
- **Printing expands everything first**, otherwise a phone would print half a card.
- **`aria-live="polite"`** on the filter count so the list changing size is announced.

### What to check when you touch mobile

At 390px, on all five pages, `document.documentElement.scrollWidth` must equal 390. Anything
larger means something is forcing a sideways scroll, and the usual culprit is a table, a long
unbroken string, or a diagram that lost its `max-width`.

---

## 9. Where you could improve this

None of these are required. They are the things that were noticed and consciously deferred,
roughly ordered by value per unit of work. Ask before starting any of them.

### Real bugs worth fixing

- **Focus is not managed when the jump index is used.** Clicking an index entry moves the
  viewport but not focus.
- **No skip link.** The position bar and filter bar are a lot of controls to tab past before
  reaching content.

### Genuinely useful features

- **A "plays my position touches" filter.** Probably the single most useful filter left. It
  needs every play tagged with who can legally receive the ball on it, which is real content
  work in `tags.py`, but it turns the offense page into a personal list for each teammate.
- **Shareable pre filtered links.** Encode the position and filter state in the URL hash so
  Eduardo can send a link that opens already narrowed to, say, third and long plays with H
  highlighted. If you build this, validate the hash against the same allow lists the script
  already uses for `localStorage`, and treat it as untrusted input, because it is.
- **A diagram legend.** Solid line, dashed line, arrowhead, T bar and the gold squares all
  mean specific things and nothing on the page says so.
- **A search inside the playbook.** The site already has a debounce pattern and a command
  palette to copy from. Keep it local to the playbook rather than wiring it into `cmdk_search`,
  which would defeat the unlisted decision.

### Housekeeping

- **Page weight.** The offense page renders around 157KB of HTML because twenty two inline
  SVG diagrams live in it. That is fine over a Cloudflare tunnel but it is the largest page on
  the site by a wide margin. Splitting plays from trick plays, or rendering diagrams only for
  visible cards, are both options if it ever matters.
- **A last updated stamp** on each page, so teammates know whether they are looking at the
  current version.
- **Print tuning for the offense page.** The card page prints well. The offense page prints
  long and breaks in awkward places.
- **Tests.** There are none. A handful of smoke tests asserting all five routes return 200
  and that every play id in `tags.CARD_PLAYS` actually exists in `plays.P` would catch the
  most likely regression, which is a typo in an id.

### Content notes, leave these alone

- The tags on each card show depth and type but not the situations, because seven more chips
  per header was too noisy. Reconsider only if the header gets redesigned.
- The rules sheet contradicts itself about where the ball is spotted after a score, the 10 in
  one place and the 20 in another. The content tells the reader to ask the referee. Do not
  pick one.
