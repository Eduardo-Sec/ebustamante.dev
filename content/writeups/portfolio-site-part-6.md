---
title: "Closing out CSP, upgrading to Django 5.2, and rebuilding the resume pipeline"
date: 2026-08-05
tags: ["project"]
draft: false
---

## Overview

The previous writeup ended with three things flagged as deferred: CSP, Permissions-Policy, and cache-busting. All three got done here, along with a Django LTS upgrade, a CI hardening pass, a full rebuild of how the resume gets published, and a fix to the deploy script itself. Two things along the way turned into real lessons worth writing down: a CSP change that silently broke the back button, and a git history rewrite that got quietly undone by an auto-merge process I didn't know this repo had. Software versions and specific values reflect the state at time of writing.

-----

## Closing out the deferred hardening items

CSP shipped as a per-request nonce middleware with a strict `script-src`, and every inline `<script>` tag across the templates picked up the nonce attribute. Verified with a real headless-browser pass across five pages plus the command palette interaction, zero violations. `style-src` still needed `unsafe-inline`, since the custom cursor in `main.js` sets `element.style.*` directly on every `mousemove`. That's first-party positioning math with no user-input path anywhere near it, not a realistic injection vector, so the tradeoff got scoped to styles only while `script-src` stayed fully strict rather than loosening both. Permissions-Policy went in alongside it, denying camera/mic/geolocation and the rest of the unused feature set. HSTS came up from the one-hour trial value to one day, still intentionally holding off on `includeSubDomains` and `preload`.

The caching piece turned out to be worth doing at the same time. Switched static file serving to `ManifestStaticFilesStorage`, so every static file gets a content hash in its URL (`main.a3f8c9.css`). A changed file is now a new URL nobody has cached, which fixed both the Cloudflare edge staleness problem and Safari's stubbornly persistent favicon cache, permanently, no more manual purges after a deploy. The one wrinkle was `site.webmanifest`, which can't use `{% static %}` as a flat file since it needed to resolve hashed icon URLs itself, so that became a small Django view instead.

Also went back and toned down the primary button, the solid-fill version was reading noticeably more saturated than the same emerald used as thin accents elsewhere, so it dropped to the dimmer variant at rest with the brighter one only on hover.

-----

## The CSP fallout: a silently broken back button

Shipping strict `script-src` broke the back button on every page, silently. It was wired up as `javascript:history.back()` in an href, and CSP blocks `javascript:` URLs outright with no nonce mechanism that applies to href attributes. Moved it to a proper click listener in `main.js` instead, which is better practice independent of CSP anyway. Worth flagging as a category of bug: CSP failures on things like this don't throw an error a user reports, they just quietly do nothing, so the actual fix was "go click every interactive element on every page after touching CSP," not just check the console for violations.

-----

## Hardening the pipeline, not just the site

A few things here were about catching problems before they reach production instead of hardening production itself.

`/.well-known/security.txt` was only reachable at `/static/.well-known/security.txt`, not its RFC-correct root path, fixed with a small Django view that reads from the existing static file, so the `security-txt.yml` auto-renewal Action keeps working against one source of truth. `/robots.txt` and `/humans.txt` got the same treatment.

Added `django-check.yml`, a workflow that runs `manage.py check`, a migration check, `check --deploy`, and `collectstatic` against Python 3.9 on every PR, matching the server's actual Python version. That specific detail matters: running CI against the production Python version is exactly what would have caught the two Dependabot incidents described in the last writeup before they ever merged, not after.

Also added `pip-audit.yml` for dependency CVE scanning, and it immediately found something real: gunicorn 21.2.0, then currently deployed, had two live CVEs (2024-1135 and 2024-6827, both HTTP request smuggling), fixed in 22.0.0+. Bumped to gunicorn 23.*, the highest version still compatible with the server's Python 3.9 at the time, same version ceiling that caused the Dependabot incidents in the first place. pip-audit now reports clean.

Separately, cleaned up dead weight from the Hugo era: deleted `hugo.yml`, `links.yml`, and `CNAME`, updated branch protection's required status checks first so nothing pointed at a workflow that no longer existed, and rebuilt cspell's word list against every writeup, it had drifted badly out of date, 161 flagged words down to zero after a real run.

-----

## Role update, and everything it touched

Updated the current role to Cybersecurity Engineer Intern at Sera Digital Corp, with the prior SOC Analyst Intern role kept as a past entry with an end date rather than removed, historical writeup content stays untouched either way, since those are dated records of what was true at the time. The update itself touched the homepage hero, the about page, the resume, JSON-LD, and CLAUDE.md.

Two things fell through the cracks on the first pass and needed follow-up fixes. The OG image still said SOC Analyst Intern, it's a static asset with the job title baked into the pixels, so the template-only update missed it entirely; regenerated it to match the site's own hero tag. And while touching the nav, noticed the command palette trigger was fully `display: none` on mobile, meaning there was no way to reach it at all on a touch device since Ctrl+K doesn't apply there. Split the trigger into separate icon/label/kbd-hint spans so mobile shows just the icon as a compact tap target instead of hiding the whole control.

A third, unrelated bug turned up in the same stretch: the mobile nav and command palette would stay open after using the browser's back button. Turns out bfcache restores a page exactly as it looked at the moment you navigated away, so if either was open when a link got tapped, back navigation restored that same open state. Fixed with a `pageshow` listener checking `event.persisted`, kept as a standalone listener outside `DOMContentLoaded` since that event doesn't refire on a bfcache restore.

-----

## The Python/Django version treadmill

Django 4.2 hit end of extended support, so the site moved to Django 5.2 LTS on Python 3.11. Before touching anything, went through every 5.0/5.1/5.2 breaking change against actual usage in the codebase, none applied, no Forms, no file uploads, no custom admin templates, no legacy storage settings. Verified empirically with a full local pass under Django 5.2.15 on Python 3.13: every route, HTMX search, the command palette, and CSP compliance all passed identically to 4.2. gunicorn went to 26.* now that the Python floor was high enough to support it. A new `deploy/upgrade-python-django.sh` handles the one-time server-side migration, since the existing `update.sh` can't, its pip install step runs under the old venv's Python 3.9, which can't satisfy a Django 5.2 requirement. It installs 3.11 alongside the untouched system Python, rebuilds the venv, backs up the old one, migrates, and smoke-tests.

With the Django app fully carrying the live site, the Hugo leftovers finally got removed, `themes/`, `public/`, `hugo.toml`, `archetypes/`, and the stray `content/*.md` pages superseded by DB-backed writeups. `CLAUDE.md` and `.claude/` moved to gitignored-but-kept-locally rather than deleted, since this repo is linked from LinkedIn and there's no reason for that file to be public.

Went back through `.github/workflows` and found `actions/setup-python` was still floating on a version tag while every other action was already SHA-pinned, closed that gap, verifying every SHA directly against GitHub's API rather than trusting a summary. Also bumped a third-party action, `projectwarden/warden`, from v1.0.0 to v2.0.0.

The Dependabot ignore rule from the previous hardening pass didn't actually hold. The wildcard `dependency-name: '*'` plus semver-major ignore rule still let Django 6.0 and gunicorn 26 PRs get proposed, because they'd already been opened before the rule landed, the rule only blocks new PRs, it doesn't retroactively close ones already sitting open. Switched to explicit per-package ignore entries for Django and gunicorn specifically, which is the documented reliable pattern, and both are capped to what Python 3.9 could support at the time. Given that history, the eventual jump to Python 3.12 / Django 6.0 got staged deliberately rather than left to Dependabot: a migration script mirroring the 3.11 upgrade's pattern, install 3.12 alongside the existing interpreters, rebuild the venv, run migrate/collectstatic/import_writeups, sitting ready to go before the version bump itself gets merged.

-----

## Resume overhaul

The resume PDF now lives at a stable, extensionless URL, `/resume/`, served directly by nginx from `files/resume.pdf`, outside `STATICFILES_DIRS`, so it never goes through `ManifestStaticFilesStorage` hashing. That matters because the resume gets updated content several times a year but the URL needs to stay constant for anything that's already linked to it; no `collectstatic`, no gunicorn restart, just drop a new file in place. The old HTML version moved to `/resume/preview/`, and legacy URLs, the old Hugo `/resume.pdf`, stale hashed `/static/resume.*.pdf` copies, now 301 to `/resume/` instead of continuing to serve stale content or 404ing.

Getting nginx to serve the PDF correctly took a second pass. Aliasing a trailing-slash location straight to a file made nginx's index module blindly concatenate `index.html` onto the alias target, since it assumes trailing-slash locations resolve to directories, produced `resume.pdfindex.html` and a 500. Fixed by aliasing to the directory and naming the file explicitly via `try_files`, which sidesteps the index module entirely.

The old `static/resume.pdf` predated the current publishing setup and had a phone number baked into it, removed in favor of a build without it. Email and city stayed everywhere they already appeared (contact page, `humans.txt`, resume, about page, footer, homepage SOC widget) rather than getting redacted on the resume specifically. First instinct was to pull them off the resume too for a stricter default, but that just made the resume inconsistent with every other page that already lists them, and the phone number is the one piece of contact info that's actually spam-sensitive enough to be worth keeping off the site entirely.

That distinction is enforced by a small script, `deploy/check-resume-pii.sh`, which runs `pdftotext` against a candidate PDF and greps for the phone number before it can get published as `files/resume.pdf`, a safety gate against accidentally publishing the wrong build, scoped to the one thing that actually needs to stay private. A second script, `deploy/purge-cloudflare-cache.sh`, purges `/resume/` and its legacy static paths from Cloudflare's edge after a publish, falling back to printing manual dashboard steps if `CF_API_TOKEN`/`CF_ZONE_ID` aren't set rather than failing outright.

-----

## A history rewrite that didn't survive the merge

Reversing the email/city redaction above looked like a good candidate for cleaning up history rather than just adding a second commit on top, since the honest end state is "this removal never should have happened," not "removed, then un-removed." So the commit that stripped them got dropped entirely: rebuilt the branch by cherry-picking the two commits that came after it onto its own parent, then force-pushed with `--force-with-lease`.

It didn't actually take. This repo turns out to auto-merge PRs, and as part of that it also merges `master` back into the feature branch before merging it in, visible in the history as a `Merge branch 'master' into ...` commit. That merge is exactly where the rewrite got undone. Git's three-way merge compared the rewritten branch against `master` using their common ancestor, and since the rewritten branch simply didn't contain a commit touching those lines, git read that as "unchanged on our side, changed on master's side" and kept master's version, the one with the redaction still in it. The rewrite was completely correct on the feature branch in isolation, it just couldn't survive being merged with a lineage that already contained the commit it was trying to erase.

The actual fix was a plain forward commit instead, one that changes the six affected lines back rather than removing the commit that changed them in the first place. That's immune to the same trap no matter what merges into it later, since it's a real diff for git to see, not an absence of one. Worth remembering for any future work on this repo specifically: don't rewrite history to erase a commit when there's automation that might merge branches together, revert forward instead.

-----

## update.sh privilege separation

The deploy script had a real bug: running the whole thing as root (`sudo bash update.sh`) left root-owned files in `.git` and `.venv`, which then broke subsequent non-root git and pip operations. Running it unprivileged couldn't restart the systemd service at all, so neither mode actually worked end to end. Fixed by splitting responsibility per step, the git/pip/`manage.py` steps drop to the `ebustamante` user via `sudo -u`, the restart stays root, while the invocation itself stays a single `sudo bash update.sh`, same as before. Each step now runs with only the privilege it actually needs.

Also found, while chasing an unrelated login prompt on the server, that the live checkout's git remote was still pointed at the pre-migration repo name from the GitHub Pages era. GitHub's rename redirect was carrying it fine, but `deploy/setup.sh` and a "source" link on the projects page both got updated to the current URL rather than continuing to rely on a redirect.

-----

## What's still open

`includeSubDomains` and `preload` on HSTS are still both off, deliberately, that's still a one-way door once submitted to browser preload lists, waiting on more clean production time first. The `feed.xsl` styling for RSS is still unverified against a real Firefox or Safari session, only confirmed dead in Chrome.

The repo itself is staying public rather than going private. The main argument for private was reducing the phone-number-style exposure surface, but there's no actual secret material in it, and for a site that exists specifically as a portfolio, having the CSP middleware, the pip-audit catch, the SHA-pinned Actions, and this session's own privilege-separation fix visible as real commits is worth more than the marginal security benefit of hiding them. Worth revisiting if that calculus ever changes.
