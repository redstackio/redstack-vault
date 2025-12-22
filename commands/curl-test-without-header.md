---
data: 'curl ''http://localhost:3000/'''
tags:
  - test
  - http
type: command
output: >-
  403 Forbidden response with message 'You do not have rights to visit this
  page'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.571Z'
id: 3377015d-ce3e-4c40-aea4-12e3f7ad16c7
verified: false
validated: true
submitted: true
---
# curl-test-without-header

## Command

```bash
curl 'http://localhost:3000/'
```

## Description

Sends a plain GET request to the protected endpoint to test IP whitelist enforcement without any custom headers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://localhost:3000/` | Target URL for the root endpoint | Yes |

## Examples

### Basic Usage

```bash
curl 'http://localhost:3000/'
```

### Advanced Usage

```bash
curl -v 'http://localhost:3000/'
```

## Expected Output

HTTP/1.1 403 Forbidden followed by the denial message.

## Related

- [[commands/curl-bypass-with-header]]
- [[procedures/Test-Access-Without-Spoofing]]
