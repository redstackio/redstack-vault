---
data: 'curl http://localhost:8081/forbidden'
tags:
  - curl
  - testing
type: command
executor: bash
platforms:
  - Linux
id: 7d76bf00-f640-4be7-ad8f-946e0ae0c24d
created_at: '2025-12-13T09:01:17.095Z'
updated_at: '2025-12-13T09:01:17.095Z'
verified: false
validated: true
submitted: true
---
# curl-get-forbidden-direct

## Command

```bash
curl http://localhost:8081/forbidden
```

## Description

Sends a GET request to the /forbidden endpoint of the Node.js server directly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://localhost:8081/forbidden` | URL of the endpoint | Yes |

## Examples

### Basic Usage

```bash
curl http://localhost:8081/forbidden
```

## Expected Output

'FORBIDDEN'

## Related

- [[procedures/Test-Direct-Access-to-Node-js-Server]]
- [[tools/curl]]
