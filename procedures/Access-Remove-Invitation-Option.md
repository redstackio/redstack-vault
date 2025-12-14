---
tags:
  - remove-invitation
  - csrf
  - web
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
updated_at: '2025-12-14T17:27:29.861Z'
sub_techniques: []
id: 154bed45-2d0f-4493-9e28-15dbc1bff7d8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Access Remove Invitation Option

## Summary

This procedure locates and triggers the remove option for a pending team invitation in Infogram, preparing for request interception to expose the CSRF vulnerability.

## Description

In the team management interface, accessing the remove function for an invited user initiates a state-changing request lacking CSRF protection. This step is crucial for discovery, as it reveals the endpoint vulnerable to unauthorized GET-based removal. Prerequisites include an active invitation; outcomes confirm the option's availability without tokens.

## Requirements

1. Pending invitation in team list
2. Authenticated admin session
3. Burp Suite proxy configured

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to remove actions
- Require user confirmation dialogs
- Audit logs for remove attempts

## Objectives

1. Identify remove functionality for invitations
2. Trigger the vulnerable request path
3. Prepare for interception

## Instructions

### Step 1: Locate Pending Invitation

**Context**: Find the target invitation in the team members list.

Scroll to the pending users section.

> Pending invitations are marked as 'Invited' with email addresses.

### Step 2: Select Remove Option

**Context**: Initiate the removal to generate the request.

Click the remove or cancel invitation button next to the entry.

> This submits the GET request to the /api/team/cancel-invitation endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- remove-invitation
- csrf
- web
