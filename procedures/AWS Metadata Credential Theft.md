---
id: c7b1d7e7-7edc-4a57-9900-908c48873cec
name: AWS Metadata Credential Theft
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:13.347335+00:00'
updated_at: '2023-04-10T20:20:07.318297+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Credentials in Files|T1081 - Credentials in Files]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[AWS Metadata]]'
- '[[Cloud - AWS]]'
- '[[Exploitation]]'
- '[[Grabbing the keys to access the instance]]'
- '[[Remote code execution]]'
commands:
- '[[Retrieve EC2 Instance Credentials]]'
---

# AWS Metadata Credential Theft

## Summary

AWS Metadata Credential Theft is a technique used by attackers to steal the AWS access keys of an EC2 instance by exploiting the instance metadata service. The instance metadata service is a web service provided by AWS that allows EC2 instances to learn about themselves without the need for externa

## Description

# Description

AWS Metadata Credential Theft is a technique used by attackers to steal the AWS access keys of an EC2 instance by exploiting the instance metadata service. The instance metadata service is a web service provided by AWS that allows EC2 instances to learn about themselves without the need for external authentication. Attackers can use this service to retrieve sensitive information such as AWS access keys, which can then be used to access other AWS resources. This technique can be used to escalate privileges and gain access to sensitive data.

 

## Requirements

1. Access to an EC2 instance

1. Knowledge of the EC2 instance metadata service

1. Ability to execute commands on the instance

 

## Defense

1. Restrict access to the instance metadata service by using IAM roles and policies

1. Monitor the instance metadata service for unusual activity

1. Use AWS Security Hub to detect and respond to potential attacks

 

## Objectives

1. Steal AWS access keys of an EC2 instance

1. Escalate privileges

1. Gain access to sensitive data

 

# Instructions

1. To retrieve the security credentials for an EC2 instance, run the following command:

 

This command uses the cURL utility to make an HTTP request to the metadata service of an EC2 instance. The metadata service provides information about the instance, including its security credentials. The command sends a request to the security-credentials endpoint to retrieve the security credentials for the instance. These credentials can be used to authenticate requests to other AWS services.



**Command** ([[Retrieve EC2 Instance Credentials]]):

```bash
curl http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Credentials in Files|T1081 - Credentials in Files]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Retrieve EC2 Instance Credentials]]

## Tags

- [[AWS Metadata]]
- [[Cloud - AWS]]
- [[Exploitation]]
- [[Grabbing the keys to access the instance]]
- [[Remote code execution]]


