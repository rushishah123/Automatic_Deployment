#!/usr/bin/env python3
import json
import sys
from jsonschema import validate, ValidationError

if len(sys.argv) < 2:
    print("Usage: validate-config.py <config>")
    sys.exit(1)

config_path = sys.argv[1]
with open(config_path) as f:
    data = json.load(f)

with open('config/deploy-schema.json') as f:
    schema = json.load(f)

try:
    validate(instance=data, schema=schema)
except ValidationError as e:
    print(f"Validation failed: {e}")
    sys.exit(1)
print("Validation successful")
