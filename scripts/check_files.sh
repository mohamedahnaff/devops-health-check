#!/usr/bin/env bash
set -u
check_file() {
    if [ -f "$1" ]; then
        printf 'FOUND: %s\n' "$1"
    else
        printf 'MISSING: %s\n' "$1"
    fi
}
for item in README.md health_check.py; do
    check_file "$item"
done
