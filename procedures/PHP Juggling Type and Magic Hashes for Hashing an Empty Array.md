---
id: 418f4c26-f22f-4506-af46-018857482c6f
name: PHP Juggling Type and Magic Hashes for Hashing an Empty Array
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.678011+00:00'
updated_at: '2023-04-06T03:56:40.691946+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Standard Cryptographic Protocol|T1032 - Standard Cryptographic Protocol]]'
tags:
- '[[NULL statements]]'
- '[[PHP Juggling type and magic hashes]]'
- '[[Type Juggling]]'
commands:
- '[[Hashing an empty array with sha1 and md5]]'
---

# PHP Juggling Type and Magic Hashes for Hashing an Empty Array

## Summary

PHP Juggling Type and Magic Hashes for Hashing an Empty Array is a technique used by attackers to bypass authentication mechanisms that rely on comparing two values. Type juggling is a PHP feature that allows for the automatic conversion of a value from one data type to another. By using this featu

## Description

# Description

PHP Juggling Type and Magic Hashes for Hashing an Empty Array is a technique used by attackers to bypass authentication mechanisms that rely on comparing two values. Type juggling is a PHP feature that allows for the automatic conversion of a value from one data type to another. By using this feature, an attacker can provide a specially crafted input that is interpreted as a different value than what was intended. In this case, the attacker can provide an empty array that is interpreted as a null value, which can bypass authentication mechanisms that check for a non-null value. The attacker can then use a magic hash to authenticate without knowing the actual password.

This technique requires knowledge of the target system and the authentication mechanism used. It can be used to gain unauthorized access to sensitive information or systems.

Business value: By understanding and mitigating this technique, organizations can better protect their authentication mechanisms and prevent unauthorized access to sensitive information or systems.

## Requirements

1. Access to the target system

1. Knowledge of the authentication mechanism used

## Defense

1. Use a strong and unique password for all accounts

1. Implement multi-factor authentication to prevent unauthorized access

1. Regularly monitor and analyze authentication logs for suspicious activity

## Objectives

1. Bypass authentication mechanisms that rely on comparing two values

1. Gain unauthorized access to sensitive information or systems

# Instructions

1. The 'sha1' and 'md5' functions are used to generate a hash value of the input data. In this case, we are trying to hash an empty array. However, since the input is empty, both functions return NULL.

**Code**: [[var_dump(sha1([])); # NULL
var_dump(md5([]));  # N]]

> The 'sha1' function generates a 40-character hexadecimal hash while the 'md5' function generates a 32-character hexadecimal hash. Both functions can accept a string or a binary data as input. It is important to note that hashing is a one-way process and the original data cannot be retrieved from the hash value.

**Command** ([[Hashing an empty array with sha1 and md5]]):

```bash
var_dump(sha1([])); # NULL
var_dump(md5([]));  # NULL
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Standard Cryptographic Protocol|T1032 - Standard Cryptographic Protocol]]

## Commands Used

- [[Hashing an empty array with sha1 and md5]]

## Tags

- [[NULL statements]]
- [[PHP Juggling type and magic hashes]]
- [[Type Juggling]]
