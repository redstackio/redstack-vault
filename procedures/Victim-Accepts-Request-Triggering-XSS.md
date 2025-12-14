---
tags:
  - xss
  - execution
  - acceptance
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
updated_at: '2025-12-14T03:15:35.732Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ddfe43d6-9472-46d2-a3c5-3c03f194d9e9
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Victim-Accepts-Request-Triggering-XSS

## Summary

This procedure triggers the stored XSS by having the victim accept the authorization request, where the x:confirm parameter reflects the unsanitized username, executing the payload.

## Description

On the requests page, clicking 'Accept' processes the request via a parameter (x:confirm) that echoes the username without encoding, parsing the script tag and executing JavaScript in the victim's browser. This can lead to alerts, cookie theft, or keylogging. Prerequisites: Loaded requests page; outcomes: Immediate payload execution.

## Requirements

1. Victim on requests page with pending request
2. No CSP blocking inline scripts
3. Interactive browser session

## Defense

Defensive measures and detection strategies:

- Validate and encode parameters like x:confirm server-side
- Use strict CSP to block unsafe-inline
- Detect JavaScript errors or unexpected DOM changes client-side

## Objectives

1. Simulate acceptance action
2. Trigger reflection in x:confirm
3. Execute arbitrary JavaScript

## Instructions

### Step 1: Locate the Request

**Context**: Identify the attacker's pending authorization.

On https://mobilevikings.com/account/requests/, find the request from the attacker.

### Step 2: Click Accept

**Context**: Initiate the vulnerable interaction.

Press the 'Accept' button, which submits via x:confirm including the username.

> The parameter reflects the payload, causing <script> to execute.

### Step 3: Observe Execution

**Context**: Verify XSS firing.

Payload runs, e.g., alert(1) pops up or network request to attacker server.

**Expected Output**: Browser alert or console log of execution.

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
- [[web]]
