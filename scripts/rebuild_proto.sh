#!/bin/bash -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"
# shellcheck source=sourceme
source "$REPO_ROOT/scripts/sourceme"

if ! ls "$PROTO_SRC"/* &>/dev/null; then
    echo "No proto files found in $PROTO_SRC"
    exit 1
fi

protoc -I="$PROTO_SRC" --python_out="$PROTO_OUT" "$PROTO_SRC"/*.proto
protol --create-package --in-place --python-out "$PROTO_OUT" protoc --proto-path "$PROTO_SRC" "$PROTO_SRC"/*.proto
python3 "$REPO_ROOT/scripts/gen_stubs.py"
