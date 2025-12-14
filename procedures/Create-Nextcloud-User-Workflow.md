---
tags:
  - nextcloud
  - workflow-creation
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
updated_at: '2025-12-14T17:29:44.946Z'
sub_techniques: []
id: 3f8ce357-4193-4312-bc05-79d49a4054d4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Nextcloud-User-Workflow

## Summary

This procedure sets up a user workflow in Nextcloud to serve as a target for demonstrating access control bypass in deletion operations.

## Description

In the context of testing Nextcloud's workflowengine app, this involves using the web UI to create a new workflow rule. This step requires an authenticated user session and provides a workflow ID needed for subsequent exploitation. The target environment is a standard Nextcloud installation with the workflowengine app enabled, running on PHP. Expected outcome is a persistent workflow entry owned by the user.

## Requirements

1. Authenticated access to Nextcloud web interface
2. Workflowengine app installed and enabled
3. Basic knowledge of Nextcloud UI navigation

## Defense

Defensive measures and detection strategies:

- Enforce workflow creation limits per user to prevent abuse
- Log all workflow creation events with user IDs for auditing

## Objectives

1. Establish a deletable workflow for vulnerability testing
2. Obtain the workflow ID for API targeting
3. Ensure the workflow is user-owned to match access control scope

## Instructions

### Step 1: Navigate to Workflow Settings

**Context**: Access the user-specific workflow management page to initiate creation.

**Command** (Browser Navigation):

Navigate to `/nextcloud/index.php/settings/user/workflow` in your web browser while authenticated.

> This loads the workflow management interface. Expected output: A form or list view for workflows.

### Step 2: Fill and Submit Creation Form

**Context**: Use the UI form to define a simple workflow rule, such as a tag-based action.

**Command** (UI Interaction):

Enter details like entity type (e.g., files), condition (e.g., tag 'test'), and action (e.g., notify), then submit.

> Form submission creates the workflow. Expected output: Success message and the new workflow listed with an ID (e.g., 3).

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
- [[workflow-creation]]
