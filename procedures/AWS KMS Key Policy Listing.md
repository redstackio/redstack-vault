---
id: 4e0888a1-d07a-48c2-8c83-daf0f0c2399e
name: AWS KMS Key Policy Listing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.407472+00:00'
updated_at: '2023-04-10T20:20:53.005219+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Credential Exfiltration]]'
- '[[KMS]]'
- '[[Listing policies attached to an specified key]]'
commands:
- '[[List Key Policies]]'
---

# AWS KMS Key Policy Listing

## Summary

The AWS Key Management Service (KMS) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data. This procedure allows an attacker to list the policies attached to a specified key, which can reveal information about who has access to the key 

## Description

# Description

The AWS Key Management Service (KMS) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data. This procedure allows an attacker to list the policies attached to a specified key, which can reveal information about who has access to the key and what they can do with it. 

To list the policies attached to a key, the attacker can use the 'List Key Policies' command. This will return a list of policies that are attached to the specified key. 

The business value of this attack is that it can help an attacker to gain access to sensitive data that is encrypted with the key. 

## Requirements

1. Valid AWS credentials with permissions to list KMS key policies

1. Access to the AWS console or CLI

## Defense

1. Ensure that AWS credentials are stored securely and not easily accessible to attackers

1. Implement strict access controls to limit the number of users who have permissions to list KMS key policies

1. Regularly monitor AWS KMS activity logs for suspicious activity

## Objectives

1. List the policies attached to a specified AWS KMS key

1. Identify who has access to the specified key and what they can do with it

# Instructions

1. Use the AWS KMS CLI command 'list-key-policies' to list the key policies for a specified customer master key (CMK).

The 'list-key-policies' command is used to display the key policies associated with a specific CMK. The command takes one argument, '--key-id', which specifies the ID of the CMK for which you want to list the policies. The output of the command is a list of the policies associated with the specified CMK. Each policy is identified by its name, which is a string value. The policies themselves are JSON documents that define the permissions and restrictions for the specified key. These policies can be modified using the 'put-key-policy' command.

**Command** ([[List Key Policies]]):

```bash
aws kms list-key-policies --key-id ID
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[List Key Policies]]

## Tags

- [[Cloud - AWS]]
- [[Credential Exfiltration]]
- [[KMS]]
- [[Listing policies attached to an specified key]]
