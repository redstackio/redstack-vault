---
tags:
  - xss
  - self-xss
  - execution
  - uber
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 2ce25e08-8a45-4081-b974-35a13e2bbda3
created_at: '2025-12-14T03:15:26.592Z'
updated_at: '2025-12-14T03:15:26.592Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe-Self-XSS-Execution

## Summary

This procedure verifies the success of the Self-XSS exploit by observing JavaScript execution in the browser following payload submission in Uber's password reset form.

## Description

After injecting the payload, this step focuses on confirming execution via the triggered onerror event, which prompts the document domain. The impact is self-contained, running only in the attacker's browser, but demonstrates the vulnerability. Use browser console or alerts to validate. This confirms the root cause: improper sanitization of the new password field.

## Requirements

1. Successful form submission from prior procedure
2. Browser with pop-up alerts enabled
3. Optional: Browser developer console open

## Defense

Defensive measures and detection strategies:

- Validate password strength and reject inputs containing HTML/JS characters
- Use server-side rendering with strict output encoding (e.g., OWASP guidelines)
- Employ Web Application Firewall (WAF) rules to block common XSS patterns in forms

## Objectives

1. Confirm JavaScript execution in the page context
2. Document the reflected payload for reporting
3. Assess the scope (self-only) to determine severity

## Instructions

### Step 1: Monitor Page Response

**Context**: Watch for immediate effects after submission.

Upon form submission, observe the page load or error message for reflected content.

> Look for the injected <img> tag in the HTML source (View Page Source) to confirm reflection.

### Step 2: Check for Alert/Prompt

**Context**: Verify JS execution via the payload's onerror handler.

A browser prompt or alert should appear displaying 'partners.uber.com' (document.domain).

> If no alert, check the browser console (F12 > Console) for errors or execution logs.

### Step 3: Validate Scope

**Context**: Ensure the XSS is self-contained.

Test if the execution affects other tabs/sessions; it should not, confirming Self-XSS.

> Attempt the payload in an incognito window or different account to verify no cross-user impact.

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
- self-xss
- execution
