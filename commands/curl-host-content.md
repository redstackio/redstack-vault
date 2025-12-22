---
data: 'curl https://subdomain.example.com/path'
tags:
  - testing
  - web
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: ad55801b-d034-43a2-9e43-7a2652d7d6d5
created_at: '2025-12-11T06:10:30.464Z'
updated_at: '2025-12-11T06:10:30.464Z'
verified: false
validated: true
submitted: true
---
# curl-host-content

## Command

```bash
curl https://subdomain.example.com/path
```

## Description

Fetches content from a URL to verify if malicious or PoC content is being served on a taken-over subdomain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://subdomain.example.com/path` | The URL to fetch | Yes |

## Examples

### Basic Usage

```bash
curl https://devrel.roblox.com/subdomain-takeover
```

### Advanced Usage

```bash
curl -i https://devrel.roblox.com/malicious-script.php
```

## Expected Output

The hosted content, such as HTML or script output, confirming control.

## Related

- [[procedures/Host-Malicious-Content-on-Taken-Over-Subdomain]]
- [[procedures/Exploit-Cookie-Theft-and-CORS-Misconfiguration]]
