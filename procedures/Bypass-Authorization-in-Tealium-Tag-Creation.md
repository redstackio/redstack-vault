---
id: proc-uuid-1
tags:
  - authorization-bypass
  - access-control
  - tealium
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:44.461Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Authorization in Tealium Tag Creation

## Summary

This procedure exploits the lack of authorization checks in Tealium's tag creation interface, allowing attackers to create tags for accounts they do not own, setting the stage for content injection.

## Description

Tealium's tag management system fails to validate if the authenticated user has permissions for the specified account during tag creation. An attacker with any valid Tealium login can specify an unauthorized account ID (e.g., Uber's) and proceed, enabling downstream attacks like XSS. This targets web-based tag management platforms integrated with sites like Uber that load utag.js.

## Requirements

1. Valid Tealium account credentials (any level)
2. Knowledge of target account ID (e.g., from reconnaissance or leaks)
3. Web browser access to Tealium's interface

## Defense

Defensive measures and detection strategies:

- Implement strict authorization checks for account-specific operations
- Log and monitor tag creation attempts with account ID mismatches
- Use role-based access control (RBAC) to limit cross-account actions

## Objectives

1. Access tag creation for unauthorized accounts
2. Confirm bypass without triggering alerts
3. Prepare for payload injection

## Instructions

### Step 1: Authenticate to Tealium

**Context**: Log in to establish a session, providing the foundation for the bypass.

Navigate to the Tealium login page and enter valid credentials.

> Successful login redirects to the dashboard without errors.

### Step 2: Navigate to Tag Creation

**Context**: Access the interface where authorization is not enforced.

From the dashboard, go to the "Tags" section and select "Create New Tag." Specify the target account ID in the configuration fields (e.g., via URL parameter or form input like account=uber-account-id).

> The form accepts the input without validation, allowing progression.

### Step 3: Verify Bypass

**Context**: Test if the tag can be created for the unauthorized account.

Attempt to save a benign tag configuration and observe the response.

> Success is indicated by no authorization error and tag listing under the target account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authorization-bypass
- tealium
- web-exploit
