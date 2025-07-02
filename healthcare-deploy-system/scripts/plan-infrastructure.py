#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("Usage: plan-infrastructure.py <path>")
    sys.exit(1)

path = sys.argv[1]
print(f"Planning infrastructure changes for {path}")
