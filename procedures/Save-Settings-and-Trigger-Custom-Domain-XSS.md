---
tags:
  - xss-trigger
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/javascript-alert-document-domain]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:20.264Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e386aae8-5798-452d-88cf-0edc13a38ba0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Settings-and-Trigger-Custom-Domain-XSS

## Summary

This procedure saves the injected XSS payload in the site settings and triggers its execution via the 'View Website' button, demonstrating stored XSS impact in the admin panel context.

## Description

After injection, submitting the form stores the payload server-side. Clicking 'View Website' executes the javascript: payload from the Custom Domain field in the browser, alerting the domain and proving execution in the victim's session. This can extend to stealing cookies or performing actions if replaced with malicious code.

## Requirements

1. Payloads already entered in domain fields
2. Access to the settings form
3. Browser to observe execution

## Defense

Defensive measures and detection strategies:

- Escape or strip javascript: URIs in output rendering
- Audit form submissions for suspicious payloads
- Use browser sandboxing or extensions to detect unexpected alerts

## Objectives

1. Persist the Custom Domain payload via save
2. Execute the stored script through UI interaction
3. Validate XSS by observing alert in admin context

## Instructions

### Step 1: Submit the Settings Form

**Context**: Save the form to store the payloads on the server.

No command; manual form submission.

> Click the 'Save' button on the settings page. Expected output: Confirmation message or redirect, with payloads stored.

### Step 2: Trigger XSS with View Website

**Context**: Interact with the button to execute the stored Custom Domain payload.

**Command** ([[commands/javascript-alert-document-domain]]):

The payload executes automatically on click:

```javascript
javascript:alert(document.domain)
```

> Click 'View Website' button. Expected output: Browser alert displaying 'localhost' or the current domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/javascript-alert-document-domain]]

## Tools Used


## Tags

- xss-trigger
- stored-xss
