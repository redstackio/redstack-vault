---
id: 84be455c-dc7b-417c-98a9-04e24f38673d
name: AWS IAM list Users
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:31.087577+00:00'
updated_at: '2023-05-25T20:07:05.535052+00:00'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws iam list groups]]'
- '[[aws iam list users]]'
- '[[aws list users in group]]'
---

# AWS IAM list Users

**Status**: ✓ Verified

## Summary

All of the IAM enumeration commands are in this one procedure, instead of individual procedures for each command. Use the one command you need, or drink all the beer and enumerate all the things. 

## Description

# Description

All of the IAM enumeration commands are in this one procedure, instead of individual procedures for each command. Use the one command you need,

or drink all the beer and enumerate all the things.

##  Instructions

1. List all of the IAM Users



**Command** ([[aws iam list users]]):

```bash
aws iam list-users

```





2. (Optional) List all of the groups



**Command** ([[aws iam list groups]]):

```bash
aws iam list-groups

```





3. (Optional) List all of the users in a group



**Command** ([[aws list users in group]]):

```bash
aws iam get-group --group-name $AWS_IAM_GROUP

```







## Platforms

- Cloud

## Commands Used

- [[aws iam list groups]]
- [[aws iam list users]]
- [[aws list users in group]]

## Tags

- [[AWS]]
- [[Cloud]]


