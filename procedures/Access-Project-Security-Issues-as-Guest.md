---
id: proc-gitlab-access-issues-as-guest
tags:
  - gitlab
  - authorization-bypass
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:36.603Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Project-Security-Issues-as-Guest

## Summary

This procedure exploits an authorization bypass in GitLab, allowing a guest user to view private project security issues via their personal dashboard after demotion.

## Description

Post-demotion, as User B (guest), access the personal security dashboard to retrieve existing project vulnerabilities, including file locations and details. Direct project access is blocked, but the dashboard bypasses checks, disclosing sensitive info like vulnerability types and affected files. This reveals internal structure to unauthorized users. Expected outcome: Full visibility of security issues without project permissions.

## Requirements

1. Project added to personal dashboard pre-demotion
2. Guest role in the project
3. Enabled security dashboard in GitLab

## Defense

Defensive measures and detection strategies:

- Remove projects from user dashboards on role downgrade
- Monitor anomalous dashboard access in logs
- Implement permission re-checks for dashboard views

## Objectives

1. Gain unauthorized read access to security data
2. Collect vulnerability details for potential exploitation
3. Demonstrate persistence of access post-revocation

## Instructions

### Step 1: Navigate to Personal Dashboard

**Context**: Access the user's security overview as guest.

Log in as User B, go to avatar > Security & analysis > Security dashboard.

> Dashboard loads with added projects.

### Step 2: View Project Issues

**Context**: Inspect security details for the target project.

Select the private project in the dashboard; review vulnerabilities, file paths, and issue descriptions.

> Displays details like CVEs, affected files (e.g., package.json), despite guest role.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[authorization-bypass]]
- [[information-disclosure]]
