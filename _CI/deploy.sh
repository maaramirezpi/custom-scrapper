#!/bin/bash
set -e

if [[ -d "infra" ]]; then
    cd infra

    npm run cdk deploy -- \
        --all \
        --require-approval never
fi