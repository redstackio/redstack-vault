---
data: 'curl http://localhost:8081/admin'
tags:
  - curl
  - testing
type: command
executor: bash
platforms:
  - Linux
id: 780aa3aa-95e2-477b-9f15-6d056874d5fb
created_at: '2025-12-13T09:01:17.098Z'
updated_at: '2025-12-13T09:01:17.098Z'
verified: false
validated: true
submitted: true
---
# curl-get-admin-direct

## Command

```bash
curl http://localhost:8081/admin
```

## Description

Sends a GET request to the /admin endpoint of the Node.js server directly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://localhost:8081/admin` | URL of the endpoint | Yes |

## Examples

### Basic Usage

```bash
curl http://localhost:8081/admin
```

## Expected Output

'ADMIN'

## Related

- [[procedures/Test-Direct-Access-to-Node-js-Server]]
- [[tools/curl]]
