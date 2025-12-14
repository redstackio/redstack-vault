---
id: proc-uuid-step2
tags:
  - xss
  - injection-test
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:32.097Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test Reflected XSS in frm_email Parameter

## Summary

This procedure tests for reflected XSS vulnerability in the frm_email field by injecting a JavaScript payload via Burp Suite, confirming unsanitized reflection in the response.

## Description

Reflected XSS occurs when user input from the frm_email parameter is echoed back into the HTML response without escaping, allowing script execution in the victim's browser context on *.██████████. The test payload 'nagli@wearehackerone.com"/><svg/onload=alert(document.domain)>' breaks out of the attribute and injects an onload handler, executing on response rendering.

## Requirements

1. Captured profile update request from previous step
2. Burp Suite Repeater tab open with the request loaded
3. Authenticated session cookies valid

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs, especially in HTML contexts
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous payloads in logs (e.g., <svg> tags)

## Objectives

1. Confirm XSS vulnerability in frm_email
2. Validate payload execution in target domain context
3. Assess potential for chaining with other exploits

## Instructions

### Step 1: Load Request in Repeater

**Context**: Prepare the intercepted request for modification.

In Burp Suite, send the captured POST to Repeater. Ensure the request includes valid authentication cookies and other parameters.

### Step 2: Inject XSS Payload

**Context**: Modify frm_email to test reflection and execution.

Replace the frm_email value with: nagli@wearehackerone.com"/><svg/onload=alert(document.domain)>

Click 'Send' to forward the request. Switch to the browser or inspect the response in Repeater's Inspector.

**Expected Output**: Response HTML contains the unescaped payload, triggering an alert box showing the domain (e.g., subdomain.██████████).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- xss
- injection-test
