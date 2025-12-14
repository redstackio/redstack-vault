---
tags:
  - xss
  - payload-injection
  - svg-xss
type: procedure
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
updated_at: '2025-12-14T03:46:37.299Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 95202a1f-c908-4944-afca-49b341172ef3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-SVG-XSS-Payload-into-Campaign-Name

## Summary

This procedure details the injection of a malicious SVG-based JavaScript payload into the lemlist Campaign Name field, exploiting the lack of input sanitization to store executable code that can later be triggered in user-facing interfaces.

## Description

The lemlist application fails to properly escape or sanitize user input in the Campaign Name during storage and rendering in popups. By closing an existing HTML tag and injecting an SVG element with an onload handler, the attacker stores arbitrary JavaScript. When a victim (including the attacker in testing) interacts with related features, the payload executes in the browser context, allowing actions like displaying alerts or stealing cookies via document.cookie. Prerequisites include an active session from the setup procedure.

## Requirements

1. Authenticated session in lemlist (from prior access)
2. Access to the campaign creation/editing form
3. Knowledge of basic HTML/SVG for payload crafting

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding (e.g., &lt; for <)
- Use Content Security Policy (CSP) to restrict inline scripts and SVG execution
- Log and monitor unusual input patterns in campaign names, such as script tags

## Objectives

1. Store the XSS payload without triggering validation errors
2. Ensure the payload survives storage and retrieval
3. Set up for execution in subsequent interactions

## Instructions

### Step 1: Enter the Payload

**Context**: Craft and input the payload to bypass any partial sanitization.

In the Campaign Name field, type: `/><svg src=x onload=confirm(document.domain);>`.

> This closes any open tag (e.g., input) and injects an SVG that loads a non-existent src, triggering onload to execute confirm() with the domain.

### Step 2: Save the Campaign

**Context**: Persist the payload in the application's database.

Click 'Save' or 'Create Campaign' to submit the form.

> The campaign saves, and the name appears in the list with the injected content, though visually altered.

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
- [[stored-xss]]
- [[JavaScript]]
