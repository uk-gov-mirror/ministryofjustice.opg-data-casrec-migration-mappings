#!/bin/bash
docker-compose run --rm generate python3 app.py --local=True
rm -r mapping_definitions
mv app/mapping_definitions/ mapping_definitions/
