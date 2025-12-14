---
id: proc-zomato-xss-detect-3
tags:
  - xss
  - detection
  - zomato
type: procedure
tools:
  - '[[tools/XSS-Hunter]]'
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
updated_at: '2025-12-14T17:30:58.379Z'
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
# Detect XSS Execution via XSS Hunter Callback

## Summary

This procedure detects and verifies the successful execution of a Blind XSS payload by receiving a callback from the XSS Hunter service, confirming script loading in the target admin context.

## Description

XSS Hunter acts as an external beacon, capturing details like IP, user-agent, and timestamp when the script executes. This confirms the vulnerability's impact, such as potential session hijacking or data exfiltration in the admin's browser. The procedure focuses on analyzing the callback for context validation.

## Requirements

1. Active XSS Hunter hunt with payload deployed
2. Prior steps completed (injection and monitoring)
3. Ability to interpret callback data for confirmation

## Defense

Defensive measures and detection strategies:

- Block outbound requests to known XSS callback domains (e.g., xss.ht)
- Implement client-side script blocking in admin interfaces
- Regularly scan admin logs for external script executions

## Objectives

1. Receive confirmation of payload execution
2. Analyze context to assess impact (e.g., admin UA)
3. Document for reporting or further exploitation

## Instructions

### Step 1: Receive Callback

**Context**: Observe the incoming notification from XSS Hunter upon execution.

Check the XSS Hunter dashboard or email notifications for a new hit on your subdomain.

> Expected output: Details including request headers, payload, and execution time.

### Step 2: Verify Context

**Context**: Confirm the execution occurred in the admin dashboard.

Review callback data: Look for indicators like internal IP ranges, admin-specific user-agents, or referrer URLs pointing to Zomato's backend.

> Expected output: Validation that the hit matches the target context, not user-side.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XSS-Hunter]]

## Tags

- xss
- detection
- callback
