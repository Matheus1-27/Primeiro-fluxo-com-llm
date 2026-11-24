#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd "$(dirname "$0")" && pwd)
exec python3 -m pip install -r "$SCRIPT_DIR/requirements.txt"
