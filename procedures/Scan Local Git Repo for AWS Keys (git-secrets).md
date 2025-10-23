---
id: a60c0a4e-d04e-42c8-88d7-89bc9e2d8c30
name: Scan Local Git Repo for AWS Keys (git-secrets)
type: procedure
verified: false
submitted: false
created_at: '2020-07-24T17:11:24.561173+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
commands:
- '[[git-secrets scan the current directory for secrets]]'
---

# Scan Local Git Repo for AWS Keys (git-secrets)

## Summary

Scan a github repository for AWS credentials such as API keys, Passwords. This tool works with a logal cloned git repo, so clone the target repo first. git-secrets 

## Description

# Description

Scan a github repository for AWS credentials such as API keys, Passwords.

This tool works with a logal cloned git repo, so clone the target repo first.

[git-secrets](https://github.com/awslabs/git-secrets)



##  Instructions

1. Using git-secrets from inside a git repo directory (any directory containing a .git folder)



**Command** ([[git-secrets scan the current directory for secrets]]):

```bash
git-secrets --scan

```





## Commands Used

- [[git-secrets scan the current directory for secrets]]


