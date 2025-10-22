---
id: 90f10c29-a639-43a5-8768-cfab3b41324f
name: Fuzzing Sub-Domains (wfuzz)
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:40.389777+00:00'
updated_at: '2023-05-26T18:52:49.108344+00:00'
commands:
- '[[wfuzz fuzz a single url]]'
---

# Fuzzing Sub-Domains (wfuzz)

**Status**: ✓ Verified

## Summary

Finding Sub-Domains using the wfuzz tool. This can come in handy if your choices are limited on what tools you have available at the time. 

## Description

# Description

Finding Sub-Domains using the wfuzz tool. This can come in handy if your choices are limited on what tools you have available at the time.

##  Instructions

1. Using wfuzz to fuzz a single URL

**Command** ([[wfuzz fuzz a single url]]):

```bash
wfuzz -c -f re -w /SecLists/Discovery/DNS/subdomains-top1mil-5000.txt -u "http://domain.htb" -H "Host: FUZZ.domain.htb" --hh 311\

```

## Commands Used

- [[wfuzz fuzz a single url]]
