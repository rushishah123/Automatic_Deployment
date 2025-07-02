# Healthcare Deploy System

This repository contains an example CI/CD pipeline for deploying the **patient-portal** healthcare application. It demonstrates a secure, compliant and cost-optimized workflow using GitHub Actions and Terraform.

## Directory Structure

```
healthcare-deploy-system/
├── .github/workflows/universal-deploy.yml
├── config/deploy-schema.json
├── applications/patient-portal/deploy-config.json
├── terraform/
│   ├── backend.tf
│   └── main.tf
├── scripts/
│   ├── validate-config.py
│   ├── security-audit.py
│   ├── cost-estimator.py
│   ├── check-deployment-state.py
│   ├── plan-infrastructure.py
│   ├── deploy-infrastructure.py
│   ├── update-deployment-state.py
│   ├── health-checks.py
│   └── comprehensive-test.py
└── README.md
```

## Setup

1. Install dependencies:
   ```bash
   pip install jsonschema requests
   sudo apt-get install terraform awscli -y
   ```
2. Configure AWS credentials so Terraform and the scripts can access your account.
3. Initialize the Terraform backend:
   ```bash
   terraform -chdir=terraform init
   ```
4. Commit and push changes to GitHub to trigger the deployment workflow.
