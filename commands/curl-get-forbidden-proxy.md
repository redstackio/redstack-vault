---
data: 'curl http://localhost:8080/forbidden'
tags:
  - curl
  - testing
type: command
executor: bash
platforms:
  - Linux
id: d47c0bea-f5db-43fa-973d-2f7b5a4bcbd7
created_at: '2025-12-13T09:01:17.088Z'
updated_at: '2025-12-13T09:01:17.088Z'
verified: false
validated: true
submitted: true
---
# curl-get-forbidden-proxy

## Command

```bash
curl http://localhost:8080/forbidden
```

## Description

Sends a GET request to the /forbidden endpoint through the ATS proxy.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://localhost:8080/forbidden` | URL of the endpoint | Yes |

## Examples

### Basic Usage

```bash
curl http://localhost:8080/forbidden
```

## Expected Output

'FORBIDDEN'

## Related

- [[procedures/Test-Access-Through-ATS-Proxy]]
- [[tools/curl]]
