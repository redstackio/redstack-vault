---
id: 3b3c8cd2-df23-4a2e-b5d5-c661889ccc3e
name: convert-hex-dump-to-binary
type: procedure
verified: true
submitted: true
created_at: '2019-11-25T19:19:34.046112+00:00'
updated_at: '2023-05-26T00:42:28.631156+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Data from Information Repositories|T1213 - Data from
    Information Repositories]]
sub_techniques: []
platforms:
  - Linux
tags:
  - convert
commands:
  - '[[commands/xxd-convert-hex-dump-to-binary]]'
tools:
  - '[[tools/xxd]]'
validated: true
---

# Convert Hex Dump to Binary

## Summary

Convert a hex dump (binary data in hexadecimal pairs) back to its original binary format using xxd, commonly needed after extracting encoded data from memory leaks like Heartbleed in CTF challenges.

## Description

Hex dumps represent binary files in readable hex format. This procedure reverses that using xxd's reverse mode, producing a usable file such as an SSH private key. It assumes the input is clean hex without offsets or ASCII.

## Requirements

1. Hex dump saved in a text file
2. xxd utility (part of vim-common on Linux)
3. Write permissions for output file

## Defense

Encrypt sensitive files like private keys and monitor for memory leaks via tools like Valgrind; use updated OpenSSL to prevent Heartbleed-style dumps.

## Objectives

1. Restore binary from hex representation
2. Validate the output file usability
3. Prepare data for further exploitation

## Instructions

### Step 1: Prepare Input File

**Context**: Copy the hex dump (e.g., from Heartbleed output) into a file without line breaks or extra characters.

No command; create $_INPUT with pure hex pairs.

### Step 2: Perform Conversion

**Context**: Use xxd to reverse the hex dump to binary, why: to obtain a functional file like id_rsa from leaked memory.

**Command** ([[commands/xxd-convert-hex-dump-to-binary]]):
```bash
xxd -ps -r $_INPUT > $_OUTPUT
```

> -ps treats input as plain hex stream, -r reverses it. Expected output is a binary file; verify with file $_OUTPUT or openssl rsa -in $_OUTPUT -check if it's a key. If errors, clean input hex.
