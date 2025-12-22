---
tags:
  - xss
  - trigger
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 45275268-3d06-4077-879f-5c60fcf940f4
created_at: '2025-12-14T03:15:47.181Z'
updated_at: '2025-12-14T03:15:47.181Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Viewing-Attacker-Info

## Summary

This procedure triggers the stored XSS by having the victim click 'Show information' on the attacker's user in the chat module, rendering the malicious full name and executing the injected JavaScript.

## Description

In the chat information panel, the attacker's full name is inserted into HTML without proper escaping, allowing the script tag to execute in the victim's browser context on the Nextcloud domain. This can lead to arbitrary JS execution, such as alerting the domain or stealing session cookies via document.cookie access.

## Requirements

1. Victim in chat module with attacker visible in user list
2. Injected payload from prior step
3. Browser supporting JavaScript execution

## Defense

Defensive measures and detection strategies:

- Sanitize all user data in chat UI with HTML entity encoding
- Implement XSS auditors or WAF rules for script tags
- Monitor browser console for unexpected script executions

## Objectives

1. Render the unsanitized full name
2. Execute the injected JavaScript
3. Achieve client-side impact like session theft

## Instructions

### Step 1: Select Attacker User

**Context**: Locate the attacker in the chat user interface.

In the chat module, find the attacker in the participant or user list.

> Hover or select the user entry.

### Step 2: Show Information

**Context**: Trigger the profile display containing the payload.

Click the 'Show information' button or link for the attacker.

> The information panel opens, rendering the full name HTML.

### Step 3: Observe Execution

**Context**: Confirm XSS payload runs in victim's browser.

Watch for the alert popup displaying the document domain.

> Expected: Alert box with 'nextcloud.example.com' or similar, confirming execution.

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
- [[trigger]]
- [[nextcloud]]
