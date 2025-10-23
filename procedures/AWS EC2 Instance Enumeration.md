---
id: 9662a66b-4a65-4721-b2c7-bc7567d50412
name: AWS EC2 Instance Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.209511+00:00'
updated_at: '2023-04-10T20:20:29.551840+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing information about all instances]]'
commands:
- '[[List all instances]]'
---

# AWS EC2 Instance Enumeration

## Summary

AWS EC2 Instance Enumeration is the process of discovering all the available EC2 instances in an AWS account. This technique can be used by an attacker to identify potential targets for further attacks or to gain a better understanding of the target environment. This technique can be performed usin

## Description

# Description

AWS EC2 Instance Enumeration is the process of discovering all the available EC2 instances in an AWS account. This technique can be used by an attacker to identify potential targets for further attacks or to gain a better understanding of the target environment. This technique can be performed using the AWS CLI or APIs. The business value of this technique is that it can help an organization identify and manage their cloud assets.

 

## Requirements

1. Valid AWS credentials with permissions to list EC2 instances

1. Access to the AWS CLI or APIs

 

## Defense

1. Ensure that AWS credentials are properly secured and not shared

1. Implement least privilege access controls to limit access to AWS resources

1. Monitor AWS CloudTrail logs for any suspicious activity

 

## Objectives

1. Discover all available EC2 instances in the target AWS account

1. Identify potential targets for further attacks

1. Gain a better understanding of the target environment

 

# Instructions

1. Use this command to describe one or more of your EC2 instances.

 

This command provides details about the specified EC2 instances, such as instance IDs, instance types, security groups, and more. You can use filters to narrow down the results. For example, you can filter by instance ID, instance type, or tag values. This command can be useful for troubleshooting, monitoring, and managing your EC2 instances.



**Command** ([[List all instances]]):

```bash
aws ec2 describe-instances
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List all instances]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing information about all instances]]


