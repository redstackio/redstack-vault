---
id: cab0aee2-a8cf-4c66-b531-28c0bde59549
type: code
language: Terraform
verified: false
created_at: '2020-03-17T05:48:40.444899+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet cab0aee2

**Language**: Terraform

```terraform
### kali-linux.tf
provider "aws" {
  region = "${var.region}"
  profile = "${var.aws_profile}"
}

### Variable Definitions
variable "region" {
  type = "string"
  default = "ca-central-1"
  description = "AWS Region"
}

variable "ami" {
  type = "map"
  default = {
    "ca-central-1"  = "ami-0a4f8e0a63f86f21c"
    "us-east-1"     = "ami-0a3803e4b51dabb6d"
    "us-west-2"     = "ami-0b2a11e35e8b89bf1"
  }
  description = "AMI's in North America Regions"
}

variable "aws_profile" {
  type = "string"
  default = "hacker"
  description = "AWS IAM Access Key Profile"
}

variable "ssh_key" {
  type = "string"
  default = "~/.ssh/id_rsa.pub"
  description = "SSH KeyPair"
}

variable "ec2_type" {
  type = "string"
  default = "t2.small"
  description = "Type of EC2 Instance"
}

### Create Security Group to allow all traffic to Kali
# Keep all ports open for reverse shells, ad-hoc services, etc.
resource "aws_security_group" "openports" {
  name = "openports"
  description = "open all ports for pentesting"

  ingress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 8
    to_port = 0
    protocol = "icmp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create an AWS SSH Key Pair for the kali instance
resource "aws_key_pair" "ssh_key_pair" {
  key_name = "kali"
  public_key = "${file("${var.ssh_key}")}"
}

locals {
  ssh_key_name = "${aws_key_pair.ssh_key_pair.key_name}"
  userdata = <<EOF
#cloud-config
users:
  - default
  - name: hacker
    groups: sudo
    shell: /bin/bash
    sudo: ['ALL=(ALL) NOPASSWD:ALL']
    ssh_pwauth: True
    ssh-authorized-keys:
      - "${file("${var.ssh_key}")}"
chpasswd:
  list: |
    root:iamgroot
    hacker:iamhacker
  expire: False
write_files:
  - path: /etc/apt/sources.list
    contents: |
      deb http://http.kali.org/kali kali-rolling main contrib non-free
      deb-src http://http.kali.org/kali kali-rolling main contrib non-free
runcmd:
  - sed -i -e '/^PasswordAuthentication/s/^.*$/PasswordAuthentication yes/' /etc/ssh/sshd_config
  - restart ssh
  - apt-get update
  - apt-get upgrade -y
EOF
}

### Create the Kali Ec2 Instance
resource "aws_instance" "kali" {
  ami                     = "${lookup(var.ami,var.region)}"
  instance_type           = "${var.ec2_type}"
  vpc_security_group_ids  = ["${aws_security_group.openports.id}"]
  key_name                = "${local.ssh_key_name}"
  user_data               = "${local.userdata}"
}

output "kali-linux" {
  value = "${formatlist(" ssh hacker@%v ", aws_instance.kali.*.public_ip)}"
}
```


