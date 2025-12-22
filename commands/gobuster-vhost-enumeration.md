---
type: command
executor: bash
data: 'gobuster vhost -u http://$_TARGET_HOST -w $_WORDLIST'
tags:
  - brute-force
  - reconnaissance
platforms:
  - Linux
  - Web
verified: true
validated: true
---

# Gobuster-Vhost-Enumeration

## Command

```bash
gobuster vhost -u http://$_TARGET_HOST -w $_WORDLIST
```

## Description

This command uses Gobuster to perform virtual host brute-forcing by enumerating potential subdomains through manipulation of the HTTP Host header. It is ideal for discovering hidden web interfaces on servers using name-based virtual hosting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_HOST | Base URL of the target web application (e.g., example.com) | Yes |
| $_WORDLIST | Path to the wordlist file containing subdomain guesses | Yes |
| -u | Specifies the target URL | Built-in |
| -w | Specifies the wordlist file | Built-in |
| vhost | Mode for virtual host enumeration | Built-in |

## Examples

### Basic Usage

```bash
gobuster vhost -u http://example.com -w /usr/share/wordlists/vhosts.txt
```

### Advanced Usage

```bash
gobuster vhost -u https://example.com -w custom-vhosts.txt --status-codes-blacklist "404,500" --wildcard
```

## Expected Output

Found: https://admin.example.com [Status 200] [Size 1234] [-> http://example.com]
Found: https://staging.example.com [Status 403] [Size 567]

Vhost responses are filtered by status codes (default: 200,204,301,302,307,401,403) and content length changes to identify valid domains.

## Related

- [[procedures/Brute-Force-Virtual-Host-Domains-Gobuster]]
- [[tools/Gobuster]]
