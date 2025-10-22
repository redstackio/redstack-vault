---
id: 2d099d09-8672-475c-844f-e817f7b5ed82
name: Extract a Hidden File In an Image Using Steghide
type: procedure
verified: false
submitted: false
created_at: '2019-10-10T00:34:20.445224+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
techniques:
- '[[Data Obfuscation|T1001 - Data Obfuscation]]'
tags:
- '[[Cryptography]]'
- '[[data encryption]]'
commands:
- '[[Steghide Extract a Hidden File in an Image]]'
---

# Extract a Hidden File In an Image Using Steghide

## Summary

Extract a file hidden in an image (or audio file) using Steghide's steganography tools. 

## Description

# Description

Extract a file hidden in an image (or audio file) using Steghide's steganography tools.

# Requirements

- cover file which has another file embedded in it

# Instructions

In order to extract a file that has been embedded in another using Steghide, the correct password must be issued. For this example, a generic wallpaper has an SSH public key embedded, with the password '**secret**'.

**Command** ([[Steghide Extract a Hidden File in an Image]]):

```bash
steghide extract -sf $_COVER
```

After running the extract command with the password '**secret**', a SSH key is extracted to the current working directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]

### Techniques

- [[Data Obfuscation|T1001 - Data Obfuscation]]

## Commands Used

- [[Steghide Extract a Hidden File in an Image]]

## Tags

- [[Cryptography]]
- [[data encryption]]
