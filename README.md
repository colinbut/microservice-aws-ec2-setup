# Microservice AWS EC2 Setup

This project provides the steps/methods required for setup an EC2 instance for running the microservice as defined in the microservice-aws-demo project.

There are many ways to setup EC2 instances in AWS:

1) via __AWS mamagement console__ creating from scratch
2) using Infrastructure as Code tool (__Terraform/Cloudformation__)
3) __AWS CLI__
4) utilizing a pre-build custom made __AMI__ for any of above methods

## Assumptions
1. Assumes a AWS account created and AWS credentials configured (access_keys & secret_keys etc)

2. This project will create EC2 instances in the default VPC.

3. To put in a custom non-default VPC require to create the custom non-default VPC.
See https://github.com/colinbut/aws-public-private-vpc for more reference on to create this. 

## Option 1 - AWS Management Console

[TBD]

## Option 2 - Terraform/Cloudformation

#### Terraform 
Create S3 bucket to store terraform state. Need to ensure bucket is unique and also ideally within same region you want to provision your infrastructure resources onto.

```bash
aws s3 mb s3://[name of bucket] --region [region]
```

Initialize Terraform Backend
```bash
terraform init
```

Validating the terraform configuration files syntax is correct:
```bash
terraform validate
```

When make changes it is always a good idea to run `terraform plan` to check the changes are what you intend to make... even though `terraform apply` does prompt you confirm (if run without the `--auto-approve` option)
```bash
terraform plan
```

To apply your infrastructure changes (creation/modifications)
```bash
terraform apply
```

#### Cloudformation
[TBD]


## Option 3 - AWS CLI

There's a pre-made `` script (available in both Bash & Python) that wraps around the AWS CLI command call. To use:

```bash
create_ec2_instances.sh
```

or using Python:
```python
python create_ec2_instances.py
```

The scripts basically just does the following underneath the hood:

```bash
aws ec2 run-instances --image-id [ami-id] --count 1 --instance-type t2.micro --key-name [KeyPair Name] --user-data [provisioning script]
```

## Option 4 - from pre-build tailored AMI

Uses Packer to build the AMI.
Configure a Jenkins job that will validate the packer template whilst making changes.

To build & deploy to your AWS account:

```bash
packer build microservice-*.json
``` 