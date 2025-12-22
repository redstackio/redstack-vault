---
tags:
  - xss-execution
  - javascript
  - dom-injection
type: procedure
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:20.486Z'
sub_techniques: []
id: 679cd36f-e8dc-4be8-a527-8ed51d386896
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-Injected-XSS-Payload

## Summary

This procedure triggers the execution of the injected JavaScript via event handlers after the payload is inserted into Twitter's DOM.

## Description

With Referer validated, original_referer injects attributes like style=font-size:1000px and onmouseover=alert(0) directly. Victim interaction (mouse over, focus, etc.) fires events, executing arbitrary JS for alerts, cookie theft, or session hijacking.

## Requirements

1. Payload inserted in DOM
2. Victim interaction
3. No CSP blocking events

## Defense

Defensive measures and detection strategies:

- Implement strict HTML parsing and attribute validation
- Monitor for anomalous JS execution in browser console
- Use sandboxing for user-generated content

## Objectives

1. Trigger event handlers
2. Run malicious JS
3. Achieve impact like data exfil

## Instructions

### Step 1: DOM Insertion

**Context**: Payload applied on reload.

Observe style changes (e.g., large font).

### Step 2: Induce Interaction

**Context**: Fire events to execute.

Victim hovers or focuses element, running alert(0) or custom payload.

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

- [[xss-execution]]
