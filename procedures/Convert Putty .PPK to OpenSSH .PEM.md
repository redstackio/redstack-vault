---
id: 71aa2020-8484-4c71-8c42-4700e8de4e15
name: Convert Putty .PPK to OpenSSH .PEM
type: procedure
verified: true
submitted: true
created_at: '2019-12-15T23:15:10.053350+00:00'
updated_at: '2023-05-26T00:45:29.975990+00:00'
platforms:
- Linux
tags:
- '[[convert]]'
- '[[Cryptography]]'
commands:
- '[[puttygen Convert .PPK to .PEM]]'
---

# Convert Putty .PPK to OpenSSH .PEM

**Status**: ✓ Verified

## Summary

Windows users often use Putty as their SSH client, which stores private keys in .PPK format.  While .PPK files are not natively supported in OpenSSH, they can be converted to OpenSSH's .PEM format using Putty's tools. 

## Description

# Description

Windows users often use Putty as their SSH client, which stores private keys in .PPK format.  While .PPK files are not natively supported in OpenSSH, they can be converted to OpenSSH's .PEM format using Putty's tools.

# Instructions

Install putty-tools from any popular package manager. Eg:

**Code**: [[apt update && apt install putty-tools -y]]

**Command** ([[puttygen Convert .PPK to .PEM]]):

```bash
puttygen $_KEY.ppk -O private-openssh -o $_KEY.pem
```

## Platforms

- Linux

## Commands Used

- [[puttygen Convert .PPK to .PEM]]

## Tags

- [[convert]]
- [[Cryptography]]
