---
tags:
  - xss
  - execution
  - twitter
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
id: f23ab6be-2738-4142-8bb2-bdf8477b57be
created_at: '2025-12-14T03:16:14.479Z'
updated_at: '2025-12-14T03:16:14.479Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Previewing-Poll

## Summary

This procedure triggers the execution of the injected XSS payload by previewing the poll, demonstrating reflected execution in the creation interface and highlighting browser-specific mitigations.

## Description

Once the payload is injected into a poll option, previewing the poll causes the unsanitized input to be rendered as HTML in the preview pane, executing JavaScript if not blocked by CSP. In modern browsers like Chrome, CSP prevents execution, but in Internet Explorer 11, it succeeds due to limited CSP enforcement. This self-XSS allows arbitrary JS in the attacker's session, such as alerts or cookie access, but cannot affect other users.

## Requirements

1. Payload already injected from prior step
2. Web browser (test in IE11 for full execution)
3. Active poll creation session

## Defense

Defensive measures and detection strategies:

- Strengthen CSP to disallow unsafe-inline and eval
- Sanitize outputs during rendering with HTML entity encoding
- Log and alert on XSS payload patterns in user inputs

## Objectives

1. Execute JavaScript via reflected input in preview
2. Assess CSP effectiveness across browsers
3. Confirm self-XSS isolation

## Instructions

### Step 1: Activate Preview

**Context**: Use the preview function to render the poll with the injected payload.

In the poll creation interface, click the "Preview" or equivalent button to display the poll layout.

### Step 2: Observe Execution

**Context**: Monitor for payload execution in the rendered preview.

Watch for an alert popup in vulnerable browsers; in modern ones, check developer console for CSP violation messages.

> Expected: alert(1) executes in IE11, confirming JS injection success.

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
