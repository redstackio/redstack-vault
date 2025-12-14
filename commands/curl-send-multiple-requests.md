---
id: cmd-curl-multiple-requests
data: >-
  for i in {1..12}; do curl -X POST
  'https://yourstore.myshopify.com/admin/api/2023-10/locations.json' -H
  'Authorization: Bearer your-access-token' -H 'Content-Type: application/json'
  -d '{"location":{"name":"Test Loc $i","address1":"123 St"}}' & done
tags:
  - http
  - race-condition
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.588Z'
verified: false
validated: true
submitted: true
---
# Curl-Send-Multiple-Requests

## Command

```bash
for i in {1..12}; do curl -X POST 'https://yourstore.myshopify.com/admin/api/2023-10/locations.json' -H 'Authorization: Bearer your-access-token' -H 'Content-Type: application/json' -d '{"location":{"name":"Test Loc $i","address1":"123 St"}}' & done
```

## Description

Sends multiple concurrent POST requests to create Shopify locations, exploiting race conditions by using background processes for parallelism.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H` | Add headers (e.g., auth, content-type) | Yes |
| `-d` | JSON payload | Yes |
| `&` | Background execution for concurrency | Yes |

## Examples

### Basic Usage

```bash
for i in {1..5}; do curl -X POST 'https://example.com/api' -d '{}' & done
```

### Advanced Usage

```bash
parallel -j12 curl -X POST 'https://yourstore.myshopify.com/admin/api/locations.json' -H 'Authorization: Bearer token' -d '{"location":{}}' ::: {1..12}
```

## Expected Output

Multiple lines of 201 Created responses with location IDs.

## Related

- [[Related Procedure]]
