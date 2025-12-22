---
id: proc-003
tags:
  - airflow
  - ui-verification
  - authorization
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Apache Airflow
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:18.289Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-UI-Restrictions-as-Test-User

## Summary

This procedure logs in as the restricted 'test' user to confirm that the Airflow UI enforces DAG-specific permissions, displaying only the 'tutorial' DAG and blocking access to others.

## Description

The Airflow web UI applies role-based restrictions correctly, unlike the vulnerable API. By logging in and inspecting the DAGs view, this verifies the setup for the bypass attack, ensuring the exploit targets a genuine permission gap. No task instances from other DAGs should be visible, highlighting the API's failure to enforce the same checks.

## Requirements

1. Created 'test' user with 'roleA'
2. Access to Airflow UI on port 8080
3. Valid credentials for 'test'

## Defense

Defensive measures and detection strategies:

- Log UI access attempts and correlate with role permissions
- Use session monitoring to detect unusual navigation patterns
- Ensure consistent permission enforcement across UI and API

## Objectives

1. Confirm restricted DAG visibility
2. Validate no cross-DAG access in UI
3. Baseline for API comparison

## Instructions

### Step 1: Log In as Test User

**Context**: Access the login page and authenticate.

No command; enter 'test' credentials at http://target:8080/login.

> Successful login redirects to dashboard.

### Step 2: Inspect DAGs View

**Context**: Navigate to the DAGs section.

No command; click 'DAGs' in the sidebar.

> Expected: Only 'tutorial' DAG listed; others hidden or access denied.

### Step 3: Check Task Instances

**Context**: Attempt to view task instances for visible and invisible DAGs.

No command; select 'tutorial' and try accessing others via URL manipulation.

> Expected: No task instances from non-'tutorial' DAGs visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- airflow
- ui-verification
