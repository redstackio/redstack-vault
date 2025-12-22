---
id: cmd-curl-host-7357
data: 'curl -H "Host: evil.com" http://irccloud.com/ -v'
tags:
  - http
  - header-injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:26.236Z'
verified: false
validated: true
submitted: true
---
# curl-send-host-header

## Command

```bash
curl -H "Host: evil.com" http://irccloud.com/ -v
```

## Description

This command uses curl to send an HTTP GET request to irccloud.com with a custom Host header set to an arbitrary domain, exploiting the lack of validation to trigger an open redirect. Use it to test Host header injection vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Host: <domain>"` | Sets the Host header to the specified domain for injection | Yes |
| `http://irccloud.com/` | Target URL endpoint | Yes |
| `-v` | Verbose output to show headers and response | No |

## Examples

### Basic Usage

```bash
curl -H "Host: evil.com" http://irccloud.com/ -v
```

### Advanced Usage

```bash
curl -H "Host: attacker.com" -X GET http://irccloud.com/login -v -i
```

## Expected Output

Verbose output showing a 302 redirect with Location: http://evil.com/ or similar, confirming the injection success. No validation errors appear.

## Related

- [[Related Procedure: Send-Request-with-Invalid-Host-Header]]
