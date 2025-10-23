---
id: 39f5c20b-f3b1-4390-b984-efd051b667be
name: Identify a Password Hash (Hashcat)
type: procedure
verified: true
submitted: true
created_at: '2020-03-14T02:00:51.380679+00:00'
updated_at: '2023-05-25T19:45:09.356398+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[Cryptography]]'
- '[[password cracking]]'
---

# Identify a Password Hash (Hashcat)

**Status**: ✓ Verified

## Summary

Analyze a password hash to identify the type and Hashcat mode. 

## Description

# Description

Analyze a password hash to identify the type and Hashcat mode.





## Objectives

Analyzing the format of the hash, and then using tools or techniques to identify the specific hash type, such as NTLMv1, NTLMv2, or other types of hashes.



1. Identify the type of hash



# Instructions

Use Hashcat's Example Hashes web page as a reference to identify the Hash Name and Hash Mode values: [Example Hashes](https://hashcat.net/wiki/doku.php?id=example_hashes)



Considerations:

- id - Many hashes are prefixed with an identifier string, which is terminated by a "$". Searching Example Hashes for this string will often find the exact hash

- length - If no id is present, look for samples from Example Hashes which match the target hash's length. Eg: a 32 char hash with no id may be MD5

Example:





**Code**: [[$axcrypt_sha1$b89eaac7e61417341b710b727768294d0e6a]]



In this case, the identifier is "axcrypt_sha1". Search Example Hashes for: "$axcrypt_sha1$" to find this is AxCrypt, Hash Mode 13300.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Tags

- [[Cryptography]]
- [[password cracking]]


