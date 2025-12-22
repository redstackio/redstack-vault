---
tags:
  - xss
  - wordpress
  - url-manipulation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:38.933Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 83f326e4-782c-4b09-ba9c-d4ce555cd669
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate-to-Vulnerable-Redirect-Endpoint

## Summary

This procedure involves directing an authenticated browser session to the vulnerable WordPress.com account user page with a crafted 'redirect_to' parameter containing a JavaScript URI, setting up the reflected XSS without immediate execution.

## Description

The vulnerability lies in the lack of sanitization for the 'redirect_to' parameter on https://wordpress.com/start/account/user. By appending a javascript: URI, the parameter is reflected into the page. Clicking 'continue' triggers execution in the authenticated context. This step focuses on URL construction and navigation, assuming authentication is already established.

## Requirements

1. Active authenticated session from prior login
2. Web browser capable of handling JavaScript URIs
3. Knowledge of the exact vulnerable URL structure

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all URL parameters, rejecting javascript: schemes
- Implement Content Security Policy (CSP) to block inline JavaScript execution
- Log and monitor unusual parameter values in access logs

## Objectives

1. Reach the vulnerable endpoint with injected payload
2. Confirm reflection of the parameter in the page source
3. Prepare for payload triggering without alerting defenses

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the URL incorporating the vulnerable parameter with a proof-of-concept payload.

Manually construct: https://wordpress.com/start/account/user?variationName=free&redirect_to=javascript:alert(document.domain)

> Ensure the session is active; paste into browser address bar.

### Step 2: Load and Interact

**Context**: Visit the URL and perform the action that reflects the payload.

Load the page and click the 'continue' button.

> The page should render, showing the reflected parameter. Inspect source to verify unsanitized javascript: URI presence.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- wordpress
- url-manipulation
