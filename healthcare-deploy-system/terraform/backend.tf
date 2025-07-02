terraform {
  backend "s3" {
    bucket = "myonsite-terraform-state"
    key    = "patient-portal/terraform.tfstate"
    region = "us-east-1"
    dynamodb_table = "myonsite-terraform-lock"
  }
}
