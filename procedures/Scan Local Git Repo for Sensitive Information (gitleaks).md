---
id: 08cda633-3ed1-453a-89d6-e73eeb972321
name: Scan Local Git Repo for Sensitive Information (gitleaks)
type: procedure
verified: false
submitted: false
created_at: '2020-07-24T17:11:33.719130+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
commands:
- '[[gitleaks scan local github repo''s]]'
- '[[gitleaks scan multiple local github repo''s]]'
---

# Scan Local Git Repo for Sensitive Information (gitleaks)

## Summary

Locate API keys, hardcoded passwords, tokens, sensitive information through a github repo. gitleaks 

## Description

# Description

Locate API keys, hardcoded passwords, tokens, sensitive information through a github repo.

[gitleaks](https://github.com/zricethezav/gitleaks)



##  Instructions

1. Using gitleaks to scan a local github repo, Clone the repo locally before running



**Command** ([[gitleaks scan local github repo's]]):

```bash
gitleaks --repo-path=~/git/gitleaks

```





2. (Option) Using gitleaks to scan multiple git repo's within a directory



**Command** ([[gitleaks scan multiple local github repo's]]):

```bash
gitleaks --owner-path=~/git

```





## Commands Used

- [[gitleaks scan local github repo's]]
- [[gitleaks scan multiple local github repo's]]


