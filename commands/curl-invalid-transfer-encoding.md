---
id: cmd-curl-invalid-te
data: >-
  curl -X POST https://www.paypal.com/ -H "Transfer-Encoding: invalid" -d "dummy
  payload" -v
tags:
  - web
  - http
type: command
output: |-
  HTTP/1.1 501 Not Implemented
  ...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:02.987Z'
verified: false
validated: true
submitted: true
---
# curl-invalid-transfer-encoding

## Command

```bash
curl -X POST https://www.paypal.com/ -H "Transfer-Encoding: invalid" -d "dummy payload" -v
```

## Description

Sends an HTTP POST request with an invalid Transfer-Encoding header to test for cache poisoning vulnerabilities. Use this to probe servers that fail to sanitize headers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Transfer-Encoding: invalid"` | Adds the malicious header | Yes |
| `-d "dummy payload"` | Provides request body | No |
| `-v` | Enables verbose output | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.paypal.com/ -H "Transfer-Encoding: invalid" -d "dummy payload" -v
```

### Advanced Usage

```bash
curl -X GET https://www.paypal.com/ -H "Transfer-Encoding: invalid" -v
```

## Expected Output

Verbose logs showing request headers sent and a 501 Not Implemented response, indicating header processing.

## Related

- [[Related Procedure: Craft-Malicious-Request-with-Invalid-Transfer-Encoding]]
