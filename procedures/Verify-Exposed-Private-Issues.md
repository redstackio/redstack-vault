---
tags:
  - verification
  - exposure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Discovery]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 08e99f7d-d188-4542-bccf-83b3299435df
created_at: '2025-12-11T03:47:56.922Z'
updated_at: '2025-12-11T03:47:56.922Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1087]]'
---
# Verify Exposed Private Issues

## Summary

This procedure checks the imported project's issues tab to confirm successful exposure of private objects linked via the IDOR bypass.

## Description

Post-import, navigate to the issues section to verify access to previously private resources, confirming the attack's success in discovering and exposing data.

## Requirements

1. Imported project in GitLab
2. Knowledge of targeted issue IDs
3. Web access to the project

## Defense

Defensive measures and detection strategies:

- Implement access controls on issue relations
- Monitor for unauthorized issue views

## Objectives

1. Confirm linkage and visibility of private issues
2. Validate attack impact
3. Identify exposed resources

## Instructions

### Step 1: Access Issues Tab

**Context**: Navigate to the imported project's issues.

Go to Project > Issues in GitLab.

> Look for the specified issue ID (e.g., 29279725).

### Step 2: Verify Access

**Context**: Check details of exposed issues.

Click on the issue to view contents.

> Expected: Full access to private issue data.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #verification
