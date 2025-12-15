---
id: proc-uuid-6
name: Observe Server Crash after Sufficient Requests
tags:
  - dos
  - rails
  - crash
type: procedure
tools:
  - '[[tools/Puma]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/observe-server-crash-log]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:36.506Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Observe Server Crash after Sufficient Requests

## Summary

This procedure monitors server logs for the stack overflow error after repeated requests, confirming the DoS impact with Puma entering a zombie state.

## Description

After ~989 requests, the recursive Rack::BodyProxy in the mutated response causes SystemStackError in Rack::Sendfile during handling, crashing the server and denying service.

## Requirements

1. Ongoing request flood
2. Access to server logs (stdout)
3. Puma running

## Defense

Defensive measures and detection strategies:

- Enable stack trace logging and alert on SystemStackError
- Use process supervisors to restart crashed servers
- Audit middleware for proxy wrapping

## Objectives

1. Confirm mutation leads to overflow
2. Verify application downtime
3. Observe potential data leakage

## Instructions

### Step 1: Monitor Logs for Crash

**Context**: Watch for the fatal error in Puma logs indicating success.

**Command** ([[commands/observe-server-crash-log]]):
```bash
# Observe in real-time: tail -f log/production.log or stdout
```

> Expected output: Entry like "2021-08-11 13:23:04 -0500 Rack app ... #<fatal: machine stack overflow in critical region>". Server unresponsive.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/observe-server-crash-log]]

## Tools Used

- [[tools/Puma]]

## Tags

- dos
- rails
- crash
