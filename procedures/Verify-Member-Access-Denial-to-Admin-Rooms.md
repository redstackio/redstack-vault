---
tags:
  - access-control
  - verification
  - 8x8
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:18.095Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 0ceb23b3-032f-48db-926f-ea65b67658ac
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-Member-Access-Denial-to-Admin-Rooms

## Summary

This procedure verifies that member users in the 8x8 platform cannot access the admin rooms management section, confirming the presence of access controls that can later be bypassed.

## Description

In the 8x8 admin panel, member users are restricted from privileged areas like rooms management. This step involves logging in as a member and attempting access to establish the baseline denial, which is crucial for demonstrating the impact of the subsequent bypass via calendar auth.

## Requirements

1. Valid member user credentials for 8x8 login
2. Browser access to admin.8x8.vc
3. Separate admin session for contrast (optional but recommended)

## Defense

Defensive measures and detection strategies:

- Implement strict role-based access control (RBAC) checks on all endpoints
- Log and alert on unauthorized access attempts to admin sections
- Use session validation to prevent cross-role manipulations

## Objectives

1. Confirm member role limitations
2. Baseline for bypass validation
3. Expected access denial outcome

## Instructions

### Step 1: Login as Member and Attempt Access

**Context**: Authenticate as a member user and navigate to the restricted admin rooms area to trigger denial.

No specific command; use browser:

- Log in to https://admin.8x8.vc with member credentials
- Navigate to https://admin.8x8.vc/#/rooms

> Attempting access should result in an access denied error (e.g., 403), confirming restrictions.

### Step 2: Document the Denial

**Context**: Capture evidence of the denial for reporting.

Screenshot or log the error message indicating insufficient permissions.

> Success: Clear denial without visibility into rooms management.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery (verifying account permissions)

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[access-control]]
- [[verification]]
