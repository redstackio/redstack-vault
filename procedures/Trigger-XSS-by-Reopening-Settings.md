---
tags:
  - trigger
  - xss
  - execution
  - web
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
id: 967df41f-1c4b-4cd9-bed1-304cf88044b6
created_at: '2025-12-14T17:32:01.949Z'
updated_at: '2025-12-14T17:32:01.949Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Reopening-Settings

## Summary

This procedure reloads the wallet settings to reflect and execute the stored XSS payload in the browser.

## Description

Reopening settings causes the server to return the unsanitized key name, rendering the HTML/JS. In the operator wallet web app, this executes arbitrary code in the victim's context.

## Requirements

1. Payload stored in a key
2. Same browser session
3. No CSP blocking execution

## Defense

Defensive measures and detection strategies:

- Sanitize outputs before rendering
- Implement strict CSP headers

## Objectives

1. Reflect stored payload
2. Execute JS in browser
3. Demonstrate impact

## Instructions

### Step 1: Close Settings

**Context**: Simulate normal navigation.

**Action**: Navigate away from or close the settings page.

> This clears the current view.

### Step 2: Reopen Settings

**Context**: Trigger reflection.

**Action**: Return to the wallet settings page.

> The page reloads, fetching and displaying stored data.

### Step 3: Observe Execution

**Context**: Validate XSS trigger.

**Action**: Look for the payload rendering (e.g., link appears or alert fires if JS).

> Arbitrary code runs; inspect console for JS errors or actions.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[trigger]]
- [[xss]]
- [[Execution]]
- [[web]]
