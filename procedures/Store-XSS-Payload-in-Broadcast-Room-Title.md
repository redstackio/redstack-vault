---
id: proc-store-xss-room-title-2024
tags:
  - xss
  - payload-storage
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/alert-xss-demo]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.523Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Store XSS Payload in Broadcast Room Title

## Summary

This procedure stores an executable JavaScript payload in the Chaturbate broadcast room title, leveraging the #roomtitle element for later retrieval and execution in a stored XSS attack.

## Description

In the context of exploiting Chaturbate's stored XSS vulnerability, the room title field is used to inject JavaScript code without sanitization. This payload is then referenced and evaluated via forged links in the chat header. The attack requires broadcaster access and targets victim browsers upon room access. Expected outcome is payload persistence in the DOM for exploitation.

## Requirements

1. Valid Chaturbate broadcaster account
2. Access to broadcast room setup interface
3. Web browser for testing

## Defense

Defensive measures and detection strategies:

- Sanitize room title inputs to remove or escape JavaScript code
- Implement Content Security Policy (CSP) to block inline javascript: URIs
- Monitor for anomalous room titles containing code-like strings

## Objectives

1. Persist XSS payload in room metadata
2. Ensure payload is retrievable via DOM selectors
3. Set up for chained execution without direct injection limits

## Instructions

### Step 1: Access Broadcast Setup

**Context**: Log in and navigate to create or edit a broadcast room to access the title field.

**Instructions**: Go to Chaturbate broadcaster dashboard and enter the room configuration.

### Step 2: Inject Payload into Room Title

**Context**: Set the title to the JavaScript payload, which will be stored in the #roomtitle element.

**Command** ([[commands/alert-xss-demo]]):

Set room title to: `alert('XSS by skavans at ' + document.domain)`

> This injects the alert payload into the title. Upon room load, it appears as text in the DOM element, ready for evaluation. Expected output: Title updated; inspect element to confirm storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/alert-xss-demo]]

## Tools Used


## Tags

- [[xss]]
- [[payload-storage]]
