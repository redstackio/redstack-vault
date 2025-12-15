---
id: proc-uuid-3
tags:
  - xss
  - execution
  - admin-context
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:57.145Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Viewing-Menu

## Summary

This procedure triggers the stored XSS by rendering the vulnerable menu titles in the Shopify Admin, executing injected JavaScript and enabling admin-level manipulations.

## Description

After payload injection, viewing the menu causes the unescaped titles to render HTML/JS directly in the admin browser context. This exploits the rendering flaw, executing onload events like prompts or more destructive actions (e.g., deleting links). Targeted at Shopify's web admin, it requires the prior stored payload and an active session. Outcomes include arbitrary script execution with admin privileges.

## Requirements

1. Stored XSS payload from previous injection
2. Active admin session
3. Browser rendering the admin page

## Defense

Defensive measures and detection strategies:

- Sanitize all stored inputs before rendering in admin templates
- Log and alert on unexpected JavaScript execution or DOM manipulations in admin sessions
- Use browser developer tools to monitor for anomalous onload events

## Objectives

1. Execute JavaScript in admin context
2. Demonstrate impact through actions like prompt or deletions
3. Escalate to further admin exploits

## Instructions

### Step 1: Navigate to Menu View

**Context**: Load the page that renders the stored titles to trigger execution.

From the admin dashboard, go to 'Online Store' > 'Navigation' and select the modified menu to view it.

> The page renders, and the payload executes immediately via SVG onload.

### Step 2: Observe and Extend Execution

**Context**: Confirm trigger and perform follow-on actions.

Watch for the prompt(1) alert; replace with scripts for deletions, e.g., via console or chained payload.

> Alert appears, confirming control; menu links can now be manipulated.

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
- [[admin-context]]
