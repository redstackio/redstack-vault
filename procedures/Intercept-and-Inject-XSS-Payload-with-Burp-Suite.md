---
id: proc-xss-injection-burp-001
tags:
  - xss
  - payload-injection
  - burp-suite
  - request-modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:55.459Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Inject-XSS-Payload-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept the quiz save request on Crowdsignal, modify the media_code parameter with a JavaScript payload, and forward it to inject stored XSS, exploiting lack of sanitization.

## Description

Targeting the save endpoint during photo insertion in quiz creation, this step captures HTTP traffic, identifies the media_code parameter (originally a photo ID), and replaces it with a payload like `"><svg/onload=alert(document.domain)>`. This allows arbitrary JavaScript to be stored and executed later. The attack scenario assumes proxy setup and applies to web environments. Prerequisites include the quiz setup from prior steps. Outcomes: Payload stored in the quiz, leading to execution on save and view.

## Requirements

1. Burp Suite installed and configured as browser proxy
2. Ongoing authenticated session in Crowdsignal quiz editor
3. Knowledge of HTTP request structure for parameter modification

## Defense

Defensive measures and detection strategies:

- Server-side sanitization of media_code using HTML entity encoding or allowlisting
- Proxy detection via HTTP headers (e.g., block requests with X-Forwarded-For mismatches)
- WAF rules to flag SVG tags or onload attributes in POST data

## Objectives

1. Bypass input validation by tampering with the save request
2. Inject persistent JavaScript for stored XSS
3. Ensure the modified request is accepted by the server

## Instructions

### Step 1: Configure and Start Interception

**Context**: Set up Burp Suite to capture traffic from the browser to the Crowdsignal save endpoint.

No command required; use Burp Suite interface:

- Launch Burp Suite and enable Intercept in Proxy > Intercept tab
- Ensure browser proxy points to Burp (e.g., 127.0.0.1:8080)
- In quiz editor, click Save after image upload

> Expected output: Request paused in Burp with media_code parameter visible.

### Step 2: Modify media_code and Forward

**Context**: Locate and alter the vulnerable parameter to inject the XSS payload.

No command required; edit in Burp Repeater or Proxy:

- In the intercepted POST request, find `media_code=PHOTO_ID`
- Replace value with `media_code="><svg/onload=alert(document.domain)>`
- Click Forward to send the request

> Expected output: Server responds with 200 OK, quiz saves with injected payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[payload-injection]]
