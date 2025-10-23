---
id: dca3231a-95a9-4ce7-a30b-80ca8b74e9b2
name: Scan Remote Git Repo for Sensitive Information (gitleaks)
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:21.872587+00:00'
updated_at: '2023-05-26T00:44:36.829598+00:00'
commands:
- '[[gitleaks scan remote github repo]]'
---

# Scan Remote Git Repo for Sensitive Information (gitleaks)

**Status**: ✓ Verified

## Summary

Locate API keys, hardcoded passwords, tokens, sensitive information through a github repo URL. gitleaks 

## Description

# Description

Locate API keys, hardcoded passwords, tokens, sensitive information through a github repo URL.

[gitleaks](https://github.com/zricethezav/gitleaks)



##  Instructions

1. Using gitleaks to scan a github repo by URL



**Command** ([[gitleaks scan remote github repo]]):

```bash
gitleaks --repo=https://github.com/zricethezav/gitleaks

```





## Commands Used

- [[gitleaks scan remote github repo]]


