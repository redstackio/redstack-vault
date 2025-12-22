---
id: cmd-uuid-001
data: >-
  curl -X GET
  "https://www.zomato.com/gold/payment-success?subscription_id=██████████&user_id=█████████"
  -i
tags:
  - web
  - access
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.672Z'
verified: false
validated: true
submitted: true
---
# curl-access-known-endpoint

## Command

```bash
curl -X GET "https://www.zomato.com/gold/payment-success?subscription_id=██████████&user_id=█████████" -i
```

## Description

Accesses the Zomato Gold payment success endpoint with known parameters to observe normal response behavior.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| URL | Endpoint with subscription_id and user_id | Yes |
| `-i` | Includes response headers | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.zomato.com/gold/payment-success?subscription_id=██████████&user_id=█████████" -i
```

### Advanced Usage

```bash
curl -X GET "https://www.zomato.com/gold/payment-success?subscription_id=██████████&user_id=█████████" -i -v
```

## Expected Output

HTTP/1.1 200 OK headers followed by body containing subscription details like dates and plan.

## Related

- [[Related Procedure]]
