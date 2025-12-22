---
tags:
  - invitation
  - team-management
  - csrf
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:29.864Z'
sub_techniques: []
id: 6d3d2abe-a3d0-4ea7-b345-dcb86c9eaa5e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Send Team Member Invitation

## Summary

This procedure sends an invitation to a team member in Infogram, creating a pending invitation that serves as the target for the CSRF-based removal attack.

## Description

Within Infogram's team management, sending an invitation generates a state-changing action that exposes the vulnerable remove endpoint. This step is preparatory for capturing the CSRF-vulnerable request, allowing an attacker to later craft a URL for unauthorized removal. The target environment is the authenticated team dashboard, with outcomes including a visible pending invitation.

## Requirements

1. Authenticated business account session
2. Access to team management interface
3. Test email address for invitation

## Defense

Defensive measures and detection strategies:

- Require confirmation for all invitation actions
- Log and alert on invitation sends/removals
- Enforce CSRF tokens on invitation endpoints

## Objectives

1. Create a pending team invitation
2. Display the invitation in team list for targeting
3. Set up for remove request interception

## Instructions

### Step 1: Navigate to Team Management

**Context**: Access the section for managing team members.

From the dashboard, click on 'Manage Teams' or similar.

> This loads the team interface with current members and invitation options.

### Step 2: Initiate and Send Invitation

**Context**: Add a new member via invitation.

Enter a test email and send the invitation.

> The system processes the request, sends an email, and adds the pending user to the list.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- invitation
- team-management
- csrf
