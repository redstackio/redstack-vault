---
id: proc-uuid-3
tags:
  - xss
  - verification
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud (Shopify)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.216Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-XSS-Execution-on-Error-Page

## Summary

This procedure confirms the reflected XSS by observing the error page response and ensuring injected HTML executes in the browser.

## Description

After submitting a malformed registration (short password), Shopify returns an error page that includes the provided first_name and last_name without sanitization. This reflection allows arbitrary JS execution, such as cookie theft or phishing. The procedure uses browser inspection to validate; impacts include session hijacking or malware delivery, with higher risk if the victim is a staff user accessing admin areas.

## Requirements

1. Successful payload submission from prior step
2. Web browser with developer tools
3. Attacker server for exfiltration testing (optional)

## Defense

Defensive measures and detection strategies:

- Encode user input in all error responses (e.g., using Shopify's Liquid templating securely)
- Implement Content Security Policy (CSP) to block inline scripts
- Log and alert on suspicious error page accesses
- Deploy WAF rules to detect script tags in POST data

## Objectives

1. Confirm unsanitized reflection
2. Test JS execution capabilities
3. Assess potential impacts like data exfiltration

## Instructions

### Step 1: Submit and Load Response

**Context**: Use browser to POST the payload and load the error page.

Fill the form with payload in names, short password, and submit.

### Step 2: Inspect Error Page

**Context**: Check for reflected input in the DOM.

Open dev tools (F12), go to Elements tab, search for the injected script.

**Expected Output**: Script tag present and not escaped.

### Step 3: Execute and Validate

**Context**: Trigger execution and monitor effects.

Refresh or resubmit; watch for alert or console errors.

**Expected Output**: JS runs, e.g., alert dialog or network tab shows exfil request.

**Success Indicators**:
- JS payload executes without errors
- Victim context allows access to cookies or DOM

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
- [[verification]]
- [[shopify]]
