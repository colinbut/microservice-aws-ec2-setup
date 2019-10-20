#!/bin/bash
yum update -y
yum install -y java-1.8.0-openjdk
curl --silent --location https://rpm.nodesource.com/setup_10.x | bash -
yum install -y nodejs