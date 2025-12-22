---
id: proc-uuid-003
name: Intercept-and-Inject-XSS-Payload
tags:
  - xss
  - payload-injection
  - http-interception
type: procedure
tools:
  - '[[tools/HTTP-Proxy-Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/modify-post-request-burp]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:16.205Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Intercept-and-Inject-XSS-Payload

## Summary

This procedure intercepts the POST request for updating a Wholesale price list and injects a stored XSS payload into the csv_file_name parameter, exploiting improper escaping in JavaScript context.

## Description

After creating a price list, editing it triggers a POST to /admin/shops/x/price_lists/x. Using an HTTP proxy like Burp Suite, capture this request and modify price_list[csv_file_name] to 'sample-csv-sku.csv"-alert(document.domain)-"', breaking out of string context to inject JavaScript. This stores the payload for later execution on the shared domain. Prerequisites: Proxy configured for browser traffic. Outcomes: Payload stored without detection.

## Requirements

1. HTTP proxy tool (e.g., Burp Suite) intercepting browser traffic
2. Existing price list from prior procedure
3. Knowledge of request parameters

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in JavaScript contexts (e.g., use DOMPurify)
- Implement Content Security Policy (CSP) to restrict inline scripts
- Monitor proxy-intercepted requests in WAF logs for parameter tampering

## Objectives

1. Capture and alter the update request
2. Inject executable JavaScript via file name
3. Store payload for cross-site execution

## Instructions

### Step 1: Trigger and Intercept Update Request

**Context**: Edit the price list to generate the POST request for interception.

Use [[commands/modify-post-request-burp]] or proxy UI:

In Burp Suite, set browser proxy, edit price list in admin, intercept the POST to /admin/shops/x/price_lists/x.

```bash
# Simulated curl for reference (actual via proxy)
curl -X POST 'https://admin.shopify.com/admin/shops/x/price_lists/x' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-raw 'price_list[csv_file_name]=sample-csv-sku.csv&other=params'
```

> Request paused in proxy; parameters visible for modification.

### Step 2: Inject XSS Payload

**Context**: Modify the file name parameter to include JavaScript breakout.

In proxy, change to:

price_list[csv_file_name]='sample-csv-sku.csv"-alert(document.domain)-"'

Forward the request.

> Request completes; price list updates with injected payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/modify-post-request-burp]]

## Tools Used

- [[tools/HTTP-Proxy-Burp-Suite]]

## Tags

- [[xss]]
- [[payload-injection]]
- [[http-interception]]
