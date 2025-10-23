---
id: 54149739-f9b8-4a7a-9b80-95ae0d42c8d3
name: AWS EC2 IAM Instance Profile Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.298595+00:00'
updated_at: '2023-04-10T20:20:19.423372+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
- '[[Credential Dumping|T1003 - Credential Dumping]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing roles of an instance]]'
---

# AWS EC2 IAM Instance Profile Enumeration

## Summary

AWS EC2 instances utilize IAM roles to grant permissions to the applications running on them. By enumerating the roles attached to an instance, an attacker can gain insight into the level of access the application running on the instance has to other AWS services. This information can be used to pl

## Description

# Description

AWS EC2 instances utilize IAM roles to grant permissions to the applications running on them. By enumerating the roles attached to an instance, an attacker can gain insight into the level of access the application running on the instance has to other AWS services. This information can be used to plan further attacks against the AWS environment.

To list the roles attached to an instance, an attacker can use the AWS CLI or AWS CloudTrail to view the instance metadata. The AWS CLI command 'EC2 IAM Instance Profile Associations' can be used to retrieve the IAM roles attached to an instance. 

Knowing the roles attached to an instance can be valuable information for both red and blue teams. Red teams can use this information to plan further attacks against the AWS environment, while blue teams can use this information to identify instances with overly permissive roles and take action to remediate them.

 

## Requirements

1. Valid AWS credentials with permissions to list EC2 instances

 

## Defense

1. Restrict access to the AWS IAM service to only authorized users and roles

1. Implement the principle of least privilege when assigning IAM roles to EC2 instances

1. Monitor AWS CloudTrail logs for suspicious activity related to IAM role enumeration

 

## Objectives

1. Identify the IAM roles attached to an EC2 instance

1. Gain insight into the level of access the application running on the instance has to other AWS services

 

# Instructions

1. Use this command to describe the IAM instance profile associations for the specified instances or a specified IAM instance profile. This command returns a list of instance profiles that are associated with the specified instances, or a list of instances that are associated with the specified instance profile.

 

The 'describe-iam-instance-profile-associations' command is used to retrieve information about the IAM instance profile associations for EC2 instances. This command can be used to retrieve information about the instance profiles associated with a specific instance or to retrieve information about the instances associated with a specific instance profile. The command takes no arguments and returns a JSON object containing information about the instance profiles or instances.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]
- [[Credential Dumping|T1003 - Credential Dumping]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing roles of an instance]]


