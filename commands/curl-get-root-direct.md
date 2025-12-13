---
data: 'curl http://localhost:8081'
tags:
  - curl
  - testing
type: command
executor: bash
platforms:
  - Linux
id: 9468509e-e2e3-4029-a9e6-4e5efbd5466e
created_at: '2025-12-13T09:01:17.101Z'
updated_at: '2025-12-13T09:01:17.101Z'
verified: false
validated: true
submitted: true
---
# curl-get-root-direct

## Command

```bash
curl http://localhost:8081
```

## Description

Sends a GET request to the root endpoint of the Node.js server directly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://localhost:8081` | URL of the endpoint | Yes |

## Examples

### Basic Usage

```bash
curl http://localhost:8081
```

## Expected Output

'INDEX'

## Related

- [[procedures/Test-Direct-Access-to-Node-js-Server]]
- [[tools/curl]]
