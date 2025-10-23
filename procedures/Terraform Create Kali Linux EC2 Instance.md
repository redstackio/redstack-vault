---
id: 126a4fb8-83a1-4a2d-80c2-2b8c629a4c9a
name: Terraform Create Kali Linux EC2 Instance
type: procedure
verified: true
submitted: true
created_at: '2019-10-11T16:41:20.166468+00:00'
updated_at: '2023-05-25T20:04:01.573232+00:00'
tactics:
- '[[Stage Capabilities|TA0026 - Stage Capabilities]]'
techniques:
- '[[Upload, install, and configure software/tools|T1362 - Upload, install, and configure
  software/tools]]'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
- '[[ec2]]'
commands:
- '[[Terraform Apply]]'
- '[[Terraform Destroy]]'
- '[[Terraform Initialization]]'
---

# Terraform Create Kali Linux EC2 Instance

**Status**: ✓ Verified

## Summary

During red team engagements you may need to bring up a fresh Kali linux instance on a public ip. Using Terraform scripting this tasks is accomplished in seconds from the command line. 

## Description

# Description

During red team engagements you may need to bring up a fresh Kali linux instance on a public ip. Using Terraform scripting this tasks is accomplished in seconds from the command line.



# Requirements

AWS API Access Key stored in the credentials file. Use an existing IAM users Access Key on your AWS account or generate a new IAM user and an Access Key. It's a good idea to name the key in the credentials file to easily recall which Access Key is for which AWS account. RedStack will always use "hacker" for the attacker systems, and "target" for the targets.





**Code**: [[# ~/.aws/credentials
[hacker]
aws_access_key_id = ]]



## Tools

- awscli

- Terraform



## Setup

1. On the hacker system create a new Working Directory "workdir" and you will make 1 file inside:

2. Create the kali-linux.tf file and paste in the Terraform code below.

This script handles a few functions like:

- create a ssh key pair

- create an ec2 security group

- create an ec2 instance

- execute a cloud-init config in the new ec2 instance

This config creates a new user, configures it's password and rsa key, allows ssh with passwords and updates the system.

Update the passwords to something complex, and ensure the ssh_key variable is pointing to the desired ssh key. You are responsible for the security of your ec2 instances and users.



**Code**: [[### kali-linux.tf
provider "aws" {
  region = "${v]]





# Instructions

With the new files inside the "workdir" first initialize Terraform to setup the modules and providers needed for the TF script.





**Command** ([[Terraform Initialization]]):

```bash
terraform init
```



Next apply the configuration.

Note: This step will create the kali linux ec2 instance on your AWS account and you will be billed for their usage by AWS Amazon.





**Command** ([[Terraform Apply]]):

```bash
terraform apply -auto-approve
```





When this part of the pentest is complete, destroy the infrastructure this script created:





**Command** ([[Terraform Destroy]]):

```bash
terraform destroy -auto-approve
```







## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Stage Capabilities|TA0026 - Stage Capabilities]]

### Techniques

- [[Upload, install, and configure software/tools|T1362 - Upload, install, and configure software/tools]]

## Commands Used

- [[Terraform Apply]]
- [[Terraform Destroy]]
- [[Terraform Initialization]]

## Tags

- [[AWS]]
- [[Cloud]]
- [[ec2]]


