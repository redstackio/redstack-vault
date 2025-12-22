---
data: // Intercept in Burp and modify request body to include payload
tags:
  - interception
type: command
output: Modified request forwarded
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:44.126Z'
id: 1d999e3d-8aac-4ea4-9c08-176eb4ce34dc
verified: false
validated: true
submitted: true
---
# burp-intercept-modify

## Command

```http
// Intercept in Burp and modify request body to include payload
POST /shop/emails/[ID] HTTP/1.1
...
html=unsanitized_payload
```

## Description

Use Burp to capture and alter HTTP requests for injecting payloads that bypass client-side checks.

## Parameters

Varies by request.

## Examples

### Basic Usage

Intercept POST, edit body, forward.

## Expected Output

Server accepts modified request.

## Related

- [[tools/Burp-Suite]]
