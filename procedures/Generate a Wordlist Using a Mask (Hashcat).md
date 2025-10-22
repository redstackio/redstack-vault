---
id: 79525632-d61c-4cf0-9d37-dfc430f8101f
name: Generate a Wordlist Using a Mask (Hashcat)
type: procedure
verified: false
submitted: false
created_at: '2019-10-18T01:13:23.076721+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
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
- '[[Hashcat Generate a Wordlist Using a Mask]]'
---

# Generate a Wordlist Using a Mask (Hashcat)

## Summary

In some cases, brute forcing must be done on entire keyspaces rather than using dictionaries. Hashcat can generate wordlists for this using mask attacks, using the --stdout option. 

## Description

# Description

In some cases, brute forcing must be done on entire keyspaces rather than using dictionaries. Hashcat can generate wordlists for this using mask attacks, using the `--stdout` option.

# Instructions

For this example, a wordlist will be built with the following format:

- first character is a digit

- second character is a symbol

- third character is a hex character from 0x00 to 0xff

- fourth character is any character

Use the following table to build the rules.txt file.

**Code**: [[l | abcdefghijklmnopqrstuvwxyz
u | ABCDEFGHIJKLMNO]]

The mask is specified when executing the command. Each character is prepended with a ?.

In this example, the mask will be: <digit><special char><hex><lower/upper/digit/special char>

Mask: **?d?s?b?a**

**Command** ([[Hashcat Generate a Wordlist Using a Mask]]):

```bash
hashcat -a 3 --stdout ?d?s?b?a > $OUTPUT.txt
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

- [[Hashcat Generate a Wordlist Using a Mask]]

## Tags

- [[Cryptography]]
- [[password cracking]]
