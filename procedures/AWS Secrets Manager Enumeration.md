---
id: 172e0017-c8e5-4621-810a-23f2ec53c469
name: AWS Secrets Manager Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.104808+00:00'
updated_at: '2023-04-10T20:20:28.872332+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
sub_techniques:
- '[[Local Account|T1087.001 - Local Account]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing information about a specific secret]]'
commands:
- '[[Describe Secret]]'
---

# AWS Secrets Manager Enumeration

## Summary

The AWS Secrets Manager Enumeration procedure involves listing information about a specific secret in AWS Secrets Manager. This can be used by an attacker to discover sensitive information stored in AWS Secrets Manager. AWS Secrets Manager is a secrets management service that helps protect access t

## Description

# Description

The AWS Secrets Manager Enumeration procedure involves listing information about a specific secret in AWS Secrets Manager. This can be used by an attacker to discover sensitive information stored in AWS Secrets Manager. AWS Secrets Manager is a secrets management service that helps protect access to applications, services, and IT resources. It enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. By listing information about a specific secret, an attacker can gain access to sensitive data such as database credentials, API keys, and other secrets. This procedure can be used to conduct reconnaissance and prepare for further attacks.

 

## Requirements

1. Valid AWS credentials with permissions to access AWS Secrets Manager

1. Access to the AWS Management Console or AWS CLI

 

## Defense

1. Limit access to AWS Secrets Manager by using AWS Identity and Access Management (IAM) roles and policies

1. Implement multi-factor authentication (MFA) for AWS accounts and users

1. Monitor AWS CloudTrail logs for suspicious activity

 

## Objectives

1. Discover sensitive information stored in AWS Secrets Manager

1. Conduct reconnaissance to prepare for further attacks

 

# Instructions

1. To describe a secret in AWS Secrets Manager, use the 'aws secretsmanager describe-secret' command followed by the ID of the secret you want to describe.

 

This command returns information about the specified secret, including its ARN, name, description, KMS key ID, and other metadata. You can use this command to verify the existence of a secret, retrieve its metadata, and ensure that it is properly configured. The 'name' parameter in the command should be replaced with the actual name or ARN of the secret you want to describe.



**Command** ([[Describe Secret]]):

```bash
aws secretsmanager describe-secret --secret-id name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]

### Sub-Techniques

- [[Local Account|T1087.001 - Local Account]]

## Commands Used

- [[Describe Secret]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing information about a specific secret]]


