locals {
  instance_bootstrap = <<EOF
  #!/bin/bash
  yum update -y
  yum install java-1.8.0-openjdk -y
  curl --silent --location https://rpm.nodesource.com/setup_10.x | bash -
  yum install nodejs -y
  EOF
}

data "template_file" "instance_userdata" {
    template = "${file("${path.cwd}/ec2/instance-bootstrap.tpl")}"
}

resource "aws_instance" "ec2_instance" {
    ami = "ami-00a1270ce1e007c27"
    count = 2
    instance_type               = "${var.instance_type}"
    key_name                    = "${var.key_name}"
    associate_public_ip_address = true
    vpc_security_group_ids      = ["sg-0f89322a79aa4a404"] # ensure security group has SSH access
    #user_data = "${base64encode(local.instance_bootstrap)}"
    user_data = "${data.template_file.instance_userdata.template}"

    tags = {
        Name          = "Microservice-Server"
        ProvisionedBy = "Terraform"
    }
    
}
