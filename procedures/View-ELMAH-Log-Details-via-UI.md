---
tags:
  - session-extraction
  - pii-leak
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:30:47.140Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 53888ac4-d033-4854-b9c0-7af26bc7ab49
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
  - '[[Steal Web Session Cookie]]'
---
# View-ELMAH-Log-Details-via-UI

## Summary

This procedure uses the ELMAH UI to view detailed error information from a selected log, extracting HTTP requests, sessions, and cookies.

## Description

After listing logs, clicking 'Details' on an entry loads full error context, including request headers, POST data, cookies, and session tokens. This exposes sensitive elements like AUTH_PASSWORD for hijacking. No authentication is required, making it a direct path to data exfiltration.

## Requirements

1. Log list retrieved
2. Web browser for UI interaction
3. Log ID from previous step

## Defense

Defensive measures and detection strategies:

- Remove UI details from public endpoints
- Sanitize logs to exclude sensitive data
- Implement rate limiting on detail views

## Objectives

1. Extract full request details
2. Capture session cookies
3. Identify PII and credentials

## Instructions

### Step 1: Interact with Log UI

**Context**: From the log list page, select and view details of a log entry.

**Command** (Browser Action):
No command; use browser to click 'Details' on a log.

> Expected output: Page with full HTTP details, cookies, and error stack.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[session-extraction]]
- [[pii-leak]]
