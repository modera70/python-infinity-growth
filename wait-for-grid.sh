#!/bin/bash
# wait-for-grid.sh

set -e

cmd="$@"

while ! curl -sSL "${HUB_URL:-http://localhost:4444}/wd/hub/status" 2>&1 \
        | jq -r '.value.ready' 2>&1 | grep "true" >/dev/null; do
    echo 'Waiting for the Grid'
    sleep 1
done

>&2 echo "Executing tests"
$cmd
