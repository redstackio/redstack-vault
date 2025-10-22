---
id: c8925148-b740-4765-bfd1-9975a1921c76
name: AWS Secret Manager Listing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.282586+00:00'
updated_at: '2023-04-10T20:19:57.596485+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Private Keys|T1552.004 - Private Keys]]'
tags:
- '[[Cloud - AWS]]'
- '[[Credential Exfiltration]]'
- '[[Listing all secrets stored by Secret Manager]]'
commands:
- '[[List Secrets in AWS Secrets Manager]]'
---

# AWS Secret Manager Listing

## Summary

The AWS Secret Manager Listing procedure involves accessing the AWS Secret Manager to view all secrets stored within. This can be useful for an attacker looking to exfiltrate credentials and other sensitive information. To perform this procedure, the attacker must have valid AWS credentials and acc

## Description

# Description

The AWS Secret Manager Listing procedure involves accessing the AWS Secret Manager to view all secrets stored within. This can be useful for an attacker looking to exfiltrate credentials and other sensitive information. To perform this procedure, the attacker must have valid AWS credentials and access to the Secret Manager service. 

When an AWS account is compromised, an attacker can use this procedure to gain access to sensitive information such as passwords, API keys, and other secrets. This information can then be used to further compromise the account or to gain access to other systems and data.

From a business perspective, this procedure highlights the importance of securing AWS credentials and access to services. Proper access controls and monitoring can help prevent unauthorized access to sensitive information.

## Requirements

1. Valid AWS credentials

1. Access to the AWS Secret Manager service

## Defense

1. Implement least privilege access controls for AWS credentials and services

1. Enable logging and monitoring for AWS services and credentials

1. Regularly rotate and revoke AWS credentials

## Objectives

1. Access the AWS Secret Manager

1. View all secrets stored within the Secret Manager

# Instructions

1. To list all the secrets available in AWS Secrets Manager, run the following command:

- The 'aws secretsmanager list-secrets' command lists all the secrets available in the Secrets Manager.
- This command does not require any arguments or options.

**Command** ([[List Secrets in AWS Secrets Manager]]):

```bash
aws secretsmanager list-secrets
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Private Keys|T1552.004 - Private Keys]]

## Commands Used

- [[List Secrets in AWS Secrets Manager]]

## Tags

- [[Cloud - AWS]]
- [[Credential Exfiltration]]
- [[Listing all secrets stored by Secret Manager]]
