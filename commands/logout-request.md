---
data: >-
  curl -X DELETE https://accounts.shopify.com/api/v1/logout -H "Authorization:
  Bearer [tokenA]"
tags:
  - logout
  - vulnerability
type: command
output: 'HTTP/1.1 400 Bad Request {"error":"Missing Logout Token Hint"}'
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.061Z'
id: 80bd2cd4-5bc8-4aa5-89bf-729b0af89941
verified: false
validated: true
submitted: true
---
# logout-request

## Command

```bash
curl -X DELETE https://accounts.shopify.com/api/v1/logout -H "Authorization: Bearer [tokenA]"
```

## Description

Attempts to logout tokenA, fails without hint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Authorization` | Bearer tokenA | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

400 error.

## Related

- [[Related Procedure: Initiate-Logout-in-Shopify-Ping-App]]
