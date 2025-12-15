---
id: cmd-uuid-5
data: >-
  wfuzz --hc=400 -z file,wordlists/params.txt
  https://hackyholidays.h1ctf.com/swag-shop/api/user?FUZZ=1
tags:
  - fuzzing
type: command
output: Discovered uuid.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.480Z'
verified: false
validated: true
submitted: true
---
# Wfuzz Fuzz User Params

## Command

```bash
wfuzz --hc=400 -z file,wordlists/params.txt https://hackyholidays.h1ctf.com/swag-shop/api/user?FUZZ=1
```

## Description

Fuzzes parameters for the user endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --hc=400 | Hide 400 codes | No |
| -z file | Wordlist | Yes |
| URL | Target with FUZZ | Yes |

## Examples

### Basic Usage

```bash
wfuzz -z file,words.txt https://api/user?FUZZ
```

## Expected Output

Valid parameters like uuid.

## Related

- [[procedures/Fuzz-API-Endpoints-and-Extract-UUID-for-IDOR]]
