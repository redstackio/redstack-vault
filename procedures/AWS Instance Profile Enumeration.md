---
id: 6a49a245-e63c-4aad-9cfa-7ea80f73dffe
name: AWS Instance Profile Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.510160+00:00'
updated_at: '2023-04-10T20:20:24.671628+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Instance Metadata API|T1522 - Cloud Instance Metadata API]]'
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Exploitation]]'
- '[[Listing instance profiles]]'
- '[[Privilege Escalation]]'
commands:
- '[[List Instance Profiles]]'
---

# AWS Instance Profile Enumeration

## Summary

AWS Instance Profiles are used to grant permissions to EC2 instances. An attacker can list instance profiles to identify which permissions are available, and use them to escalate privileges. This technique is often used in combination with other AWS enumeration techniques to map the target environm

## Description

# Description

AWS Instance Profiles are used to grant permissions to EC2 instances. An attacker can list instance profiles to identify which permissions are available, and use them to escalate privileges. This technique is often used in combination with other AWS enumeration techniques to map the target environment. To list instance profiles, an attacker can use the ListInstanceProfiles API or access the instance metadata service. 

Technical Explanation: Instance profiles are associated with EC2 instances and contain an IAM role that grants permissions. By listing instance profiles, an attacker can identify which permissions are associated with the role, potentially leading to privilege escalation. The AWS Instance Metadata Service provides a RESTful API that allows EC2 instances to access instance metadata and user data. An attacker can use this service to retrieve sensitive information about the instance, including the instance profile. 

Business Value: An attacker can use this technique to gain access to sensitive data or resources in an AWS environment, potentially leading to data theft, data manipulation, or service disruption.

 

## Requirements

1. Valid AWS credentials with permission to list instance profiles

1. Access to the AWS console or AWS CLI

1. Access to the AWS instance metadata service

 

## Defense

1. Ensure that IAM roles associated with instance profiles have the least privilege necessary

1. Monitor AWS CloudTrail logs for suspicious activity related to instance profiles

1. Disable the AWS instance metadata service if it is not needed

 

## Objectives

1. Identify which instance profiles are available in the target AWS environment

1. Determine which permissions are associated with each instance profile

1. Escalate privileges by assuming the role associated with an instance profile

 

# Instructions

1. This command lists all the instance profiles in your AWS account.

 

The 'aws iam list-instance-profiles' command is used to retrieve a list of all the instance profiles in your AWS account. An instance profile is a container for an AWS Identity and Access Management (IAM) role that you can use to pass role information to an EC2 instance when the instance starts. This command does not take any arguments or options.



**Command** ([[List Instance Profiles]]):

```bash
aws iam list-instance-profiles
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Instance Metadata API|T1522 - Cloud Instance Metadata API]]
- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List Instance Profiles]]

## Tags

- [[Cloud - AWS]]
- [[Exploitation]]
- [[Listing instance profiles]]
- [[Privilege Escalation]]


