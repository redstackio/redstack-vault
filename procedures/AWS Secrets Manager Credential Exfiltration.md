---
id: 363c2716-0a46-437a-a2f9-844b2551eed7
name: AWS Secrets Manager Credential Exfiltration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.356352+00:00'
updated_at: '2023-04-10T20:20:46.403590+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Data Encoding|T1132 - Data Encoding]]'
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
tags:
- '[[Cloud - AWS]]'
- '[[Credential Exfiltration]]'
- '[[Getting the secret value]]'
commands:
- '[[Retrieve Secret from AWS Secrets Manager]]'
---

# AWS Secrets Manager Credential Exfiltration

## Summary

AWS Secrets Manager is a service that enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. An attacker can use the 'Retrieve AWS Secrets Manager Secret Value' command to exfiltrate sensitive information stored in the servic

## Description

# Description

AWS Secrets Manager is a service that enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. An attacker can use the 'Retrieve AWS Secrets Manager Secret Value' command to exfiltrate sensitive information stored in the service. This can be used to gain access to other parts of the system, such as databases or other cloud services. The attacker can use various techniques to exfiltrate the data, such as data encoding or exfiltration over an alternative protocol.

From a technical standpoint, the attacker needs to have access to the AWS account in order to use this command. The secrets manager service should be properly configured with secure access policies and permissions to prevent unauthorized access.

From a business perspective, this attack can lead to sensitive data being exposed and potentially used for malicious purposes, resulting in financial loss, reputational damage, and legal implications.

 

## Requirements

1. Access to the AWS account

1. Properly configured secrets manager service with secure access policies and permissions

 

## Defense

1. Implement secure access policies and permissions for AWS Secrets Manager to prevent unauthorized access

1. Monitor for unusual activity and exfiltration of data from the service

1. Encrypt sensitive data stored in AWS Secrets Manager to prevent unauthorized access

 

## Objectives

1. Exfiltrate sensitive information stored in AWS Secrets Manager

1. Gain access to other parts of the system

 

# Instructions

1. To retrieve the value of a secret from AWS Secrets Manager, use the 'aws secretsmanager get-secret-value' command.

 

Arguments:
--secret-id: The ID of the secret to retrieve the value for. This can be either the Amazon Resource Name (ARN) or the friendly name of the secret.

Example:
aws secretsmanager get-secret-value --secret-id mySecret



**Command** ([[Retrieve Secret from AWS Secrets Manager]]):

```bash
aws secretsmanager get-secret-value --secret-id ID
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Data Encoding|T1132 - Data Encoding]]
- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]

## Commands Used

- [[Retrieve Secret from AWS Secrets Manager]]

## Tags

- [[Cloud - AWS]]
- [[Credential Exfiltration]]
- [[Getting the secret value]]


