---
id: 23dbbf31-b7f7-4ed8-b666-dc4747865076
name: Scan Remote Git Repo for Sensitive Information (trufflehog)
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:23.000708+00:00'
updated_at: '2023-05-26T00:46:45.443031+00:00'
commands:
- '[[trufflehog scan a github repo for sensitive info]]'
- '[[trufflehog scan a github repo with entropy disabled]]'
---

# Scan Remote Git Repo for Sensitive Information (trufflehog)

**Status**: ✓ Verified

## Summary

Locate API keys, hardcoded passwords, tokens, sensitive information through a github repo URL. This is the best current tool for scanning github repositories for sensitive information Trufflehog supports include and exclude regex patterns. trufflehog 

## Description

# Description

Locate API keys, hardcoded passwords, tokens, sensitive information through a github repo URL.

This is the best current tool for scanning github repositories for sensitive information

Trufflehog supports include and exclude regex patterns.

[trufflehog](https://github.com/dxa4481/truffleHog)



##  Instructions

1. Using trufflehog to scan a github repo by URL



**Command** ([[trufflehog scan a github repo for sensitive info]]):

```bash
trufflehog https://github.com/dxa4481/truffleHog

```





2. (Option) Use trufflehog with entropy disable



**Command** ([[trufflehog scan a github repo with entropy disabled]]):

```bash
trufflehog --entropy=FALSE https://github.com/dxa4481/truffleHog

```





## Commands Used

- [[trufflehog scan a github repo for sensitive info]]
- [[trufflehog scan a github repo with entropy disabled]]


