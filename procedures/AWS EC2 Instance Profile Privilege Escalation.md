---
id: 956735b5-bb28-4c5f-8c29-908fe72e84b0
name: AWS EC2 Instance Profile Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.533522+00:00'
updated_at: '2023-04-10T20:20:54.100763+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Cloud Instance Metadata API|T1522 - Cloud Instance Metadata API]]'
tags:
- '[[Attach an instance profile to an EC2 instance]]'
- '[[Cloud - AWS]]'
- '[[Exploitation]]'
- '[[Privilege Escalation]]'
commands:
- '[[Associate IAM Instance Profile]]'
---

# AWS EC2 Instance Profile Privilege Escalation

## Summary

AWS EC2 Instance Profile Privilege Escalation is a technique used to escalate privileges of an EC2 instance by attaching an instance profile with elevated permissions. This technique can be used by attackers to gain access to sensitive data, execute unauthorized actions, or move laterally within th

## Description

# Description

AWS EC2 Instance Profile Privilege Escalation is a technique used to escalate privileges of an EC2 instance by attaching an instance profile with elevated permissions. This technique can be used by attackers to gain access to sensitive data, execute unauthorized actions, or move laterally within the cloud environment. 

To execute this technique, the attacker must first identify an EC2 instance with a low privileged instance profile attached. The attacker can then attach a new instance profile with elevated permissions to the EC2 instance. Once the instance profile is attached, the attacker can use the elevated permissions to execute unauthorized actions within the cloud environment.

This technique can be valuable for attackers looking to gain access to sensitive data or execute unauthorized actions within a cloud environment.

 

## Requirements

1. Access to an EC2 instance with a low privileged instance profile attached

1. Ability to attach an instance profile with elevated permissions to the EC2 instance

 

## Defense

1. Ensure that instance profiles are not assigned excessive permissions

1. Monitor changes to instance profiles attached to EC2 instances

1. Implement network segmentation to limit lateral movement within the cloud environment

 

## Objectives

1. Escalate privileges of an EC2 instance

1. Gain access to sensitive data

1. Execute unauthorized actions within a cloud environment

 

# Instructions

1. To associate an IAM instance profile with an EC2 instance, use the following command:

 

The 'aws ec2 associate-iam-instance-profile' command is used to associate an IAM instance profile with an EC2 instance. This allows the instance to access the resources that are defined in the instance profile. 

The required arguments for this command are: 

1. --instance-id: The ID of the EC2 instance you want to associate the IAM instance profile with. 

2. --iam-instance-profile: The name and ARN of the IAM instance profile you want to associate with the instance. 

Example usage: 

aws ec2 associate-iam-instance-profile --instance-id i-1234567890abcdef0 --iam-instance-profile Name=MyInstanceProfile



**Command** ([[Associate IAM Instance Profile]]):

```bash
aws ec2 associate-iam-instance-profile --instance-id ID --iam-instance-profile Name=ProfileName
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Cloud Instance Metadata API|T1522 - Cloud Instance Metadata API]]

## Commands Used

- [[Associate IAM Instance Profile]]

## Tags

- [[Attach an instance profile to an EC2 instance]]
- [[Cloud - AWS]]
- [[Exploitation]]
- [[Privilege Escalation]]


