---
id: proc-001
tags:
  - user-creation
  - access-control
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:47.296Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Low-Permission-User-in-HackerOne-Organization

## Summary

This procedure sets up a low-privilege user in a HackerOne organization with multiple programs, assigning them to a group that restricts access to only one program, enabling testing of API access controls against UI permissions.

## Description

In the context of testing HackerOne's access controls, create a new user and a custom group with permissions limited to a single program (e.g., askcmsakmdfksqa_h1r). Assign the user to this group and verify that the UI enforces these restrictions. This isolates the user for subsequent API exploitation, highlighting discrepancies between UI and API enforcement. Prerequisites include admin access to the organization.

## Requirements

1. Administrative access to HackerOne organization settings
2. Organization must have at least two programs (e.g., askcmsakmdfksqa_h1r and askcmsakmdfksqa_h1b)
3. Web browser for UI navigation

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) consistently across UI and API
- Audit user and group creations in organization logs
- Monitor for anomalous user assignments to low-perm groups

## Objectives

1. Establish a controlled low-privilege environment
2. Verify UI access restrictions as baseline
3. Prepare for API key generation

## Instructions

### Step 1: Add New User

**Context**: Navigate to organization user management to create a test user.

Access https://hackerone.com/organizations/askcmsakmdfksqa_demo/settings/users and add a new user with basic details.

### Step 2: Create Low-Permission Group

**Context**: Define a group with access only to the authorized program.

Create a group with limited permissions specifically for program askcmsakmdfksqa_h1r.

### Step 3: Assign User to Group

**Context**: Restrict the user's scope to the single program.

Assign the new user to the low-permission group, ensuring access only to askcmsakmdfksqa_h1r.

### Step 4: Verify Access

**Context**: Confirm UI enforcement of permissions.

Log in as the new user and verify they can only see askcmsakmdfksqa_h1r in the UI.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- user-creation
- access-control
- hackerone
