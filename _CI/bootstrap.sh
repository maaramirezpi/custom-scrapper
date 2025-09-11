#!/bin/bash
set -e

if [[ -d "infra" ]]; then
    cd infra

    echo "Install AWS CDK version"

    npm i -g aws-cdk
    npm ci --include=dev

    echo "Synthesize infra.."

    npm run cdk synth -- \
        --quiet \

fi