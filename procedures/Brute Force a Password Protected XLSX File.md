---
id: 19e10971-3635-49e6-9489-ab65339983cc
name: Brute Force a Password Protected XLSX File
type: procedure
verified: true
submitted: true
created_at: '2020-06-25T21:07:47.268848+00:00'
updated_at: '2023-05-25T19:47:25.482851+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[Brute Force]]'
commands:
- '[[John the Ripper Brute Force a Hash File]]'
- '[[office2john.py Extract a Password Hash from an XLSX File]]'
---

# Brute Force a Password Protected XLSX File

**Status**: ✓ Verified

## Summary

Extract the password hash from a password protected XLSX file, and attempt to brute force it with John the Ripper. 

## Description

# Description

Extract the password hash from a password protected XLSX file, and attempt to brute force it with John the Ripper.



# Instructions

Instructions on how to complete the procedure. Typically multiple numbered lists with commands included, and may contain H2 subheadings.



1. Use John the Ripper's office2john.py script to extract the password hash. On Kali, this script is often located at: /usr/share/john/office2john.py





**Command** ([[office2john.py Extract a Password Hash from an XLSX File]]):

```bash
office2john.py $_TARGET_FILE.xslx
```





2. Use John the Ripper to brute force the hash





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
- [[office2john.py Extract a Password Hash from an XLSX File]]

## Tags

- [[Brute Force]]


