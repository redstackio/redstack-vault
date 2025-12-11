---
tags:
  - information-disclosure
  - jenkins
  - api-tokens
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - Jenkins
techniques:
  - '[[Account Discovery]]'
  - '[[Data from Local System]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: befffd84-8ef5-4a6d-a9d8-875eac82f5aa
created_at: '2025-12-11T06:10:15.836Z'
updated_at: '2025-12-11T06:10:15.836Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1087]]'
  - '[[T1005]]'
---
# Access Sensitive API Tokens and Source Code

## Summary

This procedure involves navigating an authenticated Jenkins session to disclose API tokens and source code, exploiting poor access controls.

## Description

Once authenticated, the Jenkins dashboard exposes sensitive data like API tokens in user configs and source code in job repositories, leading to potential further attacks.

## Requirements

1. Authenticated Jenkins session.
2. Knowledge of Jenkins interface navigation.
3. No additional tools needed.

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) in Jenkins.
- Monitor dashboard access and data views in logs.

## Objectives

1. Retrieve API tokens.
2. Access and download source code.
3. Identify usable sensitive information.

## Instructions

### Step 1: View API Tokens

**Context**: Navigate to user configuration.

Go to /user/<username>/configure to view API tokens.

> Expected: Display of active API tokens.

### Step 2: Access Repositories

**Context**: Browse job configurations.

Navigate to job pages and view source code repositories.

> Expected: Exposure of code for public apps.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]
- [[Collection]]

### Techniques

- [[Account Discovery]]
- [[Data from Local System]]

### Sub-Techniques

None

## Commands Used

None

## Tools Used

None

## Tags

- information-disclosure
- jenkins
- api-tokens
