#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("Usage: security-audit.py <path>")
    sys.exit(1)

path = sys.argv[1]
print(f"Running security audit on {path}")
# Placeholder for CodeQL/Trivy scans
