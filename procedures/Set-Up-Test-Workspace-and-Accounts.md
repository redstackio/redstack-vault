---
tags:
  - setup
  - workspace
  - accounts
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:38.425Z'
sub_techniques: []
id: d2f43406-78e4-49b5-b51f-217544230f3d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-Test-Workspace-and-Accounts

## Summary

This procedure establishes the testing environment for the Dust XSS attack by creating a workspace and inviting a dummy member account, simulating the attacker-controlled account.

## Description

In the context of exploiting Dust's file upload vulnerability, initial setup is crucial to have administrative control for validation and a low-privilege member account for exploitation. This involves logging into dust.tt, creating or selecting a workspace, and inviting a secondary account as a member. The workspace SID is needed for API calls, and the dummy account's session cookie is required for authenticated uploads.

## Requirements

1. Valid Dust.tt admin credentials
2. Access to web browser for account management
3. Secondary email/account for dummy user

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit workspace creation
- Monitor for unusual account invitations from admin accounts
- Use anomaly detection on session creations

## Objectives

1. Prepare controlled environment for XSS testing
2. Establish attacker (member) and victim (admin) roles
3. Obtain necessary identifiers like workspace SID

## Instructions

### Step 1: Create or Access Workspace

**Context**: Log in as admin to set up the target workspace.

**Instructions**: Navigate to dust.tt, log in with admin credentials, and create a new workspace or use an existing one. Note the workspace SID from the URL (e.g., /w/<workspace_sid>).

### Step 2: Invite Dummy Account

**Context**: Add a low-privilege member to simulate the attacker.

**Instructions**: From the workspace settings, invite a secondary account via email, assigning it the 'member' role. Log in to the dummy account to obtain its session cookie ('appSession').

**Expected Output**: Confirmation email sent and account joined as member.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[setup]]
- [[workspace]]
- [[accounts]]
