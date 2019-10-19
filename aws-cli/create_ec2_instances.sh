#!/bin/bash
aws ec2 run-instances --image-id ami-00a1270ce1e007c27 --count 1 --instance-type t2.micro --key-name MyLondonKP