---
tags:
  - merge-request
  - gitlab-ui
type: procedure
tools:
  - '[[tools/Git]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:44.368Z'
sub_techniques: []
id: 6955906b-3d54-4b87-93a5-c072005b0c38
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Merge-Request-from-Master-to-XSS-Branch

## Summary

This procedure uses the GitLab UI to create a merge request from master (source) to the XSS branch (target), ensuring rebase is required.

## Description

The MR setup displays the target branch name in the rebase widget, triggering XSS when viewed. Source and target are swapped to create the conflict scenario.

## Requirements

1. Developer permissions on project
2. Branches pushed to remote
3. Access to Merge Requests UI

## Defense

Defensive measures and detection strategies:

- Validate MR source/target branches
- Require approvals for MRs with unusual branches
- Scan MR descriptions/branches for payloads

## Objectives

1. Initiate MR with rebase prompt
2. Expose vulnerable widget
3. Prepare for victim viewing

## Instructions

### Step 1: Create MR

**Context**: Set up the conflicting MR.

**Instructions**: Navigate to Project > Merge Requests > New merge request. Set source branch: master, target branch: <img/src='x'/onerror=alert(document.domain)>, add title/description, submit.

> Expected output: MR page shows 'Rebase and merge' button due to conflicts.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Git]]

## Tags

- merge-request
- gitlab-ui
