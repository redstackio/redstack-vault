---
id: bab343fb-82fd-462e-b000-ac5d8a4c47d7
name: AWS IAM User Group Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:10.039225+00:00'
updated_at: '2023-04-10T20:20:04.102679+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
tags:
- '[[1. Enumerating IAM users]]'
- '[[Cloud - AWS]]'
- '[[Listing the IAM groups that the specified IAM user belongs to]]'
commands:
- '[[List IAM Groups for User]]'
---

# AWS IAM User Group Enumeration

## Summary

AWS IAM User Group Enumeration is an account discovery technique that allows an attacker to list the IAM groups that a specified IAM user belongs to. This information can be used to identify potential targets for privilege escalation or lateral movement within an AWS environment. The attacker can u

## Description

# Description

AWS IAM User Group Enumeration is an account discovery technique that allows an attacker to list the IAM groups that a specified IAM user belongs to. This information can be used to identify potential targets for privilege escalation or lateral movement within an AWS environment. The attacker can use the 'List Groups for User' command to retrieve a list of IAM groups that the specified IAM user belongs to. The command can be executed via the AWS CLI or SDKs.

 

## Requirements

1. Valid AWS access key and secret access key

1. Permissions to execute the 'List Groups for User' command

 

## Defense

1. Ensure that IAM users have the minimum level of permissions necessary to perform their job duties

1. Implement multi-factor authentication for AWS accounts

1. Monitor AWS CloudTrail logs for suspicious activity related to IAM user and group management

 

## Objectives

1. Identify potential targets for privilege escalation within an AWS environment

1. Discover potential targets for lateral movement within an AWS environment

 

# Instructions

1. To list the groups that a specified IAM user belongs to, use the following command:

 

- Replace 'user-name' with the name of the IAM user you want to list the groups for.
- This command will return a list of groups that the specified user belongs to, including the group name and group ID.
- If the user does not belong to any groups, the command will return an empty list.
- Note that you must have the necessary permissions to list the groups for a user.



**Command** ([[List IAM Groups for User]]):

```bash
aws iam list-groups-for-user --user-name user-name
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]

## Commands Used

- [[List IAM Groups for User]]

## Tags

- [[1. Enumerating IAM users]]
- [[Cloud - AWS]]
- [[Listing the IAM groups that the specified IAM user belongs to]]


