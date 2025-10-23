---
id: f42fb955-ccf2-4eed-9ac9-3cb43c6b59ef
name: Enumerate a Git Repository for Secrets
type: procedure
verified: false
submitted: false
created_at: '2019-10-16T22:13:26.212152+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Credentials in Files|T1081 - Credentials in Files]]'
tags:
- '[[data exposure]]'
commands:
- '[[Git List a Git Repository''s Commit History]]'
- '[[Git List a Git Repository''s Commit History for Lost Commits]]'
- '[[Git List a Git Repository''s Commit Messages]]'
---

# Enumerate a Git Repository for Secrets

## Summary

Git repositories often contain sensitive information that the authors unintentionally committed or thought was removed. By enumerating the commit history, it may be possible to identify secrets in commit messages, file content, deleted files, etc. Using the reflog argument  may show lost commits fr

## Description

# Description

Git repositories often contain sensitive information that the authors unintentionally committed or thought was removed. By enumerating the commit history, it may be possible to identify secrets in commit messages, file content, deleted files, etc. Using the `reflog` argument  may show lost commits from instances where a repository was reset to a point prior to than the commits made after it.



# Instructions

Enumerate commit messages for useful information.



**Command** ([[Git List a Git Repository's Commit Messages]]):

```bash
git log --all
```



Enumerate the content of all commits.





**Command** ([[Git List a Git Repository's Commit History]]):

```bash
git log -p
```



Enumerate the content of all commits, including head resets.





**Command** ([[Git List a Git Repository's Commit History for Lost Commits]]):

```bash
git reflog -p
```





## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Credentials in Files|T1081 - Credentials in Files]]

## Commands Used

- [[Git List a Git Repository's Commit History]]
- [[Git List a Git Repository's Commit History for Lost Commits]]
- [[Git List a Git Repository's Commit Messages]]

## Tags

- [[data exposure]]


