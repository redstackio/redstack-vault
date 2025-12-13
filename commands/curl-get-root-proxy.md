---
data: 'curl http://localhost:8080'
tags:
  - curl
  - testing
type: command
executor: bash
platforms:
  - Linux
id: 7eb36c61-7f39-4e34-bb32-c11735a7d38e
created_at: '2025-12-13T09:01:17.092Z'
updated_at: '2025-12-13T09:01:17.092Z'
verified: false
validated: true
submitted: true
---
# curl-get-root-proxy

## Command

```bash
curl http://localhost:8080
```

## Description

Sends a GET request to the root endpoint through the ATS proxy.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://localhost:8080` | URL of the endpoint | Yes |

## Examples

### Basic Usage

```bash
curl http://localhost:8080
```

## Expected Output

'INDEX'

## Related

- [[procedures/Test-Access-Through-ATS-Proxy]]
- [[tools/curl]]
