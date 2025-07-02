#!/usr/bin/env python3
import sys
import requests

url = "https://patient-portal.example.com/health"
if len(sys.argv) > 1:
    url = sys.argv[1]

try:
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Health check failed: {response.status_code}")
        sys.exit(1)
    print("Health check passed")
except Exception as e:
    print(f"Health check error: {e}")
    sys.exit(1)
