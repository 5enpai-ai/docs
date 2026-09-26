#!/bin/bash
# usage: fetch.sh cdn_url outname
u="${1/https:\/\/cdn.openart.ai\//https://storage.googleapis.com/cdn.openart.ai/}"
curl -sS -o "gen/$2" -w "$2 %{http_code}\n" "$u"
