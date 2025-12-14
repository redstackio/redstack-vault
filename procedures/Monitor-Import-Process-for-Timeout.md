---
tags:
  - timeout-exploitation
  - monitoring
type: procedure
tools:
  - '[[tools/Custom-Python-HTTP-Server]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Python]]'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 595dc571-9ef5-496b-a449-331026b103ba
created_at: '2025-12-14T17:23:28.008Z'
updated_at: '2025-12-14T17:23:28.008Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Monitor-Import-Process-for-Timeout

## Summary

This procedure waits for the Concrete CMS import to timeout after processing delayed requests, ensuring the temporary PHP file remains accessible post-error.

## Description

By submitting multiple delaying URLs, the import exceeds the 120-second PHP execution limit, triggering an error and skipping cleanup in VolatileDirectory::__destruct. Monitoring server logs confirms request processing.

## Requirements

1. Active malicious server logging requests
2. Timer or clock for 120-second wait
3. Access to CMS interface for error confirmation

## Defense

Defensive measures and detection strategies:

- Implement strict execution time limits with forced cleanup
- Alert on import timeouts or excessive remote requests
- Rate-limit file manager operations

## Objectives

1. Confirm timeout error in CMS
2. Verify all delay requests processed via logs
3. Ensure temp file persistence

## Instructions

### Step 1: Initiate Wait

**Context**: Start timing the import process.

No command; begin countdown from import submission.

> Process runs for ~120 seconds.

### Step 2: Check for Error and Logs

**Context**: Observe CMS response and server logs.

No command; refresh CMS page and tail server logs.

> CMS shows timeout error; logs show 20+ /stuck requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-Python-HTTP-Server]]

## Tags

- [[timeout-exploitation]]
- [[php]]
