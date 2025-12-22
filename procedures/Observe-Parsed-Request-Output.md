---
tags:
  - verification
  - logging
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Node.js
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c3f67f52-ae49-4eff-b24c-a095e70a50ad
created_at: '2025-12-13T09:01:17.224Z'
updated_at: '2025-12-13T09:01:17.224Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe Parsed Request Output

## Summary

This procedure involves monitoring the Node.js server's console output to verify the success of the HTTP Request Smuggling exploit.

## Description

Check the logged headers and body to confirm that the parser misinterpreted the malformed header as including 'transfer-encoding: chunked', indicating successful smuggling.

## Requirements

1. Running Node.js server with logging
2. Previous steps completed
3. Console access

## Defense

Defensive measures and detection strategies:

- Log and alert on unexpected header formats
- Patch Node.js to enforce RFC7230

## Objectives

1. Validate exploitation
2. Confirm smuggling impact
3. Analyze parsed results

## Instructions

### Step 1: Check Server Logs

**Context**: Review console for parsed request details.

> Look for headers like { host: 'localhost:5000', 'x-abc': '', 'transfer-encoding': 'chunked' } and body 'A'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Node.js]]

## Tags

- [[verification]]
- [[logging]]
