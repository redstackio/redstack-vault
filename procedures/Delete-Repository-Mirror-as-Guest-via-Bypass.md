---
id: proc-phab-delete-mirror-guest-bypass
tags:
  - authorization-bypass
  - phabricator
  - diffusion
  - deletion
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:44.817Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Delete-Repository-Mirror-as-Guest-via-Bypass

## Summary

This procedure exploits a missing permission check in Phabricator's DiffusionMirrorDeleteController to allow guest users to delete repository mirrors, disrupting synchronization without authentication.

## Description

The vulnerability arises from inadequate authorization in applications/diffusion/controller/DiffusionMirrorDeleteController.php, where the delete endpoint (e.g., /diffusion/TEST/mirror/delete/1/) does not verify user permissions. Guests can directly access this URL to perform the deletion, unlike protected endpoints. Impact includes potential denial of mirror sync, though low severity as creation/editing remains secured.

## Requirements

1. Repository with mirror configured (e.g., 'TEST' with mirror ID 1)
2. Guest access to Phabricator instance
3. Knowledge of repository short name and mirror ID

## Defense

Defensive measures and detection strategies:

- Add explicit requireCapability() checks in DiffusionMirrorDeleteController
- Enable Phabricator's bin/storage reveal for auditing deletions
- Monitor for anomalous guest requests to /mirror/delete/ endpoints via web server logs

## Objectives

1. Unauthorized deletion of a repository mirror
2. Disruption of repository synchronization
3. Demonstration of selective authorization flaw

## Instructions

### Step 1: Identify Mirror Details

**Context**: Gather the target URL components from the repository setup.

Note the repository short name ('TEST') and mirror ID (e.g., 1) from the admin-created mirror.

### Step 2: Access Delete Endpoint as Guest

**Context**: Exploit the bypass by directly invoking the delete action.

In a browser as guest, navigate to http://phabricator/diffusion/TEST/mirror/delete/1/ and confirm the deletion (if prompted, but no auth required).

> Expected: Successful deletion without login; mirror removed from repository view.

### Step 3: Validate Deletion

**Context**: Confirm the impact on the repository.

Re-access the repository mirrors tab; the target mirror should be absent.

> Success: No mirror listed, sync disrupted if active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authorization-bypass]]
- [[phabricator]]
- [[mirror-deletion]]
