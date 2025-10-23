---
id: 5c8d86c0-ea1c-4310-8431-09b9368d6e7f
name: Brute Force a Password Hash using John the Ripper
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T19:50:41.387618+00:00'
updated_at: '2023-05-26T00:45:01.187768+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[Cryptography]]'
commands:
- '[[John the Ripper Brute Force a Hash File]]'
---

# Brute Force a Password Hash using John the Ripper

**Status**: ✓ Verified

## Summary

Use John the Ripper to brute force a password hash. When not specifying the type of hash, John will attempt to guess the correct type. 

## Description

# Description

Use John the Ripper to brute force a password hash. When not specifying the type of hash, John will attempt to guess the correct type.



# Instructions





**Command** ([[John the Ripper Brute Force a Hash File]]):

```bash
john --wordlist=$_WORDLIST $_HASH_FILE
```





## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[John the Ripper Brute Force a Hash File]]

## Tags

- [[Cryptography]]


