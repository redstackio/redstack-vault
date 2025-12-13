---
data: 'curl [options] [url]'
tags:
  - http
  - web
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 4253750c-68d1-44a0-8da2-2c82d75299e1
created_at: '2025-12-13T09:01:17.522Z'
updated_at: '2025-12-13T09:01:17.522Z'
verified: false
validated: true
submitted: true
---
# Curl Send HTTP Request

## Command

```bash
curl [options] [url]
```

## Description

Uses curl to send custom HTTP requests, useful for testing web vulnerabilities like HTTP Request Smuggling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Add custom header | No |
| `--data` | Send POST data | No |
| `-I` | HEAD request | No |

## Examples

### Basic Usage

```bash
curl -I http://target.com
```

### Advanced Usage

```bash
curl -H "Transfer-Encoding: chunked" --data "payload" http://target.com
```

## Expected Output

HTTP response headers and body, indicating server behavior.

## Related

- [[procedures/Craft-HTTP-Smuggling-Request]]
- [[procedures/Identify-Vulnerable-Node.js-Application]]
