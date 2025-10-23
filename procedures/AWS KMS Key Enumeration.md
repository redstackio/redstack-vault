---
id: e8b3652e-e824-4dcf-a68d-fd38be0b097a
name: AWS KMS Key Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.146895+00:00'
updated_at: '2023-04-10T20:19:49.153467+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing keys in KMS]]'
---

# AWS KMS Key Enumeration

## Summary

The AWS Key Management Service (KMS) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data. This procedure allows an attacker to enumerate and list the keys in KMS. This can be useful for discovering sensitive data that is being encrypte

## Description

# Description

The AWS Key Management Service (KMS) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data. This procedure allows an attacker to enumerate and list the keys in KMS. This can be useful for discovering sensitive data that is being encrypted with KMS. The attacker can then use these keys to decrypt the data and exfiltrate it.

Technical Explanation: The attacker can use the AWS CLI to list the keys in KMS. This can be done by running the 'aws kms list-keys' command. The output will contain information about each key, such as the key ID and the date it was created.

Business Value: An attacker can use this procedure to gain access to sensitive data that is being encrypted with KMS. This data can then be used for financial gain or to gain a competitive advantage.

 

## Requirements

1. Valid AWS credentials with permissions to access KMS

1. Access to the AWS CLI

 

## Defense

1. Implement proper access controls and permissions for AWS credentials

1. Monitor AWS API calls for unusual activity

1. Encrypt sensitive data at rest and in transit

 

## Objectives

1. Enumerate and list the keys in KMS

1. Discover sensitive data that is being encrypted with KMS

 

# Instructions

1. Use this command to list all AWS KMS keys in your account.

 



**Code**: [[aws kms list-keys]]



> This command takes no arguments and returns a JSON object containing information about all the KMS keys in your account. The output includes the key ID, creation date, and description of each key.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing keys in KMS]]


