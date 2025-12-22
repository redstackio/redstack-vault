---
tags:
  - xss-trigger
  - user-interaction
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 21e742df-7bb5-4b59-906a-7e018ee7ba6e
created_at: '2025-12-13T23:55:38.245Z'
updated_at: '2025-12-13T23:55:38.245Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Continue-Button

## Summary

This procedure triggers the reflected XSS by navigating back to the malicious URL and clicking the 'Continue' button, executing the injected JavaScript payload to steal cookies or redirect the user.

## Description

After login, returning to the crafted URL and interacting with the 'Continue' button causes the application to process the unsanitized 'returnTo' parameter, executing the javascript: payload in the browser. This leads to arbitrary code execution, such as alerting or exfiltrating document cookies, or performing an open redirect. The attack requires user interaction but can be socially engineered.

## Requirements

1. Active browser session post-login
2. Malicious URL from previous step
3. Incomplete account state

## Defense

Defensive measures and detection strategies:

- Sanitize 'returnTo' to whitelist only safe protocols (http/https)
- Block or escape javascript: URIs in redirects
- Implement browser-side CSP headers to prevent inline script execution
- Monitor for anomalous JavaScript alerts or redirects in client logs

## Objectives

1. Execute the injected JavaScript
2. Collect sensitive data like cookies
3. Achieve session hijacking or phishing

## Instructions

### Step 1: Navigate Back to Malicious URL

**Context**: Reload or return to the original URL to re-apply the 'returnTo' parameter in the authenticated context.

Manually enter or bookmark-navigate to: https://help.shopify.com/en/support/confirm-account-details?returnTo=javascript:alert(document.cookie)

### Step 2: Interact with Continue Button

**Context**: Click the button to process the parameter and trigger the redirect/execution.

Locate and click the 'Continue' button on the page.

**Expected Output**: The payload executes, e.g., an alert box displays the document's cookies.

### Step 3: Verify Execution and Exfiltrate

**Context**: Confirm the XSS fired and adapt for real exfiltration.

Observe the alert or modify payload for data send (e.g., to attacker server). For open redirect, use http://malicious-site.com.

**Expected Output**: Cookies exposed or redirect occurs, enabling further attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[cookie-theft]]
