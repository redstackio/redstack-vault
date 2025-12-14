---
id: proc-uuid-2
tags:
  - gitlab
  - preparation
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:28.221Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Unauthorized-User-Project

## Summary

Sign in as a low-privilege user without membership in the target private group and create a dummy project to serve as the vector for the IDOR exploit.

## Description

This step simulates the attacker's perspective in GitLab, creating a project that can be used to trigger the vulnerable group sharing endpoint. The user must not have access to the private group. This project acts as the 'from' entity in the sharing process, allowing parameter manipulation.

## Requirements

1. Valid GitLab user account without private group membership
2. Access to project creation UI
3. Web browser

## Defense

Defensive measures and detection strategies:

- Limit project creation to verified users
- Audit project sharing attempts

## Objectives

1. Establish attacker's project for sharing
2. Confirm lack of target group access
3. Prepare for request interception

## Instructions

### Step 1: Sign In as Unauthorized User

**Context**: Log in with a non-member account (e.g., 'jane').

No command; use GitLab login page.

### Step 2: Create Dummy Project

**Context**: Create a new project to use in sharing.

No command; use GitLab UI: Visit http://gitlab-instance/projects/new, name it 'dummy-project', and create.

> Project is now ready for group sharing exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[preparation]]
