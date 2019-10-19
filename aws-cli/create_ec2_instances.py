import subprocess

ami = 'ami-00a1270ce1e007c27'
no_of_instances = 1
instance_type = 't2.micro'
keyPair = 'MyLondonKP'

aws_create_instance_cli_command ='aws ec2 run-instances --image-id ' + ami + ' --count ' + str(no_of_instances) + ' --instance-type ' + instance_type + ' --key-name ' + keyPair

print("Running aws cli command: ")
print(aws_create_instance_cli_command)

subprocess.call(aws_create_instance_cli_command.split(' '))