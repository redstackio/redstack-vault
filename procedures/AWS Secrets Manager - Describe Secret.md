---
id: 66cb512c-2707-4555-9813-008dbbb3d1d2
name: AWS Secrets Manager - Describe Secret
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.308419+00:00'
updated_at: '2023-04-10T20:20:06.667209+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
- '[[Credentials In Files|T1552.001 - Credentials In Files]]'
- '[[Credentials in Registry|T1552.002 - Credentials in Registry]]'
tags:
- '[[Cloud - AWS]]'
- '[[Credential Exfiltration]]'
- '[[Listing information about a specific secret]]'
commands:
- '[[Describe AWS Secrets Manager Secret]]'
---

# AWS Secrets Manager - Describe Secret

## Summary

The AWS Secrets Manager Describe Secret command is used to list information about a specific secret stored in AWS Secrets Manager. This command can be used by an attacker to retrieve sensitive information such as usernames, passwords, and API keys. The attacker can then use this information to gain

## Description

# Description

The AWS Secrets Manager Describe Secret command is used to list information about a specific secret stored in AWS Secrets Manager. This command can be used by an attacker to retrieve sensitive information such as usernames, passwords, and API keys. The attacker can then use this information to gain access to other systems and resources within the target's environment.

From a technical perspective, this command sends a request to the AWS Secrets Manager API to retrieve the specified secret. The response includes the secret's metadata, such as its name, ARN, and creation date, as well as the secret's value, which is the sensitive information stored in the secret.

The business value of this attack is significant, as an attacker can gain access to sensitive information that can lead to further compromise of the target's environment. This can result in data theft, financial loss, and reputational damage to the target organization.

 

## Requirements

1. Valid AWS credentials with permissions to access Secrets Manager

 

## Defense

1. Ensure that AWS credentials are properly secured and not accessible to unauthorized users

1. Implement access controls to limit access to Secrets Manager to only authorized users and applications

1. Monitor Secrets Manager for suspicious activity, such as unusual requests or changes to secrets

 

## Objectives

1. Retrieve sensitive information such as usernames, passwords, and API keys

1. Gain access to other systems and resources within the target's environment

 

# Instructions

1. To describe a specific secret in AWS Secrets Manager, use the describe-secret command with the --secret-id parameter followed by the name of the secret.

 

The describe-secret command is used to retrieve the details of a specific secret in AWS Secrets Manager. The --secret-id parameter is used to specify the name of the secret to be described. This command can be useful for retrieving information such as the ARN, description, and tags associated with a secret. Additionally, the command can be used to retrieve the current version and staging labels of the secret.



**Command** ([[Describe AWS Secrets Manager Secret]]):

```bash
aws secretsmanager describe-secret --secret-id name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

### Sub-Techniques

- [[Credentials In Files|T1552.001 - Credentials In Files]]
- [[Credentials in Registry|T1552.002 - Credentials in Registry]]

## Commands Used

- [[Describe AWS Secrets Manager Secret]]

## Tags

- [[Cloud - AWS]]
- [[Credential Exfiltration]]
- [[Listing information about a specific secret]]


