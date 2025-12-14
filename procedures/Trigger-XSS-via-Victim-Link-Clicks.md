---
id: proc-trigger-xss-victim-clicks-2024
tags:
  - xss
  - execution-trigger
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/alert-xss-demo]]'
  - '[[commands/set-variable-b-roomtitle]]'
  - '[[commands/eval-jquery-text]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Malicious File]]'
updated_at: '2025-12-13T23:55:06.473Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Malicious File]]'
---
# Trigger XSS via Victim Link Clicks

## Summary

This procedure simulates victim interaction to execute the split XSS payload in Chaturbate, resulting in arbitrary JavaScript run and potential account takeover.

## Description

The victim clicks the first link to set the variable, then the second to eval the room title, exploiting the stored XSS. This grants attacker control over the victim's browser session, e.g., stealing tokens or manipulating the account.

## Requirements

1. Broadcast active with malicious links
2. Victim browser session
3. Prior payload setup complete

## Defense

Defensive measures and detection strategies:

- Educate users on not clicking suspicious links in chat
- Implement click-jacking protection and URI validation
- Monitor for eval() calls or anomalous alerts in client logs

## Objectives

1. Execute first payload part
2. Chain to second for full eval
3. Achieve JS execution for takeover

## Instructions

### Step 1: Click First Link

**Context**: Victim clicks the first app link to set `b`.

**Command** ([[commands/set-variable-b-roomtitle]]):

Click link from first app.

> Runs `b='#roomtitle';0`. Expected: Variable set silently.

### Step 2: Click Second Link

**Context**: Click second to execute stored payload.

**Command** ([[commands/eval-jquery-text]]):

Click link from second app.

> Runs `eval($(b).text())`, executing [[commands/alert-xss-demo]]. Expected: Alert pops, confirming XSS; extend to steal session.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Malicious File]]

### Sub-Techniques


## Commands Used

- [[commands/set-variable-b-roomtitle]]
- [[commands/eval-jquery-text]]
- [[commands/alert-xss-demo]]

## Tools Used


## Tags

- [[xss]]
- [[execution-trigger]]
