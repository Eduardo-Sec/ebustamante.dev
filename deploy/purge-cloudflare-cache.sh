#!/bin/bash
# Purge /resume/ and its legacy redirect targets from Cloudflare's edge
# cache after publishing a new resume. The extensionless /resume/ URL
# isn't cached by Cloudflare's default rules (confirmed via cf-cache-status:
# DYNAMIC), but the /static/... paths are, so this covers both in case
# that ever changes.
#
# Requires CF_API_TOKEN (Zone > Cache Purge permission, scoped to this
# zone) and CF_ZONE_ID as environment variables. Without them, prints the
# manual dashboard steps instead of failing.
set -euo pipefail

URLS=(
    "https://ebustamante.dev/resume/"
    "https://ebustamante.dev/static/resume.pdf"
)

if [ -z "${CF_API_TOKEN:-}" ] || [ -z "${CF_ZONE_ID:-}" ]; then
    cat >&2 <<EOF
No CF_API_TOKEN / CF_ZONE_ID set -- purge manually instead:

  Cloudflare dashboard > ebustamante.dev > Caching > Configuration >
  Purge Cache > Custom Purge, and enter:
$(printf '    %s\n' "${URLS[@]}")

To automate this next time, create a token in the dashboard scoped to
Zone > Cache Purge for this zone only, then export CF_API_TOKEN and
CF_ZONE_ID before re-running this script.
EOF
    exit 0
fi

json_urls=$(printf '"%s",' "${URLS[@]}")
json_urls="[${json_urls%,}]"

curl -s -X POST "https://api.cloudflare.com/client/v4/zones/${CF_ZONE_ID}/purge_cache" \
    -H "Authorization: Bearer ${CF_API_TOKEN}" \
    -H "Content-Type: application/json" \
    --data "{\"files\": ${json_urls}}"
echo
