---
id: 09b9d9d8-da69-48aa-9ba8-b98ca30da806
name: AWS Region Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.231968+00:00'
updated_at: '2023-04-10T20:20:35.846435+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing information about a specific region]]'
commands:
- '[[Describe EC2 Instances]]'
---

# AWS Region Information Gathering

## Summary

AWS Region Information Gathering is a procedure used to gather information about a particular AWS region. The procedure involves using the EC2 Instance Description command to obtain information about instances running in the region. This information can include instance IDs, instance types, securit

## Description

# Description

AWS Region Information Gathering is a procedure used to gather information about a particular AWS region. The procedure involves using the EC2 Instance Description command to obtain information about instances running in the region. This information can include instance IDs, instance types, security groups, and more. This procedure can be used by attackers to map out a target's infrastructure and identify potential targets for further attacks. From a business perspective, this procedure can be used by security teams to identify potential vulnerabilities in their AWS environment.

 

## Requirements

1. Valid AWS credentials with appropriate permissions

1. Access to the AWS console or command line interface

 

## Defense

1. Ensure that AWS credentials are securely stored and not shared

1. Enable multi-factor authentication for AWS accounts

1. Monitor AWS CloudTrail logs for any unauthorized access or changes to the environment

 

## Objectives

1. Gather information about a specific AWS region

1. Identify potential targets for further attacks

1. Identify potential vulnerabilities in the AWS environment

 

# Instructions

1. The 'aws ec2 describe-instances' command is used to retrieve information about one or more Amazon Elastic Compute Cloud (Amazon EC2) instances. This command requires the --region parameter to specify the region where the instances are located.

 

The 'aws ec2 describe-instances' command can be used to retrieve detailed information about one or more Amazon EC2 instances, including their instance IDs, instance types, security groups, and more. This command can be useful for troubleshooting issues with your instances, or for gathering information about your instances for reporting or analysis purposes. The --region parameter is required to specify the region where the instances are located. You can also use filters to narrow down the results of the command, such as by instance ID, tag, or state.



**Command** ([[Describe EC2 Instances]]):

```bash
aws ec2 describe-instances --region region
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Describe EC2 Instances]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing information about a specific region]]


