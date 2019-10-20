resource "aws_instance" "ec2_instance" {
    ami = "ami-00a1270ce1e007c27"
    instance_type               = "${var.instance_type}"
    key_name                    = "${var.key_name}"
    associate_public_ip_address = true

    tags = {
        Name = "Server"
    }

    provisioner "remote-exec" {
        inline = [
            "sudo yum update -y",
            "sudo yum install java-1.8.0-openjdk -y",
            "sudo curl --silent --location https://rpm.nodesource.com/setup_10.x | bash -",
            "sudo yum install -y nodejs"
        ]

        connection {
            type        = "ssh"
            user        = "ec2-user"
            host        = "${aws_instance.ec2_instance.public_ip}"
            private_key = file("~/dev/aws/MyLondonKP.pem")
        }
    }
    
}
