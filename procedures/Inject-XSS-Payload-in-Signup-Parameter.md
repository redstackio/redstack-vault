---
tags:
  - xss
  - reflected-xss
  - javascript
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:36.262Z'
sub_techniques: []
id: c48d6121-5b33-4351-91ab-06a3b218f722
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Signup-Parameter

## Summary

This procedure exploits a reflected XSS vulnerability in the 'signup' parameter of Shopify's partners page by injecting JavaScript code, leading to immediate execution in the victim's browser context for potential session hijacking or data exfiltration.

## Description

The vulnerability occurs because the 'signup' URL parameter is directly incorporated into JavaScript code on the page without sanitization, such as in Partners.VapSignupFunnel.partnerDashboardPageLoad(<user_input>);. An attacker crafts a malicious URL and tricks a logged-in user into accessing it, executing arbitrary scripts. In a real attack, this enables stealing session cookies, keystroke logging, or redirecting to phishing sites. Prerequisites include a valid session; the procedure focuses on payload delivery via URL manipulation.

## Requirements

1. Active logged-in session on app.shopify.com
2. Web browser for testing (or link distribution for attack)
3. Knowledge of the vulnerable endpoint: https://app.shopify.com/services/partners

## Defense

Defensive measures and detection strategies:

- Validate and encode all user-controlled inputs in JavaScript contexts (e.g., use JSON.stringify or escape functions)
- Implement Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript alerts or network requests from user pages

## Objectives

1. Inject and execute JavaScript payload via the 'signup' parameter
2. Confirm exploitation through visible effects like alerts
3. Demonstrate potential for broader impacts like session theft

## Instructions

### Step 1: Craft Malicious URL

**Context**: Construct the URL with the XSS payload in the 'signup' parameter to bypass sanitization and trigger execution.

Use the base URL https://app.shopify.com/services/partners and append ?signup=<payload>&signup_action=whitehat_signup, where <payload> is JavaScript like confirm(document.domain).

> Example full URL: https://app.shopify.com/services/partners?signup=confirm(document.domain)&signup_action=whitehat_signup. This will reflect the payload into executable JS.

### Step 2: Access the URL in Logged-In Session

**Context**: Navigate to the crafted URL while authenticated, causing the page to load and execute the injected script.

Paste the URL into the browser address bar and press Enter.

> The page loads, and the JavaScript executes immediately, showing an alert with the domain. In dev tools, inspect the rendered script: Partners.VapSignupFunnel.partnerDashboardPageLoad(confirm(document.domain)); return {};

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- reflected-xss
- javascript
- shopify
