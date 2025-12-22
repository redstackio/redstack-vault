---
tags:
  - xss-trigger
  - execution
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: 2c8e0ea3-ca9f-4f08-ba95-69392aebac91
created_at: '2025-12-14T03:16:20.715Z'
updated_at: '2025-12-14T03:16:20.715Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save and Trigger XSS in Template

## Summary

This procedure covers saving the modified template with the injected payload and viewing it to execute the stored JavaScript, confirming the XSS vulnerability.

## Description

After payload injection in Mixmax's Social Badges, saving persists the malicious URL. Viewing or reloading the template renders the badges, triggering the javascript: handler in the browser context. This affects the current user and potentially others viewing shared templates, enabling actions like session theft. Prerequisites: injected payload in an open template.

## Requirements

1. Template with injected payload ready
2. Browser session in Mixmax
3. No ad blockers interfering with script execution

## Defense

Defensive measures and detection strategies:

- Scan stored templates for malicious patterns before rendering
- Use output encoding for all dynamic content in templates
- Monitor for unexpected JavaScript alerts or network requests from templates

## Objectives

1. Persist the XSS payload in the template
2. Execute arbitrary JavaScript upon rendering
3. Validate impact through observable effects like alerts

## Instructions

### Step 1: Save and View Template

**Context**: Commit changes and reload to activate the stored payload.

**Action**:
- Click the "Save" button in the template editor to store the changes.
- Exit the editor and navigate back to view the template list or preview the specific template.
- Upon loading the view, the Social Badges should render, executing the payload.

> Expect an alert box popping up with "1". In a real attack, this would run custom JS. Check browser developer tools for execution confirmation if alert is suppressed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[Execution]]
- [[stored-xss]]
