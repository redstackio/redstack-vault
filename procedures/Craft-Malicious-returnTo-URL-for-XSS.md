---
tags:
  - xss
  - url-crafting
  - javascript-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 9ef3a13f-bcb5-46c0-8890-c27c89620d39
created_at: '2025-12-13T23:55:38.264Z'
updated_at: '2025-12-13T23:55:38.264Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-returnTo-URL-for-XSS

## Summary

This procedure involves constructing a malicious URL targeting the Shopify Help Center's 'returnTo' parameter to inject JavaScript via the 'javascript:' protocol, setting up a reflected XSS attack.

## Description

The 'returnTo' parameter in the https://help.shopify.com/en/support/confirm-account-details endpoint lacks proper sanitization, allowing attackers to append 'javascript:' payloads. When a user with an incomplete account visits the URL, logs in, and clicks 'Continue', the payload executes in the browser context. This can steal cookies, perform redirects, or execute other malicious scripts. Prerequisites include knowledge of URL encoding and JavaScript basics; the attack relies on social engineering to get victims to interact.

## Requirements

1. Web browser for testing
2. Understanding of URL parameters and JavaScript payloads
3. Access to a test or victim Shopify account in incomplete state

## Defense

Defensive measures and detection strategies:

- Validate and sanitize 'returnTo' parameters to block non-http/https protocols
- Implement Content Security Policy (CSP) to restrict inline JavaScript execution
- Monitor for unusual javascript: URLs in access logs
- Educate users on phishing risks and incomplete account handling

## Objectives

1. Inject arbitrary JavaScript into the page context
2. Prepare for execution upon user interaction
3. Enable data exfiltration or redirects

## Instructions

### Step 1: Identify the Endpoint

**Context**: Locate the vulnerable endpoint in the Shopify Help Center.

No command required; note the base URL: https://help.shopify.com/en/support/confirm-account-details.

### Step 2: Append Malicious Payload

**Context**: Craft the 'returnTo' parameter with a javascript: payload to test XSS, such as alerting cookies.

Construct the full URL manually:

```url
https://help.shopify.com/en/support/confirm-account-details?returnTo=javascript:alert(document.cookie)
```

> This URL, when processed, reflects the payload for later execution. For production attacks, encode the payload if needed and customize (e.g., to send cookies to an external server).

### Step 3: Open the URL in Browser

**Context**: Load the crafted URL to initiate the flow.

Navigate to the URL in a web browser.

**Expected Output**: The page loads, potentially prompting account actions, with the parameter present in the query string.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[url-crafting]]
