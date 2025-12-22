---
id: 123e4567-e89b-12d3-a456-426614174001
name: Setup-Workspace-and-Accounts-for-Testing
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.224Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
tags:
  - setup
  - workspace
  - accounts
platforms:
  - Web
tools: []
commands: []
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---

# Setup-Workspace-and-Accounts-for-Testing

## Summary

This procedure sets up a Dust workspace environment with attacker and victim accounts to simulate the stored XSS attack, ensuring controlled testing of privilege escalation.

## Description

In the context of exploiting Dust's file upload XSS, this initial setup creates or accesses a workspace where the attacker has admin rights, then adds a low-privilege dummy account to mimic the attacker's position. This allows testing the upload and escalation without affecting production. Prerequisites include a Dust account; outcomes include ready accounts and workspace SID for API calls.

## Requirements

1. Valid Dust.tt account with ability to create workspaces
2. Access to invite members via the web interface
3. Dummy email/account for the low-privilege member

## Defense

Defensive measures and detection strategies:

- Monitor workspace creation and member invitations for anomalies
- Enforce role-based access controls during setup
- Log all account additions and review for unauthorized invites

## Objectives

1. Establish controlled environment for XSS exploitation
2. Simulate attacker (member) and victim (admin) roles
3. Obtain workspace SID for subsequent API interactions

## Instructions

### Step 1: Create or Access Workspace

**Context**: Log in to Dust.tt and create a new workspace or select an existing one to serve as the test environment.

**Instructions**: Navigate to the Dust dashboard, click 'Create Workspace', name it (e.g., 'TestXSS'), and note the generated workspace SID from the URL (e.g., /w/<workspace_sid>).

> Successful login and workspace creation grants admin privileges to the creator.

### Step 2: Invite Dummy Account

**Context**: Add a low-privilege account to simulate the attacker uploading from a member role.

**Instructions**: In the workspace settings, go to 'Members', click 'Invite', enter a dummy email, and assign 'Member' role. Have the dummy account accept the invite and log in.

> Dummy account joins with limited permissions, ready for file upload testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[workspace]]
- [[accounts]]
