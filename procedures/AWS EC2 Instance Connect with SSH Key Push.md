---
id: 9c5d72c3-496e-4f27-af27-1c6204a67004
name: AWS EC2 Instance Connect with SSH Key Push
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:09.637114+00:00'
updated_at: '2023-04-10T20:19:45.225862+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Valid Accounts|T1078 - Valid Accounts]]'
- '[[Web Shell|T1100 - Web Shell]]'
tags:
- '[[AWS - Instance Connect - Push an SSH key to EC2 instance]]'
- '[[Cloud - AWS]]'
commands:
- '[[Describe EC2 instances]]'
- '[[Send SSH public key]]'
---

# AWS EC2 Instance Connect with SSH Key Push

## Summary

This procedure outlines the steps to push an SSH key to an Amazon EC2 instance using AWS Instance Connect. This allows for secure SSH access to the instance without the need for a bastion host or exposing SSH ports to the internet. This procedure is useful for system administrators and developers w

## Description

# Description

This procedure outlines the steps to push an SSH key to an Amazon EC2 instance using AWS Instance Connect. This allows for secure SSH access to the instance without the need for a bastion host or exposing SSH ports to the internet. This procedure is useful for system administrators and developers who need secure and convenient SSH access to EC2 instances.

## Requirements

1. AWS account with EC2 instances

1. AWS CLI or AWS Management Console

1. SSH key pair for authentication

## Defense

1. Limit access to AWS resources using IAM roles and policies

1. Enable VPC Flow Logs to monitor network traffic

1. Use AWS Security Groups to restrict access to EC2 instances

## Objectives

1. Push an SSH key to an EC2 instance for secure SSH access

1. Reduce the need for a bastion host or exposing SSH ports to the internet

1. Enable system administrators and developers to have secure and convenient SSH access to EC2 instances

# Instructions

1. To use Amazon EC2 Instance Connect for SSH access to your EC2 instances, follow these steps:
1. Use the following command to describe the instances in your account:
   aws ec2 describe-instances --profile uploadcreds --region eu-west-1 | jq ".[][].Instances | .[] | {InstanceId, KeyName, State}"
2. Note the InstanceId of the instance you want to connect to.
3. Use the following command to send your SSH public key to the instance:
   aws ec2-instance-connect send-ssh-public-key --region us-east-1 --instance-id INSTANCE --availability-zone us-east-1d --instance-os-user ubuntu --ssh-public-key file://shortkey.pub --profile uploadcreds
   Replace INSTANCE with the InstanceId of the instance you want to connect to.
4. Connect to the instance using SSH.

**Code**: [[# https://aws.amazon.com/fr/blogs/compute/new-usin]]

> The first command is used to describe the instances in your account, and returns the InstanceId, KeyName, and State of each instance. The second command is used to send your SSH public key to the instance you want to connect to. Replace INSTANCE with the InstanceId of the instance you want to connect to. Once you have sent your SSH public key to the instance, you can connect to it using SSH.

**Command** ([[Describe EC2 instances]]):

```bash
$ aws ec2 describe-instances --profile uploadcreds --region eu-west-1 | jq ".[][].Instances | .[] | {InstanceId, KeyName, State}"
```

**Command** ([[Send SSH public key]]):

```bash
$ aws ec2-instance-connect send-ssh-public-key --region us-east-1 --instance-id INSTANCE --availability-zone us-east-1d --instance-os-user ubuntu --ssh-public-key file://shortkey.pub --profile uploadcreds
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Valid Accounts|T1078 - Valid Accounts]]
- [[Web Shell|T1100 - Web Shell]]

## Commands Used

- [[Describe EC2 instances]]
- [[Send SSH public key]]

## Tags

- [[AWS - Instance Connect - Push an SSH key to EC2 instance]]
- [[Cloud - AWS]]
