#/bin/sh

if [[ $# -eq 1 ]]; then
    ENVIRONMENT="${1}"
    echo "PYTH_BIN=${ENVIRONMENT}" >> .env
else
    rm -f .env
fi
