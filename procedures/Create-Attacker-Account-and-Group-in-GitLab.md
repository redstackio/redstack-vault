---
id: proc-gitlab-create-account-group-001
tags:
  - gitlab
  - account-creation
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:55:06.935Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Attacker-Account-and-Group-in-GitLab

## Summary

This procedure establishes an initial foothold on a GitLab instance by registering a new attacker account and creating a group with administrative control, setting the stage for injecting malicious configurations.

## Description

In the context of exploiting GitLab vulnerabilities, creating a dedicated attacker account and group is essential for isolating the attack and gaining the necessary permissions to modify group settings. This targets self-hosted or public GitLab instances where user registration is open. The outcome is a controlled environment for subsequent XSS injection without alerting existing users.

## Requirements

1. Access to the GitLab instance's registration page (no prior credentials needed if open sign-up).
2. Web browser for UI navigation.
3. Valid email for account verification (if enabled).

## Defense

Defensive measures and detection strategies:

- Disable open registration or require admin approval for new accounts.
- Monitor for rapid group creations from new accounts using audit logs.
- Implement rate limiting on sign-ups and group operations.

## Objectives

1. Gain legitimate access as a low-privilege user.
2. Create a group for payload storage.
3. Prepare for privilege escalation via injected content.

## Instructions

### Step 1: Register Attacker Account

**Context**: Create a new user account to operate under without compromising existing credentials.

No command required; use the UI:

Navigate to https://gitlab.domain.com/users/sign_up and register 'attacker01' with a valid email and password.

> Account creation succeeds if registration is open; verify via email confirmation if needed.

### Step 2: Log In and Create Group

**Context**: Authenticate and establish a group for settings manipulation.

No command required; use the UI:

Log in at https://gitlab.domain.com/users/sign_in, then visit https://gitlab.domain.com/groups/new and create 'attack_group'.

> Group is created with the attacker as Owner; dashboard shows the new group.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[account-creation]]
