---
tags:
  - origin-bypass
  - websocket
type: procedure
tools:
  - '[[tools/Process-Monitor]]'
  - '[[tools/Burp-Suite]]'
  - '[[tools/Request-Highlighter]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/websocket-seturldefaultbrowser-calc]]'
  - '[[commands/require-child-process-exec-calc]]'
platforms:
  - Windows
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 70cf871b-8619-4a13-8fbe-f7ab875fccc1
created_at: '2025-12-11T03:47:56.479Z'
updated_at: '2025-12-11T03:47:56.479Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Test WebSocket Server for Origin Validation

## Summary

This procedure tests the local WebSocket server for improper access control by attempting cross-origin connections and sending messages.

## Description

Connecting from an arbitrary webpage to ws://localhost:1235 and observing message processing confirms the lack of Origin header validation. This vulnerability allows command injection from any site.

## Requirements

1. Running PlayStation Now application
2. Browser and Burp Suite for WebSocket testing
3. Local access to port 1235

## Defense

Defensive measures and detection strategies:

- Implement strict Origin checks in WebSocket servers
- Monitor for unexpected WebSocket connections

## Objectives

1. Confirm cross-origin vulnerability
2. Verify server processes arbitrary messages
3. Escalate to command testing

## Instructions

### Step 1: Connect from Browser

**Context**: Load a webpage and attempt WebSocket connection.

Connect to ws://localhost:1235 and send test messages.

> Observe server response without Origin check.

### Step 2: Inspect with Burp

**Context**: Use Burp Suite to monitor the connection.

Proxy the WebSocket traffic and confirm no rejection based on origin.

> Successful message exchange indicates vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- #origin-bypass
- [[commands/websocket-seturl-example]]
