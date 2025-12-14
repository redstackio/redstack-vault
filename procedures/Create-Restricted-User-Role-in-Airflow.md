---
id: proc-001
tags:
  - airflow
  - role-creation
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
updated_at: '2025-12-14T17:30:18.308Z'
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
# Create-Restricted-User-Role-in-Airflow

## Summary

This procedure creates a custom restricted role in Apache Airflow by modifying the default User role to limit access to only reading the 'tutorial' DAG, setting up the conditions for testing authorization bypass.

## Description

In Apache Airflow, roles control user permissions on DAGs and resources. This procedure simulates a least-privilege scenario by creating 'roleA' that removes general DAG read/delete/edit permissions and adds specific read access to the 'tutorial' DAG. It requires admin access and is a prerequisite for exploiting the API bypass in versions before 2.7.2. The outcome establishes a controlled environment where UI restrictions are enforced, but API vulnerabilities can be tested.

## Requirements

1. Administrative access to Airflow web interface (port 8080)
2. Existing Airflow installation with default roles
3. Knowledge of Airflow's permission model

## Defense

Defensive measures and detection strategies:

- Regularly audit role permissions via Airflow's security manager
- Enable logging for role modifications and monitor for unauthorized changes
- Upgrade to Airflow 2.7.2+ to patch API bypass

## Objectives

1. Create a role with minimal permissions for testing
2. Ensure UI enforces DAG-specific access
3. Prepare for API exploitation validation

## Instructions

### Step 1: Access Admin Interface

**Context**: Log in as an admin to the Airflow UI and navigate to Security > Roles.

No command required; use the web interface to select and copy the default 'User' role.

> Copying creates a base for modification without altering production roles.

### Step 2: Modify Permissions

**Context**: Remove broad permissions and add specific DAG access to restrict the role.

No command; in the role editor:
- Remove 'can read on DAGs', 'can delete on DAGs', 'can edit on DAGs'
- Add 'can read on DAG:tutorial'

> Save as 'roleA'. This limits visibility to only the 'tutorial' DAG in the UI.

### Step 3: Verify Role Creation

**Context**: Confirm the role is active and permissions are applied correctly.

No command; check the Roles list in admin panel.

> Expected: 'roleA' listed with only 'can read on DAG:tutorial' permission.

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
- role-creation
