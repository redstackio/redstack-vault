---
id: bb6c440e-3dec-48ee-96e5-e58d17fa101c
name: AWS Managed Policies Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:11.648345+00:00'
updated_at: '2023-04-10T20:20:41.361765+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Steal Application Access Token|T1528 - Steal Application Access Token]]'
- '[[Valid Accounts|T1078 - Valid Accounts]]'
tags:
- '[[Checking all managed policies attached to the user]]'
- '[[Cloud - AWS]]'
- '[[Persistence]]'
commands:
- '[[List Attached User Policies]]'
---

# AWS Managed Policies Enumeration

## Summary

The AWS Managed Policies Enumeration procedure involves checking all managed policies attached to a user in order to identify any policies that may grant excessive privileges or allow for persistence in the event of a compromise. This procedure is typically used by attackers who have already gained

## Description

# Description

The AWS Managed Policies Enumeration procedure involves checking all managed policies attached to a user in order to identify any policies that may grant excessive privileges or allow for persistence in the event of a compromise. This procedure is typically used by attackers who have already gained access to an AWS account and are looking to escalate their privileges and maintain persistence.

To enumerate the managed policies attached to a user, the List Attached User Policies command can be used. This command will return a list of all managed policies that are attached to the specified user.

By identifying and exploiting overly permissive managed policies, an attacker can escalate their privileges and maintain persistence in the event that their initial access is detected and removed.

## Requirements

1. Valid AWS credentials with appropriate permissions to list attached user policies

## Defense

1. Ensure that users are only granted the minimum necessary permissions required to perform their job functions

1. Regularly review and audit managed policies to identify any that may be overly permissive

1. Implement MFA and strong password policies to prevent unauthorized access to AWS accounts

## Objectives

1. Identify all managed policies attached to a user

1. Identify any overly permissive managed policies that may grant excessive privileges

1. Maintain persistence in the event of a compromise

# Instructions

1. Use the 'aws iam list-attached-user-policies' command to list all the policies that are attached to a specific IAM user.

This command will return a list of policies that are attached to the specified user. The policies can be either AWS managed policies or customer managed policies. The command takes one argument which is the name of the user whose attached policies you want to list. The output of the command will include the policy name, policy ARN, and the policy type (AWS managed or customer managed).

**Command** ([[List Attached User Policies]]):

```bash
aws iam list-attached-user-policies --user-name user_name
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Steal Application Access Token|T1528 - Steal Application Access Token]]
- [[Valid Accounts|T1078 - Valid Accounts]]

## Commands Used

- [[List Attached User Policies]]

## Tags

- [[Checking all managed policies attached to the user]]
- [[Cloud - AWS]]
- [[Persistence]]
