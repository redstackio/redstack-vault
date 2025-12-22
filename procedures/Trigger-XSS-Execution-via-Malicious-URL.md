---
tags:
  - xss
  - execution
  - slack
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
updated_at: '2025-12-14T03:15:27.073Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 54c42068-4f18-4458-8b19-032b8f68128e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS Execution via Malicious URL

## Summary

This procedure triggers the execution of the crafted XSS payload by loading a malicious URL on Slack's sign-in page, resulting in arbitrary JavaScript running in the browser.

## Description

This final step delivers the payload via a controllable URL, exploiting the reflection to execute code in the sign-in context. The target is any browser accessing the page, with potential for social engineering to lure victims. Prerequisites: Crafted payload and access to subdomain/parameter control. Expected outcome: JavaScript execution, e.g., domain prompt, confirming the exploit.

## Requirements

1. Control over a Slack subdomain (e.g., via registration) or parameter manipulation
2. Web browser to load and observe execution
3. No special network privileges beyond internet access

## Defense

Defensive measures and detection strategies:

- Enable strict CSP to block unsafe-inline and eval
- Log and alert on suspicious JavaScript execution in sign-in flows
- Rate-limit or block access from anomalous subdomains

## Objectives

1. Load URL to reflect and parse the payload
2. Execute JavaScript in Slack's domain context
3. Validate impact (e.g., credential access potential)

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the URL incorporating the subdomain or parameters with payload.

For subdomain: Use https://sshunter.slack.com/help/requests/793043. For parameters: https://slack.com/signin?redir=%2Fhelp%2Frequests%2F793043%3Fid%3D%22%3E%3Csvg%20onload%3Dprompt(document.domain)%3E.

> Expected output: URL ready for access, with payload embedded.

### Step 2: Load URL in Browser

**Context**: Trigger the page load to execute the onload event.

Paste the URL into a browser address bar and press Enter. The page should render, and the SVG onload should fire immediately.

> Expected output: Browser prompt displaying 'sshunter.slack.com' or equivalent domain.

### Step 3: Verify Execution and Impact

**Context**: Confirm the exploit's success and potential for further abuse.

Inspect console for errors; replace prompt with keylogger or form-grabber for real attacks. Test in incognito to simulate victim.

> Expected output: No blocks; code runs with access to sign-in form elements.

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
- trigger
- execution
