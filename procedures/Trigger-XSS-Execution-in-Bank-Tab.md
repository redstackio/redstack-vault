---
tags:
  - xss
  - execution
  - bank-tab
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
detection_risk: medium
sub_techniques: []
id: c7979e61-c5a2-4410-b0e9-ba4f0b99abf0
created_at: '2025-12-14T03:16:25.386Z'
updated_at: '2025-12-14T03:16:25.386Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-in-Bank-Tab

## Summary

This procedure outlines triggering the execution of a stored XSS payload from account settings within the Moneybird Bank tab, where the vulnerable fields are rendered, leading to JavaScript execution in a high-privilege financial context.

## Description

Once the payload is stored in account settings, accessing the Bank tab causes the application to load and render the unsanitized data, executing the injected script. This can occur for the account owner or shared users, compromising the session during banking operations. The technique relies on the application's failure to escape output in the Bank tab's UI components.

## Requirements

1. Payload already injected via prior procedure
2. Access to the Bank tab with the affected account
3. Browser console open for monitoring execution

## Defense

Defensive measures and detection strategies:

- Apply context-aware escaping in all UI renders (e.g., HTML, JS contexts)
- Audit rendering paths for stored data
- Log and alert on script execution attempts via CSP violations

## Objectives

1. Render the vulnerable field in the Bank tab
2. Execute the JavaScript payload
3. Confirm impact in a sensitive area

## Instructions

### Step 1: Navigate to Bank Tab

**Context**: From the dashboard, access the Bank tab to load financial data intertwined with account settings.

Use web navigation to `/bank` or equivalent tab.

> Expected: Page loads with account details, including injected fields.

### Step 2: Observe Execution

**Context**: The payload executes automatically upon render.

Monitor browser console for script run (e.g., alert or fetch).

> Expected: Alert pops or network tab shows exfiltration request.

### Step 3: Validate in Console

**Context**: Use dev tools to inspect if DOM manipulation occurred.

Check console for errors or custom logs from payload.

> Expected: Evidence of JS execution, like modified elements.

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
