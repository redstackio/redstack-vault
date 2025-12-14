---
data: >-
  curl -X DELETE
  https://ravel2.myshopify.com/admin/api/ping-api/v1/client/installations/8eec631b-6b40-4718-9a25-16821434c4a5
  -H "Authorization: Bearer [tokenB]"
tags:
  - revoke
  - shop
type: command
output: 'HTTP/1.1 200 OK {"status":"ok"}'
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.078Z'
id: a77aef5c-7233-4c25-a224-0404b61c1614
verified: false
validated: true
submitted: true
---
# revoke-shop-installation

## Command

```bash
curl -X DELETE https://ravel2.myshopify.com/admin/api/ping-api/v1/client/installations/8eec631b-6b40-4718-9a25-16821434c4a5 -H "Authorization: Bearer [tokenB]"
```

## Description

Revokes shop-specific token installation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Authorization` | Bearer tokenB | Yes |
| Installation ID | Specific ID | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

200 OK status.

## Related

- [[Related Procedure: Initiate-Logout-in-Shopify-Ping-App]]
