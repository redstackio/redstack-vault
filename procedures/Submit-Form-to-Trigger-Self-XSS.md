---
id: 123e4567-e89b-12d3-a456-426614174003
tags:
  - xss
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.134Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Form-to-Trigger-Self-XSS

## Summary

This procedure submits the workspace creation form, causing the injected payload to be rendered and execute JavaScript in the user's browser session.

## Description

Upon form submission, the server or client-side rendering processes the unsanitized workspace name, inserting the payload into the DOM. The onerror handler on the invalid <img> tag fires, executing alert(document.cookie) and displaying session cookies. As a self-XSS, this only affects the attacker but highlights the vulnerability for potential phishing or self-inflicted harm.

## Requirements

1. Payload successfully injected in prior step
2. Form ready for submission (other fields optional)
3. Active browser session

## Defense

Defensive measures and detection strategies:

- Escape all user inputs before rendering in HTML
- Deploy WAF rules to detect common XSS payloads in form data
- Monitor for JavaScript errors or alerts in client logs

## Objectives

1. Trigger payload execution via form processing
2. Confirm XSS by observing alert with cookies
3. Assess impact on session data

## Instructions

### Step 1: Submit the Form

**Context**: Interact with the submit button to process the form and render the input.

No command required; click the 'Create Workspace' or equivalent submit button.

> An alert should immediately appear showing the contents of document.cookie, proving successful self-XSS execution.

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
- [[Execution]]
