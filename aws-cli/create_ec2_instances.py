import os
import subprocess

ami = 'ami-00a1270ce1e007c27'
no_of_instances = 1
instance_type = 't2.micro'
keyPair = 'MyLondonKP'

# TODO take this in as an arg
provisioning_script = 'install_nodejs.sh'

aws_cli_command_args = {
    'ami': ami,
    'no_of_instances': str(no_of_instances),
    'instance_type': instance_type,
    'keyPair' : keyPair,
    'provisioning_script': provisioning_script
}

aws_create_instance_cli_command = "aws ec2 run-instances --image-id {ami} --count {no_of_instances} --instance-type {instance_type} --key-name {keyPair} --user-data file://provisioning-scripts/{provisioning_script}".format(**aws_cli_command_args)

print("Running aws cli command: ")
print(aws_create_instance_cli_command)

subprocess.call(aws_create_instance_cli_command.split(' '))