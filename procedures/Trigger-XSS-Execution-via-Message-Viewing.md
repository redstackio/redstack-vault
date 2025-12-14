---
id: p3c4d5e6-g7h8-9012-cdef-3456789012
tags:
  - xss-execution
  - session-theft
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:34.345Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-via-Message-Viewing

## Summary

This procedure sends the injected message to the victim and triggers JavaScript execution when they view it, allowing arbitrary code run in their browser for data exfiltration.

## Description

Once sent, the message's unsanitized content is rendered in the victim's inbox view, executing the embedded script. This can steal session cookies, perform keylogging, or redirect, as evidenced by alert executions in the report.

## Requirements

1. Composed message with XSS payload
2. Victim's active ok.ru session
3. Attacker monitoring for execution confirmation

## Defense

Defensive measures and detection strategies:

- Sanitize all rendered user content
- Implement strict XSS filters and CSP headers
- Log and alert on script execution attempts in browser consoles

## Objectives

1. Deliver payload to victim's inbox
2. Execute JavaScript on view
3. Collect stolen data like cookies

## Instructions

### Step 1: Send the Message

**Context**: Transmit the payload to the target.

In the messaging interface, enter the victim's username and click 'Send'.

> Expected: Message delivered to inbox without blocks.

### Step 2: Victim Views and Executes

**Context**: Wait for victim interaction to trigger.

When the victim opens the message, the payload executes automatically in their browser.

> Expected: JavaScript runs, e.g., alert popup or console log showing cookie access.

### Step 3: Verify Exploitation

**Context**: Confirm success via observed effects.

Use developer tools or payload callbacks to verify execution, such as sending stolen data to an attacker-controlled server.

> Expected: Data exfiltration or visual confirmation like alerts.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[code-execution]]
