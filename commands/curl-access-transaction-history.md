---
id: cmd-curl-access-history
data: >-
  curl -H "Cookie: session=your_session_cookie"
  https://cashier.unikrn.com/cashier/transaction-history
tags:
  - web-request
  - session
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:48.256Z'
verified: false
validated: true
submitted: true
---
# curl-access-transaction-history

## Command

```bash
curl -H "Cookie: session=your_session_cookie" https://cashier.unikrn.com/cashier/transaction-history
```

## Description

This command accesses the Unikrn transaction history endpoint with an authenticated session cookie to initiate the session handshake. Use it to verify endpoint access before IDOR exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: session=..."` | Authenticates the request with session cookie | Yes |
| URL | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: session=abc123" https://cashier.unikrn.com/cashier/transaction-history
```

### Advanced Usage

```bash
curl -v -H "Cookie: session=abc123" https://cashier.unikrn.com/cashier/transaction-history
```

## Expected Output

HTTP 200 response with JSON containing transaction data or session handshake details, e.g., {"transactions": [...], "userId": 456}.

## Related

- [[Related Procedure|procedures/Access-Unikrn-Transaction-History-Endpoint]]
