---
id: proc-submit-observe-self-xss
tags:
  - xss
  - execution
  - self-xss
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
updated_at: '2025-12-14T00:11:09.454Z'
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
# Submit-and-Observe-Self-XSS-Execution

## Summary

This procedure submits the injected HTML comment and observes the resulting one-time script execution, confirming the self-XSS vulnerability in the Deck app.

## Description

Upon submission, the comment renders the injected HTML, executing scripts only in the attacker's browser session. This is due to improper server-side rendering of comments. The execution is non-persistent, disappearing on refresh or reload, limiting impact to self-inflicted actions like local data exfiltration.

## Requirements

1. Injected payload in comments field
2. Active session in the attacker's browser
3. Ability to inspect page source and console

## Defense

Defensive measures and detection strategies:

- Escape HTML on server-side rendering
- Use strict output encoding in templates
- Log rendering errors or unusual DOM manipulations

## Objectives

1. Trigger payload execution via submission
2. Verify self-only impact
3. Document execution behavior

## Instructions

### Step 1: Submit the Comment

**Context**: Finalize the injection by sending the comment.

Click the "Send" or submit button in the comments interface.

**Expected Output**: Comment appears in the list.

### Step 2: View and Trigger Execution

**Context**: Reload or interact to render the payload.

Click into the card comments or refresh the page to view the comment.

**Expected Output**: Styled link renders; base target may redirect or execute on click.

### Step 3: Inspect for Execution

**Context**: Confirm script behavior.

Open browser dev tools (F12) and check console/network for execution traces.

**Expected Output**: JavaScript runs one-time; no persistence on reload.

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
- [[self-xss]]
