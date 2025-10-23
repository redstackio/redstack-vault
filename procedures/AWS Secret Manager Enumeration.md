---
id: 74916d14-b703-440b-a551-ee716a2350b6
name: AWS Secret Manager Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.081307+00:00'
updated_at: '2023-04-10T20:20:52.309272+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing all secrets stored by Secret Manager]]'
commands:
- '[[List AWS Secrets]]'
---

# AWS Secret Manager Enumeration

## Summary

The AWS Secret Manager is a service that enables you to store and manage secrets, such as database credentials, API keys, and other sensitive data. An attacker can use the 'List AWS Secrets' command to enumerate all the secrets stored in an AWS account. By doing so, the attacker can gain valuable i

## Description

# Description

The AWS Secret Manager is a service that enables you to store and manage secrets, such as database credentials, API keys, and other sensitive data. An attacker can use the 'List AWS Secrets' command to enumerate all the secrets stored in an AWS account. By doing so, the attacker can gain valuable information that can be used to further compromise the account.

To use this command, the attacker needs to have valid AWS credentials that have the necessary permissions to access the Secret Manager API. Once the attacker has enumerated the secrets, they can use them to gain access to other resources in the AWS account.

This procedure can be used as part of a larger attack chain, such as lateral movement or data exfiltration.

 

## Requirements

1. Valid AWS credentials with permissions to access the Secret Manager API

1. Access to the internet to communicate with the AWS API

 

## Defense

1. Implement the principle of least privilege by granting AWS credentials with the minimum necessary permissions to access the Secret Manager API

1. Enable AWS CloudTrail to log all API calls to the Secret Manager and monitor the logs for suspicious activity

1. Regularly rotate secrets stored in the Secret Manager to mitigate the impact of a potential compromise

 

## Objectives

1. Enumerate all secrets stored in an AWS account

1. Gain access to sensitive data stored in the Secret Manager

1. Use the secrets to further compromise the AWS account

 

# Instructions

1. Use this command to list all the secrets in your AWS Secrets Manager.

 



**Code**: [[aws secretsmanager list-secrets]]



> The `aws secretsmanager list-secrets` command returns a JSON object containing information about all the secrets in your AWS Secrets Manager. This information includes the secret name, ARN, description, and the date and time the secret was created or last modified. You can use this command to quickly view all the secrets in your account, and use the information to manage and update your secrets as needed.



**Command** ([[List AWS Secrets]]):

```bash
aws secretsmanager list-secrets
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List AWS Secrets]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing all secrets stored by Secret Manager]]


