---
data: 'curl -X GET "https://www.lyst.com/email-capture/stock-alert/93543518/" -v'
tags:
  - csrf
  - test
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:42.555Z'
id: 34afc738-cb48-4a31-8513-18153abb1644
verified: false
validated: true
submitted: true
---
# test-stock-alert-endpoint

## Command

```bash
curl -X GET "https://www.lyst.com/email-capture/stock-alert/93543518/" -v
```

## Description

Tests the Lyst stock alert endpoint by sending a GET request with a product ID to verify it adds the item to the saved list without CSRF protection. Use during reconnaissance to confirm vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Product ID (e.g., 93543518) | Lyst product identifier in URL path | Yes |
| -v | Verbose output for headers and response | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.lyst.com/email-capture/stock-alert/93543518/" -v
```

### Advanced Usage

```bash
curl -X GET "https://www.lyst.com/email-capture/stock-alert/93543518/?return_url=/somewhere" -v -H "Cookie: session=abc"
```

## Expected Output

HTTP 200 OK or 302 redirect with Location header; no CSRF errors. Item added to saved list upon authentication check.

## Related

- [[commands/csrf-chained-stock-alert-get]]
