#!/bin/bash
# Safety gate for publishing a new resume. Run against the candidate PDF
# BEFORE committing it to files/resume.pdf -- catches accidentally leaking
# the phone number, which is the one piece of contact info this site never
# publishes (email and city are fine, only the number is spam-sensitive).
#
# Usage: deploy/check-resume-pii.sh /path/to/candidate.pdf
set -euo pipefail

FILE="${1:?Usage: $0 /path/to/candidate.pdf}"

if [ ! -f "$FILE" ]; then
    echo "File not found: $FILE" >&2
    exit 1
fi

MATCHES=$(pdftotext "$FILE" - | grep -inE '227-6628' || true)

if [ -n "$MATCHES" ]; then
    echo "Phone number found -- do not publish this file:" >&2
    echo "$MATCHES" >&2
    exit 1
fi

PAGES=$(pdfinfo "$FILE" 2>/dev/null | awk '/^Pages:/ {print $2}')
if [ "$PAGES" != "1" ]; then
    echo "Warning: expected a 1-page resume, this file has ${PAGES:-an unknown number of} pages." >&2
fi

echo "OK: no PII patterns found in $FILE (${PAGES:-?} page(s))."
