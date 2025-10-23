---
id: 2eb27abd-568b-4c19-bab0-c77d94b50be9
name: AWS IAM List Access Keys
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:29.013247+00:00'
updated_at: '2023-05-25T20:04:30.747758+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws iam list access keys]]'
- '[[aws list access key ID''s for IAM user]]'
- '[[aws list ssh public keys for user]]'
---

# AWS IAM List Access Keys

**Status**: ✓ Verified

## Summary

List all of the IAM access keys 

## Description

# Description

List all of the IAM access keys

##  Instructions

1. List all of the access keys



**Command** ([[aws iam list access keys]]):

```bash
aws iam list-access-keys

```





2. (Optional) List the Access Key IDs for an IAM User



**Command** ([[aws list access key ID's for IAM user]]):

```bash
aws iam list-access-keys --user-name $AWS_IAM_USER

```







3. (Optional) List all of the public SSH keys for a user



**Command** ([[aws list ssh public keys for user]]):

```bash
aws iam list-ssh-public-keys --user-name $AWS_IAM_USER

```





## Platforms

- Cloud

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]

## Commands Used

- [[aws iam list access keys]]
- [[aws list access key ID's for IAM user]]
- [[aws list ssh public keys for user]]

## Tags

- [[AWS]]
- [[Cloud]]


