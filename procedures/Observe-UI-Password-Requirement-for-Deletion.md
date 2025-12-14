---
tags:
  - nextcloud
  - ui-observation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:44.941Z'
sub_techniques: []
id: 83e6e8d9-57fb-4046-916b-819b6fde0541
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-UI-Password-Requirement-for-Deletion

## Summary

This procedure demonstrates the standard security control in Nextcloud's web UI for workflow deletion, which requires password confirmation to prevent accidental or unauthorized actions.

## Description

By attempting deletion through the UI, this step highlights the context-dependent access control present in the frontend but absent in the backend API. It requires an authenticated session and is performed on a Nextcloud instance with workflowengine. The outcome confirms the password prompt as a protective measure against destructive operations.

## Requirements

1. Existing user workflow created
2. Authenticated web session
3. Access to workflow settings UI

## Defense

Defensive measures and detection strategies:

- Monitor UI interactions for repeated failed deletion attempts
- Implement client-side logging of confirmation prompts

## Objectives

1. Verify the presence of password confirmation in UI
2. Understand the security expectation for deletion
3. Prepare for API bypass comparison

## Instructions

### Step 1: Access Workflow List

**Context**: Load the UI page containing the target workflow.

**Command** (Browser Navigation):

Go to `/nextcloud/index.php/settings/user/workflow`.

> Displays the list of user workflows. Expected output: Target workflow visible.

### Step 2: Initiate Deletion

**Context**: Trigger the delete action to observe the control.

**Command** (UI Interaction):

Click the Delete button next to the workflow.

> This prompts for password confirmation. Expected output: Modal dialog requesting user password; deletion halts without input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[ui-observation]]
