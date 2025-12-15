---
id: uuid-create-mr-diffnote
tags:
  - gitlab
  - merge-request
  - diffnote
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.157Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Merge-Request-and-DiffNote

## Summary

This procedure creates a merge request in GitLab to expose file differences and generates a DiffNote by commenting on a diff line, providing the object needed for the GraphQL type confusion exploit.

## Description

As User B (maintainer), create a merge request comparing branches to highlight file changes. Then, in the diff view, comment on a specific line to create a DiffNote, which has a global ID that can be abused in the destroySnippet mutation. This targets the Snippets::DestroyService indirectly via the DiffNote's repository method. Prerequisites include the setup project with branches.

## Requirements

1. Maintainer access to project
2. Branches with differing file content
3. Access to GitLab merge request UI

## Defense

Defensive measures and detection strategies:

- Limit merge request creation to developers
- Audit DiffNote creations for unusual patterns

## Objectives

1. Generate a merge request for diff exposure
2. Create a DiffNote as the exploit vector
3. Prepare for ID extraction

## Instructions

### Step 1: Create Merge Request

**Context**: Compare branches to create a diff view.

No specific command; in project, navigate to Merge Requests > New Merge Request, select source/target branches.

> Submit the MR; confirm it appears in the list with file differences visible.

### Step 2: Add DiffNote Comment

**Context**: Comment on a line in the diff to generate DiffNote.

No specific command; in MR diff view, click a changed line, enter comment, and submit.

> Verify comment appears in MR discussion; this creates the DiffNote object.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- merge-request
- diffnote
