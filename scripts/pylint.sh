#! /usr/bin/env bash

set -euo pipefail

main() {
    pylint cstruct --errors-only
}

main "$@"
