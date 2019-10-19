# Microservice AWS EC2 Setup

Assumes you have a AWS account created and your AWS credentials configured (access_keys & secret_keys etc)

This project will create EC2 instances in the default VPC.

To put in a custom non-default VPC require to create the custom non-default VPC.
See https://github.com/colinbut/aws-public-private-vpc for more reference on to create this. 

## Option 1 - AWS Management Console

[TBD]

## Option 2 - Terraform/Cloudformation

Create S3 bucket to store terraform state

```bash
aws s3 mb s3://[name of bucket] --region [region]
```

Initialize Terraform Backend
```bash
terraform init
```

## Option 3 - from pre-build tailored AMI

Uses Packer to build the AMI.
Configure a Jenkins job that will validate the packer template whilst making changes.

To build & deploy to your AWS account:

```bash
packer build microservice-*.json
``` 

## Option 4 - AWS CLI

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
