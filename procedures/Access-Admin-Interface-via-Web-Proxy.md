---
tags:
  - proxy-access
  - internal-pivoting
type: procedure
tools:
  - '[[tools/download.py]]'
  - '[[tools/grep]]'
  - '[[tools/GPU]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
platforms:
  - SSL VPN
techniques:
  - '[[Non-Standard Port]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 721cce7e-fef4-4646-82a3-c7a42e012dbc
created_at: '2025-12-11T06:10:40.278Z'
updated_at: '2025-12-11T06:10:40.278Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0005]]'
mitre_techniques:
  - '[[T1571]]'
---
# Access Admin Interface via Web Proxy

## Summary

This procedure leverages the VPN's web proxy functionality to access the internal admin interface after authentication.

## Description

Once authenticated, the VPN allows proxying to internal URLs like https://0/admin/, providing access to administrative controls for further exploitation.

## Requirements

1. Successful authentication to the VPN
2. Knowledge of internal admin path
3. Active VPN session

## Defense

Defensive measures and detection strategies:

- Restrict proxy access to admin interfaces
- Log and alert on internal admin access via VPN

## Objectives

1. Reach admin dashboard
2. Prepare for privilege escalation
3. Enable command injection

## Instructions

### Step 1: Login and Proxy to Admin

**Context**: Use the VPN proxy to navigate internally.

After login, access https://0/admin/ via the web proxy function.

### Step 2: Verify Access

**Context**: Confirm admin interface functionality.

Interact with the dashboard to ensure full access.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Non-Standard Port]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[proxy-access]]
- [[internal-pivoting]]
