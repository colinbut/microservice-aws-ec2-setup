#!/bin/bash
yum update -y
yum install java-1.8.0-openjdk -y
curl --silent --location https://rpm.nodesource.com/setup_10.x | bash -
yum install nodejs -y