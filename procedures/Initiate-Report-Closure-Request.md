---
tags:
  - request-interception
  - hackerone
  - report-closure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:46.974Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
id: a03a4cbb-3f88-4e82-b42b-05e6b131710a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Report-Closure-Request

## Summary

This procedure generates and captures a legitimate HTTP POST request for closing a report as a duplicate in the sandbox program, setting the stage for modification.

## Description

Using User B's session, select a test report and trigger the 'Close as duplicate' action to capture the /reports/bulk request. This request includes parameters like original_report_id (initially a sandbox ID), which will be targeted for tampering. Requires proxy interception for capture.

## Requirements

1. Authenticated User B in sandbox with a test report
2. Proxy tool (e.g., Burp Suite) configured for request interception
3. Knowledge of HTTP request structure

## Defense

Defensive measures and detection strategies:

- Rate-limit bulk endpoint requests
- Log all closure actions with user and program context
- Validate session tokens on sensitive actions

## Objectives

1. Capture baseline closure request
2. Identify modifiable parameters
3. Ensure request is replayable

## Instructions

### Step 1: Select Test Report

**Context**: Choose a report to close for request generation.

As User B, navigate to the sandbox reports list, open a test report, and click 'Close Report' > 'Duplicate'.

> Expected output: UI prompts for duplicate details; request prepares to send.

### Step 2: Intercept Request

**Context**: Capture the POST before it reaches the server.

With proxy active, proceed with the closure action to intercept the request to /reports/bulk.

> Expected output: Raw HTTP POST visible, including form-encoded body with original_report_id.

### Step 3: Analyze Parameters

**Context**: Review for exploitation points.

Examine the request: note report_ids[], original_report_id, CSRF token, and cookies.

> Expected output: Parameters confirmed; request paused for modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- request-interception
- report-closure
