---
id: proc-semrush-trigger-xss
tags:
  - xss-execution
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.474Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Update-Settings-and-Trigger-Stored-XSS

## Summary

This procedure finalizes the storage of the injected XSS payload by updating project settings and triggers its execution upon page reload, resulting in JavaScript alert displaying stolen cookies.

## Description

After injection, submitting the update persists the payload in SEMrush's backend. Reloading the page renders the unsanitized input, executing the JavaScript in the victim's context. This stored XSS affects any user viewing the project dashboard, with impacts including session theft via document.cookie. It targets the web platform and assumes the payload has been successfully injected.

## Requirements

1. Injected payload from prior interception step
2. Open Position Tracking Settings page
3. Browser session with the project

## Defense

Defensive measures and detection strategies:

- Sanitize all stored user inputs with HTML entity encoding before rendering
- Deploy Content Security Policy (CSP) to block inline scripts and unsafe attributes
- Alert on JavaScript errors or unexpected alerts in application logs

## Objectives

1. Persist the malicious payload in project data
2. Execute arbitrary JS to demonstrate impact (e.g., cookie theft)
3. Simulate real-world effects like defacement or session hijack

## Instructions

### Step 1: Submit Updates

**Context**: Save the modified competitor list to the backend.

No specific command; use the UI:

- With the payload-added list visible, click the 'Update' button
- Confirm any prompts and wait for success message

> Settings update completes; no errors indicate storage success.

### Step 2: Close and Reload Page

**Context**: Trigger rendering of the stored payload to execute XSS.

No specific command; navigate:

- Close the 'Position Tracking Settings' page
- Return to or reload the Rankings Distribution tab

> Alert dialog appears with contents of document.cookie, confirming execution.

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

- stored-xss
- execution
- exfiltration
