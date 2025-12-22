---
tags:
  - xss
  - verification
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 6dbceaaa-cdcc-4704-b5b8-a509c4a39b4f
created_at: '2025-12-14T03:16:30.904Z'
updated_at: '2025-12-14T03:16:30.904Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-Stored-XSS-Execution

## Summary

Confirm the stored payload executes JavaScript in vulnerable contexts like unencoded outputs and JSON responses when viewed.

## Description

After injection, retrieve and observe the profile in various rendering contexts to trigger XSS. For Vimeo, execution occurs in JS inputs, plain strings, and HTML-headed JSON, impacting viewers. Prerequisites: stored payload; outcomes: demonstrated arbitrary JS run.

## Requirements

1. Injected profile with payload
2. Ability to view as another user
3. Browser for JS alert testing

## Defense

Defensive measures and detection strategies:

- Encode all outputs contextually (e.g., JSON.stringify for JS)
- Implement strict CSP
- Monitor for JS errors or alerts in user sessions

## Objectives

1. Trigger execution in multiple contexts
2. Validate cross-user impact
3. Assess payload reliability

## Instructions

### Step 1: Retrieve Profile Content

**Context**: Load the updated profile page.

Visit the profile URL and inspect the rendered HTML/JS.

> Look for the payload in source, unstripped.

### Step 2: Test Execution Contexts

**Context**: Check JS, unencoded, and JSON outputs.

View in incognito or another account; observe alert() pop if successful. Test API responses for JSON with HTML headers.

> Execution confirms stored XSS viability.

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
