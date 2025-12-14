---
tags:
  - jenkins
  - script-console
  - access-control
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
updated_at: '2025-12-14T17:31:52.709Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: b248fd71-d304-4c3e-aadc-aa8c03e032d7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Jenkins-Script-Console

## Summary

This procedure navigates to the Jenkins Script Console after unauthorized authentication, exploiting lack of post-login restrictions.

## Description

With a session established, the attacker accesses administrative features like the Script Console, which allows Groovy script execution. This is limited to the test environment but enables further exploitation.

## Requirements

1. Active authenticated session in Jenkins
2. Browser access to the dashboard
3. Knowledge of Jenkins UI navigation

## Defense

Defensive measures and detection strategies:

- Disable or restrict Script Console access to admins only
- Implement role-based access control (RBAC)
- Log all console accesses and script executions

## Objectives

1. Load the Script Console interface
2. Confirm execution permissions
3. Prepare for code injection

## Instructions

### Step 1: Navigate to Manage Jenkins

**Context**: From the dashboard, access administrative options.

Click on "Manage Jenkins" in the left sidebar.

**Expected Output**: Management page loads with available plugins and features.

### Step 2: Open Script Console

**Context**: Select the console for script execution.

Click on "Script Console" under the management options.

**Expected Output**: Groovy script input area appears, ready for code.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[jenkins]]
- [[script-console]]
