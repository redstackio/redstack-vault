---
id: bcd3a873-4866-4024-8b1c-d7fcffc05f36
name: directory-brute-force
type: command
executor: bash
data: >-
  gobuster dir -u http://$_MALICIOUS_HOST -w
  /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html
output: null
created_at: '2023-04-06T03:56:31.692963+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - recon
  - web
verified: true
validated: true
---

# directory-brute-force

## Command

```bash
gobuster dir -u http://$_MALICIOUS_HOST -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html
```

## Description

Performs directory and file brute-forcing on the attacker's malicious website to discover hidden endpoints for phishing pages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Target URL | Yes |
| -w | Wordlist path | Yes |
| -x | File extensions to check | No |
| $_MALICIOUS_HOST | Attacker's host (e.g., evil-website.tld) | Yes |

## Examples

### Basic Usage

```bash
gobuster dir -u http://evil-website.tld -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

## Expected Output

Found: /phish (Status: 200) indicating discovered directories.

## Related

- [[procedures/Open-URL-Redirection-Exploitation]]
- [[commands/web-server-enumeration]]
