import os
import subprocess
import argparse

JAVA = "java"
NODE_JS = "nodejs"

parser = argparse.ArgumentParser()
parser.add_argument("project_type", help="the type of project to create ec2 instances for", choices=[JAVA, NODE_JS])
parser.add_argument("--no-of-instances", help="number of ec2 instances to provision", type=int, default=1)
parser.add_argument("--instance-type", help="the type of ec2 instance to provision", default="t2.micro")
parser.add_argument("--ami", help="the ami id to provide", default="ami-00a1270ce1e007c27")
parser.add_argument("--key-name", help="The name of the key pair to use for SSH access", default="MyLondonKP")
parser.add_argument("--dry-run", help="Dry run?", action="store_true")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()

ami = args.ami
no_of_instances = args.no_of_instances
instance_type = args.instance_type
keyPair = args.key_name

project_type_provisioning_script_mapping = {
    JAVA : "install_java.sh",
    NODE_JS : "install_nodejs.sh"
}

provisioning_script = project_type_provisioning_script_mapping[args.project_type]

aws_cli_command_args = {
    'ami': ami,
    'no_of_instances': str(no_of_instances),
    'instance_type': instance_type,
    'keyPair' : keyPair,
    'provisioning_script': provisioning_script
}

aws_create_instance_cli_command = "aws ec2 run-instances --image-id {ami} --count {no_of_instances} --instance-type {instance_type} --key-name {keyPair} --user-data file://provisioning-scripts/{provisioning_script}".format(**aws_cli_command_args)

if args.verbose:
    print("Running aws cli command: ")
    print(aws_create_instance_cli_command)

if args.dry_run:
    print("Executing script as a dry run - turn on verbose option using --verbose to see command being executed")
else:
    print("Executing...")
    subprocess.call(aws_create_instance_cli_command.split(' '))