#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("Usage: cost-estimator.py <path>")
    sys.exit(1)

path = sys.argv[1]
print(f"Estimating cost for {path}")
# Placeholder for cost estimation logic
