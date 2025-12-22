---
tags:
  - nextcloud
  - verification
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
updated_at: '2025-12-14T17:29:44.930Z'
sub_techniques: []
id: 8f3a55e0-1dcd-45d0-ae26-f8522870d95f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Workflow-Deletion

## Summary

This procedure confirms the success of the API-based deletion by checking the Nextcloud UI, ensuring the workflow is removed without traces.

## Description

Post-exploitation verification involves refreshing the workflow management UI to observe the absence of the deleted item. This step validates the bypass in a Nextcloud environment with workflowengine, confirming the impact of the access control flaw.

## Requirements

1. Access to the same authenticated session
2. Original workflow settings UI
3. Prior successful API deletion

## Defense

Defensive measures and detection strategies:

- Cross-verify UI and backend states after deletions
- Alert on discrepancies between API logs and UI views

## Objectives

1. Confirm workflow removal
2. Validate bypass effectiveness
3. Assess for any residual effects

## Instructions

### Step 1: Refresh UI

**Context**: Reload the workflow list to check current state.

**Command** (Browser Action):

Navigate or refresh `/nextcloud/index.php/settings/user/workflow`.

> Updates the view. Expected output: Empty or reduced workflow list.

### Step 2: Inspect List

**Context**: Scan for the target workflow's absence.

**Command** (UI Check):

Review the displayed workflows.

> No target workflow should appear. Expected output: Confirmation of deletion; no error messages.

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
- [[verification]]
