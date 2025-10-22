---
id: e728cf9c-0519-4db3-8d3a-2a9826e8aef3
name: AWS IAM List Policy
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:25.205869+00:00'
updated_at: '2023-05-25T20:04:58.068743+00:00'
platforms:
- Cloud
tags:
- '[[AWS]]'
- '[[Cloud]]'
commands:
- '[[aws describe iam policy]]'
- '[[aws iam list policies]]'
---

# AWS IAM List Policy

**Status**: ✓ Verified

## Summary

List all of the IAM policies under an AWS account 

## Description

# Description

List all of the IAM policies under an AWS account

##  Instructions

1. List all of the IAM Policies

**Command** ([[aws iam list policies]]):

```bash
aws iam list-policies

```

2. (Optional) Describe an IAM policy

**Command** ([[aws describe iam policy]]):

```bash
aws iam get-policy --policy-arn arn:aws:iam::aws:policy/$AWS_IAM_POLICY

```

## Platforms

- Cloud

## Commands Used

- [[aws describe iam policy]]
- [[aws iam list policies]]

## Tags

- [[AWS]]
- [[Cloud]]
