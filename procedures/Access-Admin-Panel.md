---
id: proc-bmc-admin-access-2024
tags:
  - privilege-escalation
  - admin-access
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:58.713Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access Admin Panel

## Summary

With the authentication bypassed, this procedure navigates to and confirms full admin privileges within the BMC Remedy AR System, allowing control over tickets, users, and permissions.

## Description

Post-bypass, the session inherits admin roles due to flawed redirect handling. This enables viewing/modifying the ticket database, altering user info, and changing permissions. Builds on prior steps; outcomes include unrestricted access to sensitive admin functions in the DoD ITSM environment.

## Requirements

1. Bypassed session active.
2. Familiarity with BMC Remedy UI navigation.
3. Target supports admin console exposure.

## Defense

Defensive measures and detection strategies:

- Role-Based Access Control (RBAC) with server-side enforcement, not reliant on client params.
- Audit admin access logs for anomalies (e.g., logins from non-admin IPs or sudden role elevations).

## Objectives

1. Verify and utilize admin privileges.
2. Enable data manipulation capabilities.
3. Prepare for PII extraction.

## Instructions

### Step 1: Navigate to Admin Sections

**Context**: Use the bypassed session to reach admin areas.

**Action** (UI Navigation):

From the dashboard, select admin tools or forms.

> Admin panels load fully, showing options like user management.

### Step 2: Test Privileges

**Context**: Confirm escalation by attempting restricted actions.

**Action** (Function Test):

Try editing a sample ticket or viewing user lists.

> Expected: Changes save without permission errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- privilege-escalation
- admin-access
