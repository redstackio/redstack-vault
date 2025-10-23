---
id: b96dd824-adba-416d-a697-4820a5f1c209
name: AWS Secrets Manager Resource-Based Policy Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.331643+00:00'
updated_at: '2023-04-10T20:20:33.800407+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Unsecured Credentials|T1552 - Unsecured Credentials]]'
tags:
- '[[Cloud - AWS]]'
- '[[Credential Exfiltration]]'
- '[[Getting resource-based policy attached to an specific secret]]'
commands:
- '[[Retrieve Resource Policy for AWS Secrets Manager Secret]]'
---

# AWS Secrets Manager Resource-Based Policy Exfiltration

## Summary

AWS Secrets Manager is a service that helps you protect access to your applications, services, and IT resources. A resource-based policy is an AWS Identity and Access Management (IAM) policy that you can attach to a secret to define who can access the secret and what actions they can perform. An at

## Description

# Description

AWS Secrets Manager is a service that helps you protect access to your applications, services, and IT resources. A resource-based policy is an AWS Identity and Access Management (IAM) policy that you can attach to a secret to define who can access the secret and what actions they can perform. An attacker with access to the AWS console or API can use the 'Get Secrets Manager Resource Policy' command to retrieve the resource-based policy attached to a specific secret. This can allow the attacker to exfiltrate sensitive credentials and gain access to additional resources within the AWS environment.

 

## Requirements

1. Access to the AWS console or API

1. Permissions to retrieve the resource-based policy for a specific secret

 

## Defense

1. Ensure that access to the AWS console and API is restricted to authorized personnel only

1. Enable multi-factor authentication (MFA) for all AWS accounts

1. Regularly review and audit resource-based policies attached to secrets for unauthorized changes or access

 

## Objectives

1. Retrieve the resource-based policy attached to a specific secret

1. Exfiltrate sensitive credentials

1. Gain access to additional resources within the AWS environment

 

# Instructions

1. To get the resource-based policy for a secret in AWS Secrets Manager, use the get-resource-policy command. Replace 'ID' with the ID of the secret you want to retrieve the policy for.

 

The get-resource-policy command retrieves the resource-based policy for a secret in AWS Secrets Manager. This policy determines who has access to the secret and what actions they can perform on it. The '--secret-id' flag is used to specify the ID of the secret you want to retrieve the policy for. This command can be useful for auditing and troubleshooting purposes, as well as for ensuring that the correct permissions are set for your secrets.



**Command** ([[Retrieve Resource Policy for AWS Secrets Manager Secret]]):

```bash
aws secretsmanager get-resource-policy --secret-id ID
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Unsecured Credentials|T1552 - Unsecured Credentials]]

## Commands Used

- [[Retrieve Resource Policy for AWS Secrets Manager Secret]]

## Tags

- [[Cloud - AWS]]
- [[Credential Exfiltration]]
- [[Getting resource-based policy attached to an specific secret]]


