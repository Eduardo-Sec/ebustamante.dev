#!/bin/bash
# Deployment update script — run after every git push.
# Usage: ssh user@REDACTED 'sudo bash /opt/ebustamante/deploy/update.sh'
#
# Runs as root so it can restart the systemd service, but every step
# that touches app files (git, pip, manage.py) drops to the ebustamante
# user via sudo -u -- running those as root instead pollutes .git/.venv
# with root-owned files and breaks future non-root git/pip operations.
set -euo pipefail

APP_DIR="/opt/ebustamante"
APP_USER="ebustamante"

echo "==> Pulling latest code"
sudo -u "$APP_USER" git -C "$APP_DIR" pull

echo "==> Installing any new dependencies"
sudo -u "$APP_USER" "$APP_DIR/.venv/bin/pip" install -r "$APP_DIR/requirements.txt" --quiet

echo "==> Running migrations"
sudo -u "$APP_USER" "$APP_DIR/.venv/bin/python" "$APP_DIR/manage.py" migrate --noinput

echo "==> Collecting static files"
sudo -u "$APP_USER" "$APP_DIR/.venv/bin/python" "$APP_DIR/manage.py" collectstatic --noinput

echo "==> Importing new writeups"
sudo -u "$APP_USER" "$APP_DIR/.venv/bin/python" "$APP_DIR/manage.py" import_writeups

echo "==> Restarting gunicorn"
systemctl restart ebustamante

echo "==> Done. Site is live."
