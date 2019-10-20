variable "region" {
  type        = "string"
  description = "The region to use for provisioning infrastructure"
  default     = "eu-west-2"
}

variable "instance_type" {
  type          = "string"
  description   = "The instance type of the EC2 instance to provision"
}

variable "key_name" {
  type          = "string"
  description   = "The name of the Key Pair used to authenticate into the provisioned EC2 instance"
}

