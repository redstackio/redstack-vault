---
id: 9d4daff2-4a8f-4354-b022-99ecbe54e898
name: AWS KMS Key Listing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:12.166856+00:00'
updated_at: '2023-04-10T20:20:56.531058+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
tags:
- '[[Cloud - AWS]]'
- '[[Enumeration]]'
- '[[Listing information about a specific key]]'
commands:
- '[[Describe KMS Key]]'
---

# AWS KMS Key Listing

## Summary

The AWS KMS Key Listing procedure involves using the AWS KMS Describe Key command to list information about a specific key. This can be useful for an attacker to gather information about the key and its usage, such as the key state, creation date, and key policy. From this information, an attacker 

## Description

# Description

The AWS KMS Key Listing procedure involves using the AWS KMS Describe Key command to list information about a specific key. This can be useful for an attacker to gather information about the key and its usage, such as the key state, creation date, and key policy. From this information, an attacker may be able to determine if the key is being used for sensitive data and plan further attacks.

To execute this procedure, the attacker would need access to the AWS CLI and appropriate permissions to use the AWS KMS Describe Key command.

The business value of this procedure is that it can help identify potential security weaknesses in an organization's cloud infrastructure and allow for proactive mitigation.

 

## Requirements

1. Access to the AWS CLI

1. Appropriate permissions to use the AWS KMS Describe Key command

 

## Defense

1. Ensure that appropriate access controls are in place for AWS KMS keys

1. Monitor AWS CloudTrail logs for suspicious activity related to KMS keys

1. Regularly review and update AWS KMS key policies to ensure they align with security best practices

 

## Objectives

1. List information about a specific AWS KMS key

1. Determine the key state, creation date, and key policy

1. Identify potential security weaknesses in an organization's cloud infrastructure

 

# Instructions

1. To describe a customer master key (CMK), use the describe-key command. This command returns detailed information about the specified CMK, including its Amazon Resource Name (ARN), key state, creation date, description, and key usage.

 

The --key-id option specifies the ID or Amazon Resource Name (ARN) of the CMK. This is a required parameter. The command returns information about the specified CMK. If the specified CMK does not exist, the command returns an error. The output includes the following information about the specified CMK: 

- KeyId: The globally unique identifier for the CMK.
- Description: The description of the CMK.
- KeyManager: The Amazon Web Services account ID of the key manager for the CMK.
- KeyState: The state of the CMK (Enabled, Disabled, PendingDeletion, PendingImport, or Unavailable).
- CreationDate: The date and time when the CMK was created.
- CustomerMasterKeySpec: The type of key material in the CMK (either SYMMETRIC_DEFAULT or RSA_2048).
- Origin: The source of the CMK's key material (either AWS_KMS or EXTERNAL).
- KeyUsage: The intended use of the CMK (either ENCRYPT_DECRYPT or SIGN_VERIFY).
- Arn: The Amazon Resource Name (ARN) of the CMK.
- Enabled: Indicates whether the CMK is enabled.



**Command** ([[Describe KMS Key]]):

```bash
aws kms describe-key --key-id ID
```



## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]
- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Data from Cloud Storage|T1530 - Data from Cloud Storage]]
- [[Steal Application Access Token|T1528 - Steal Application Access Token]]

## Commands Used

- [[Describe KMS Key]]

## Tags

- [[Cloud - AWS]]
- [[Enumeration]]
- [[Listing information about a specific key]]


