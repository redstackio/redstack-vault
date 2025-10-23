---
id: 0afef758-6950-4090-bd40-5c60b3aa0d10
name: AWS KMS Key Policy Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.212170+00:00'
updated_at: '2023-04-10T20:20:52.653535+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Getting full information about a policy]]'
commands:
- '[[Retrieve KMS Key Policy]]'
---

# AWS KMS Key Policy Enumeration

## Summary

The AWS KMS Key Policy Enumeration procedure involves retrieving the full information about a policy for an AWS KMS key. This information can be used to identify potential weaknesses in the key policy and can aid in the discovery of other AWS resources. An attacker can use this information to gain 

## Description

# Description

The AWS KMS Key Policy Enumeration procedure involves retrieving the full information about a policy for an AWS KMS key. This information can be used to identify potential weaknesses in the key policy and can aid in the discovery of other AWS resources. An attacker can use this information to gain access to sensitive data and resources within the target's AWS environment. To retrieve the policy, the attacker can use the 'Retrieve AWS KMS Key Policy' command.

 

## Requirements

1. Valid AWS credentials with permissions to retrieve the KMS key policy

 

## Defense

1. Ensure that AWS credentials are properly secured and not accessible to unauthorized users

1. Implement least privilege access control to restrict access to sensitive resources

1. Monitor AWS CloudTrail logs for any suspicious activity related to KMS key policy retrieval

 

## Objectives

1. Retrieve the full information about a policy for an AWS KMS key

1. Identify potential weaknesses in the key policy

1. Discover other AWS resources

 

# Instructions

1. To retrieve the policy of an AWS KMS key, use the following command:

 

The `aws kms get-key-policy` command retrieves the policy for the specified KMS key. The `--policy-name` parameter specifies the name of the policy to retrieve, and the `--key-id` parameter specifies the ID of the KMS key whose policy you want to retrieve. The output will be a JSON-formatted string that represents the policy document for the specified key.



**Command** ([[Retrieve KMS Key Policy]]):

```bash
aws kms get-key-policy --policy-name name --key-id ID
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Retrieve KMS Key Policy]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Getting full information about a policy]]


