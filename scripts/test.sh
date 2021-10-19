#!/usr/bin/env bash

set -e
set -x

pytest --cov=py_moysklad --cov=tests --cov-report=term-missing
