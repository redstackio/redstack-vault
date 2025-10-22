---
id: 12b10285-290c-411e-b284-650c8cbd5a33
name: Brute Force Password Hashes (Hashcat)
type: procedure
verified: true
submitted: true
created_at: '2020-03-17T04:34:06.715518+00:00'
updated_at: '2023-05-25T19:59:26.357810+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
platforms:
- Linux
- Windows
tags:
- '[[Cryptography]]'
- '[[password cracking]]'
commands:
- '[[hashcat Brute Force Password Hashes]]'
---

# Brute Force Password Hashes (Hashcat)

**Status**: ✓ Verified

## Summary

Use Hashcat to brute force hashes with a dictionary. See Example Hashes for help identifying the mode. 

## Description

# Description

Use Hashcat to brute force hashes with a dictionary. See [Example Hashes](https://hashcat.net/wiki/doku.php?id=example_hashes) for help identifying the mode.

## Objectives

Brute force attacks can be used in various stages of an attack, including initial access, privilege escalation, and lateral movement. They can also be used to bypass authentication controls and defenses, and gain access to systems and networks.

1. Crack the Hash and obtain the Password

# Instructions

Using the appropriate mode from Example Hashes and a wordlist to brute force the

**Command** ([[hashcat Brute Force Password Hashes]]):

```bash
hashcat -m $_VALUE $_HASHES $_WORDLIST
```

## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[hashcat Brute Force Password Hashes]]

## Tags

- [[Cryptography]]
- [[password cracking]]
