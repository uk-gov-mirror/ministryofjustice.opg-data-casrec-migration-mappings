#!/bin/bash
docker-compose run --rm generate python3 app.py --local=True
mv app/mapping_definitions/ mapping_definitions/
