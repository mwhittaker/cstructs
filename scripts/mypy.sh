#! /usr/bin/env bash

set -euo pipefail

main() {
    mypy cstruct --ignore-missing-imports
}

main "$@"
