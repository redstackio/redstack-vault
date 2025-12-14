---
tags:
  - xss
  - javascript-execution
  - client-side
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
id: 6691812d-3899-4d9e-9a53-3acb77364622
created_at: '2025-12-14T03:15:53.258Z'
updated_at: '2025-12-14T03:15:53.258Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Clicking-Hyperlink

## Summary

This procedure executes the XSS payload by clicking the malicious hyperlink in the unsanitized email view, resulting in arbitrary JavaScript running in the authenticated user's browser context.

## Description

Once the email is viewed in 'original HTML' mode, clicking the hyperlink with the javascript: URI (e.g., javascript:alert(0);) causes the browser to execute the JavaScript directly. This leads to client-side attacks such as stealing session cookies via document.cookie, keylogging, or further exploitation. The vulnerability stems from unvalidated URI schemes in hyperlinks, impacting any user viewing the email.

## Requirements

1. The email must be open in 'original HTML' view with the hyperlink visible
2. User interaction (click) on the link
3. Modern web browser without restrictions on javascript: URIs

## Defense

Defensive measures and detection strategies:

- Strip or validate all URI schemes in email hyperlinks server-side
- Implement browser extensions or policies to block javascript: protocol execution
- Monitor for unexpected JavaScript alerts or DOM manipulations in web app logs

## Objectives

1. Execute arbitrary JavaScript in the victim's browser
2. Access sensitive data like session cookies
3. Enable further attacks such as account takeover

## Instructions

### Step 1: Interact with the Hyperlink

**Context**: Click the malicious link to trigger the URI execution and confirm the XSS vulnerability.

In the rendered email view, locate and click the hyperlink containing the javascript: URI payload. Observe the immediate execution, such as an alert dialog popping up.

> For exploitation, replace alert(0) with code to exfiltrate data, e.g., fetch('/steal?cookie=' + document.cookie).

**Expected Output**: JavaScript payload executes, displaying an alert or performing other actions in the browser.

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

- [[xss]]
- [[javascript-execution]]
- [[client-side]]
