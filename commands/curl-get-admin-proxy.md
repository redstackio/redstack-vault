---
data: 'curl http://localhost:8080/admin'
tags:
  - curl
  - testing
type: command
executor: bash
platforms:
  - Linux
id: 6bee250b-1e67-4273-9b58-90cac2f0f835
created_at: '2025-12-13T09:01:17.090Z'
updated_at: '2025-12-13T09:01:17.090Z'
verified: false
validated: true
submitted: true
---
# curl-get-admin-proxy

## Command

```bash
curl http://localhost:8080/admin
```

## Description

Sends a GET request to the /admin endpoint through the ATS proxy, expecting rerouting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://localhost:8080/admin` | URL of the endpoint | Yes |

## Examples

### Basic Usage

```bash
curl http://localhost:8080/admin
```

## Expected Output

'FORBIDDEN'

## Related

- [[procedures/Test-Access-Through-ATS-Proxy]]
- [[tools/curl]]
