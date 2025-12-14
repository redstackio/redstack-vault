---
id: proc-trigger-xss-001
tags:
  - xss-execution
  - stored-xss
  - html-rendering
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
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
updated_at: '2025-12-13T23:55:38.329Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS by Accessing Payment Info

## Summary

This procedure triggers the execution of the stored XSS payload by accessing the payment method info endpoint, where the injected ipAddress is rendered as HTML in the victim's browser.

## Description

After injection, visit /api/paymentMethodInfoById/ID, which fetches and displays the payment details including the tainted ipAddress. Due to HTML rendering without escaping, the JavaScript executes, potentially alerting or stealing cookies.

## Requirements

1. Injected payload from prior step
2. Access to the payment info view (authenticated or public if misconfigured)
3. Victim browser context

## Defense

Defensive measures and detection strategies:

- Escape HTML outputs in all API responses
- Set Content-Type to application/json for API endpoints
- Implement XSS auditors or CSP to block inline scripts

## Objectives

1. Execute arbitrary JavaScript in browser context
2. Achieve code execution for data exfiltration
3. Validate the full XSS chain

## Instructions

### Step 1: Navigate to Endpoint

**Context**: Use the browser to load the payment info page or API response.

Open https://example.8x8.com/api/paymentMethodInfoById/ID in the browser.

> The page renders the ipAddress as HTML, triggering onload events.

### Step 2: Observe Execution

**Context**: Monitor console and alerts for payload activation.

No command; watch for alert(document.domain) or network requests from the script.

> Success if JavaScript runs, e.g., domain alert pops up.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- [[xss-execution]]
- [[stored-xss]]
