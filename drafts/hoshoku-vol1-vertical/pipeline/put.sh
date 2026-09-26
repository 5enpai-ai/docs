#!/bin/bash
# usage: put.sh file signURL
curl -sS -X PUT -H "Content-Type: image/png" -H "Content-Length: $(stat -c%s "$1")" --data-binary @"$1" -o /dev/null -w "$1 %{http_code}\n" "$2"
