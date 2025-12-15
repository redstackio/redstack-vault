---
id: proc-002
tags:
  - airflow
  - user-assignment
  - authorization
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Apache Airflow
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:18.304Z'
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
# Assign-Restricted-Role-to-Test-User

## Summary

This procedure creates a test user in Apache Airflow and assigns the restricted 'roleA' to it, enabling simulation of a low-privilege account for vulnerability testing.

## Description

User management in Airflow allows admins to create accounts and link them to roles. Here, a user named 'test' is created and assigned 'roleA', which only permits reading the 'tutorial' DAG. This sets up the authenticated session needed to demonstrate the API bypass, where UI limits are enforced but API endpoints fail to validate permissions properly for wildcard requests.

## Requirements

1. Admin access to Airflow UI
2. Pre-created 'roleA' with restricted permissions
3. Airflow configured with user authentication

## Defense

Defensive measures and detection strategies:

- Monitor user creation logs for anomalous admin activity
- Implement role-based access reviews periodically
- Use RBAC auditing tools to detect over-privileged assignments

## Objectives

1. Provision a restricted test account
2. Confirm role linkage
3. Enable login for restriction verification

## Instructions

### Step 1: Navigate to User Management

**Context**: Log in as admin and go to Security > Users in the Airflow UI.

No command; use the web interface.

> Prepares for new user creation.

### Step 2: Create Test User

**Context**: Add a new user with minimal details.

No command; enter username 'test', set a password, and save.

> User 'test' is now provisioned but without roles.

### Step 3: Assign Role

**Context**: Link the restricted role to the user.

No command; edit the 'test' user and select 'roleA' from available roles.

> Save changes. Expected: User profile shows 'roleA' assignment.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- airflow
- user-assignment
