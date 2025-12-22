---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -s "https://target.com/?p=123" -H "User-Agent: Mozilla/5.0" | grep -i
  "private content"
tags:
  - web
  - recon
  - access
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:19.684Z'
verified: false
validated: true
submitted: true
---
# curl-access-private-post

## Command

```bash
curl -s "https://target.com/?p=123" -H "User-Agent: Mozilla/5.0" | grep -i "private content"
```

## Description

This command uses curl to perform an unauthenticated HTTP GET request to a WordPress private post URL, checking for disclosure of restricted content. It is used to test access control bypass vulnerabilities in outdated WordPress installations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `"https://target.com/?p=123"` | Target URL with post ID | Yes |
| `-H "User-Agent: Mozilla/5.0"` | Sets a browser-like user agent to avoid detection | No |
| `| grep -i "private content"` | Filters output for indicators of private data | No |

## Examples

### Basic Usage

```bash
curl -s "https://target.com/?p=123"
```

### Advanced Usage

```bash
curl -s "https://target.com/?p=123" -H "User-Agent: Mozilla/5.0" -o post.html | grep -i "private"
```

## Expected Output

HTML content of the private post if vulnerable, e.g., lines containing post title, body, and any private markers. No output or a login redirect indicates failure.

## Related

- [[Related Procedure: Exploit-WordPress-Private-Post-Access-Bypass]]
