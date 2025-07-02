provider "aws" {
  region = "us-east-1"
}

resource "aws_ecs_cluster" "patient_portal" {
  name = "patient-portal-cluster"
}
