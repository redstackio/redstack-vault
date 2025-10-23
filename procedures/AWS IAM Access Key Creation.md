---
id: 4b92ef60-ad67-4cff-9e92-fdd7bf241454
name: AWS IAM Access Key Creation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.620245+00:00'
updated_at: '2023-04-10T20:20:01.274949+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Create Account|T1136 - Create Account]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[5. Exploitation Scenario]]'
- '[[Cloud - AWS]]'
- '[[Creating a new access key for another user]]'
- '[[Persistence & Backdooring]]'
commands:
- '[[Create Access Key for IAM User]]'
---

# AWS IAM Access Key Creation

## Summary

The AWS IAM Access Key Creation procedure involves creating a new access key for an existing user in AWS Identity and Access Management (IAM). This technique can be used to maintain persistence and backdoor an AWS environment. By creating an access key for another user, an attacker can maintain acc

## Description

# Description

The AWS IAM Access Key Creation procedure involves creating a new access key for an existing user in AWS Identity and Access Management (IAM). This technique can be used to maintain persistence and backdoor an AWS environment. By creating an access key for another user, an attacker can maintain access to the environment even if their own credentials are revoked. The attacker can then use this access key to perform actions on behalf of the compromised user.

From a technical perspective, this procedure involves using the 'Create IAM Access Key' command in the AWS Management Console or AWS CLI to create a new access key for the target user. The access key consists of an access key ID and a secret access key, which can be used to authenticate API requests to AWS services.

The business value of this procedure is that it allows an attacker to maintain access to an AWS environment even if their own credentials are revoked. This can lead to data theft, data destruction, or other malicious activities.

 

## Requirements

1. Valid AWS IAM credentials with permissions to create IAM access keys

 

## Defense

1. Regularly review and audit IAM access keys for all users

1. Implement multi-factor authentication (MFA) for IAM users

1. Limit the permissions of IAM users to only what is necessary for their job functions

 

## Objectives

1. Maintain persistence in an AWS environment

1. Backdoor an AWS environment

1. Perform actions on behalf of a compromised user

 

# Instructions

1. To create an access key for an IAM user, use the following command:

 

This command creates an access key for the specified IAM user. The access key consists of an access key ID and a secret access key. These keys are used to authenticate programmatic access to AWS services. The access key ID is used to identify the access key, while the secret access key is used to sign requests made with the access key. The `--username` option specifies the name of the IAM user for whom the access key is being created.



**Command** ([[Create Access Key for IAM User]]):

```bash
aws iam create-access-key --username example_username
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Create Account|T1136 - Create Account]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[Create Access Key for IAM User]]

## Tags

- [[5. Exploitation Scenario]]
- [[Cloud - AWS]]
- [[Creating a new access key for another user]]
- [[Persistence & Backdooring]]


