---
tags:
  - gitlab
  - configuration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands//add_contacts]]'
  - '[[commands//remove_contacts]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 2d272dc0-a0ca-4345-9034-9f883d4469cc
created_at: '2025-12-11T03:47:49.752Z'
updated_at: '2025-12-11T03:47:49.752Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Enable Customer Relations in Group

## Summary

This procedure enables the Customer Relations feature in a GitLab group, which is necessary for exploiting related vulnerabilities like stored XSS.

## Description

Enabling this feature exposes fields vulnerable to input sanitization issues. It targets GitLab 15.0.0 environments running on Linux with supporting services.

## Requirements

1. Ownership or admin access to the GitLab group
2. GitLab web interface access

## Defense

Defensive measures and detection strategies:

- Audit feature enablement in group settings
- Implement input validation for feature-related fields

## Objectives

1. Activate vulnerable feature
2. Prepare for payload injection

## Instructions

### Step 1: Navigate to Settings

**Context**: Go to group Settings -> General.

> Expand 'Permissions and group features'.

### Step 2: Enable Feature

**Context**: Toggle 'Customer Relations' to enabled and save.

> Confirm the feature is active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #gitlab
- #configuration
