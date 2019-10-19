terraform {
    backend "s3" {
        bucket = "cb-microservice-aws-ec2-setup"
        key = "ec2-infra"
        region = "eu-west-2"
    }
    required_version = ">= 0.12.4"
}

provider "aws" {
  region = "${region}"
}
