---
id: acronis-replay-cross-tenant-001
tags:
  - session-replay
  - idor-exploit
  - data-destruction
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
updated_at: '2025-12-14T17:28:28.691Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Destruction]]'
---
# Replay-Recovery-Request-with-Cross-Tenant-Session-Cookie

## Summary

This procedure modifies and replays an intercepted Acronis recovery API request using a session cookie from another tenant, exploiting IDOR to execute destructive actions on unauthorized machines.

## Description

Building on intercepted requests, this targets the lack of authorization checks on parameters in Acronis APIs. By swapping the session cookie, an attacker can run recovery plans across tenants, overwriting data on victim machines. Requires a valid target session cookie and precise parameter retention.

## Requirements

1. Intercepted request from prior procedure
2. Valid X-Apigw-Session cookie from target organization
3. Burp Suite Repeater for request modification and sending

## Defense

Defensive measures and detection strategies:

- Validate tenant ownership for all machineId and planId parameters
- Implement session binding to specific tenants
- Alert on cross-tenant API calls and monitor for data overwrite events

## Objectives

1. Bypass tenant boundaries via session manipulation
2. Execute recovery plan on unauthorized machine
3. Achieve data destruction through overwrite

## Instructions

### Step 1: Obtain Target Session

**Context**: Acquire credentials for the victim tenant to get a session cookie.

Login to target Acronis account in a separate browser/session to capture X-Apigw-Session via Burp or dev tools.

> Cookie value extracted.

### Step 2: Modify Request in Repeater

**Context**: Update the intercepted request for cross-tenant use.

In Burp Repeater, paste the POST request, replace X-Apigw-Session with target cookie, adjust machineId to victim's UUID if needed.

> Request updated.

### Step 3: Send and Verify Execution

**Context**: Replay to trigger the unauthorized recovery.

Click Send and check response.

> 200 OK with execution details; monitor target machine for overwrite.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Impact]] Impact

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Data Destruction]] Data Destruction

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- session-replay
- idor-exploit
- data-destruction
