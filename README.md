# Microservice AWS EC2 Setup

This project provides the steps/methods required for setup an EC2 instance for running the microservice as defined in the [microservice-aws-demo](https://github.com/colinbut/microservice-aws-demo.git) project.

There are many ways to setup EC2 instances in AWS:

1) via __AWS mamagement console__ creating from scratch
2) using Infrastructure as Code tool (__Terraform/Cloudformation__)
3) __AWS CLI__
4) utilizing a pre-build custom made __AMI__ for any of above methods

## Assumptions
1. Assumes a AWS account created and AWS credentials configured (access_keys & secret_keys etc)

2. This project will create EC2 instances in the default VPC.

3. To put in a custom non-default VPC require to create the custom non-default VPC.
See my Terraform project - [aws-public-private-vpc](https://github.com/colinbut/aws-public-private-vpc) for more reference on to create this. 

## Option 1 - AWS Management Console

[TBD]

## Option 2 - Terraform/Cloudformation
It is good to manage infrastructure changes and define them in 'code'. This option details how to do this via modern infrastructure as code tools such as __Terraform__ and __AWS Cloudformation__

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

Go to the Cloudformation directory and execute following command from the AWS CLI:

```bash
aws cloudformation create-stack --stack-name microservice-ec2-instance --template-body file://ec2_instances.yml
```

the --stack-name you can provide anything.

## Option 3 - AWS CLI

Can also create the required EC2 instances via the __AWS CLI__

There's a pre-made `create_ec2_instances` script (available in both Bash & Python) that wraps around the AWS CLI command call. To use:

```bash
create_ec2_instances.sh
```

or using Python:
```python
python create_ec2_instances.py
```

The scripts basically just does the following aws cli command underneath the hood:

```bash
aws ec2 run-instances --image-id [ami-id] --count 1 --instance-type t2.micro --key-name [KeyPair Name] --user-data [provisioning script]
```

## Option 4 - from pre-build custom made AMI

See the [microservice-ami](https://github.com/colinbut/microservice-ami.git) project for more details on the corresponding AMIs for the required development platform.

Possible to uses Packer to build the AMI.

To build & deploy to your AWS account:

e.g. 
```bash
packer build [microservice-*.json]
``` 

The AMI can now be referenced in any of the above 3 methods of creating the EC2 instance.