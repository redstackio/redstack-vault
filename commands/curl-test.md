---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: 'curl -I https://vex.weather.com'
tags:
  - web
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.636Z'
verified: false
validated: true
submitted: true
---
# curl-test

## Command

```bash
curl -I https://vex.weather.com
```

## Description

This command performs a HEAD request to verify control over a subdomain post-takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | HEAD request only | No |
| `https://vex.weather.com` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -I https://vex.weather.com
```

### Advanced Usage

```bash
curl -I -H "User-Agent: Mozilla/5.0" https://vex.weather.com
```

## Expected Output

HTTP headers showing 200 OK and custom content indicating successful takeover.

## Related

- [[Related Procedure: Detect-and-Exploit-Subdomain-Takeover]]
