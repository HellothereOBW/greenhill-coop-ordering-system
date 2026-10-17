#!/usr/bin/env bash
# Validate and run the local demo. Not a production deployment script.
set -euo pipefail
cd "$(dirname "$0")"
python -m pip install -r requirements.txt
python -m pytest -q
exec python -m flask --app app run --host 127.0.0.1
