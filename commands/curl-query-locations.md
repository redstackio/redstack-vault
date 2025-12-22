---
id: cmd-curl-query-locations
data: >-
  curl -X GET 'https://yourstore.myshopify.com/admin/api/2023-10/locations.json'
  -H 'Authorization: Bearer your-access-token'
tags:
  - http
  - api-query
  - shopify
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.577Z'
verified: false
validated: true
submitted: true
---
# Curl-Query-Locations

## Command

```bash
curl -X GET 'https://yourstore.myshopify.com/admin/api/2023-10/locations.json' -H 'Authorization: Bearer your-access-token'
```

## Description

Retrieves the list of store locations from Shopify API to verify counts post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `-H` | Authorization header | Yes |

## Examples

### Basic Usage

```bash
curl -X GET 'https://example.com/api/locations.json' -H 'Authorization: Bearer token'
```

### Advanced Usage

```bash
curl -X GET 'https://yourstore.myshopify.com/admin/api/locations.json?limit=50' -H 'Authorization: Bearer token' | jq '.locations | length'
```

## Expected Output

JSON array of locations, e.g., {"locations":[{"id":1,...},...]}.

## Related

- [[Related Procedure]]
