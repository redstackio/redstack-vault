---
id: proc-914331-login-user
tags:
  - authentication
  - web
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:29.456Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-as-Team-Member-User

## Summary

This procedure authenticates a team member with 'USER' role to the Outpost application, enabling access to the notes API within the team context for IDOR exploitation.

## Description

To demonstrate the IDOR, switch to a 'USER' role account in the same team as the owner. This allows the attacker to perform note operations that can be intercepted and modified. The login establishes a session with limited privileges, highlighting the lack of per-note authorization in the API.

## Requirements

1. Valid 'USER' role credentials for the same team
2. Access to the web login interface
3. Session management (e.g., cookies or tokens)

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for all roles
- Monitor login patterns for anomalous team access

## Objectives

1. Gain 'USER' session in the target team
2. Confirm access to notes functionality
3. Set up for request interception

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the authentication endpoint.

Open the Outpost login page in a browser and enter team member 'USER' credentials.

### Step 2: Verify Session

**Context**: Confirm successful login and team context.

After login, navigate to the notes section and attempt to create or view a personal note to validate the session and team membership.

**Expected Output**: Dashboard or notes interface loads with 'USER' permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[web]]
