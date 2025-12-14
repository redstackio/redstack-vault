---
tags:
  - gitlab
  - issue-creation
  - design-upload
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T05:32:13.164Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 066c0219-8d75-4cfe-9950-856cf9a8dd2a
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Create-Issue-with-Design-in-Reporter-Project

## Summary

This procedure involves creating an issue in the Reporter's own project and uploading a design file to it, leveraging permissions allowed in user-owned projects to prepare for migration-based escalation.

## Description

Using the GitLab UI, a Reporter creates a new issue in their project and attaches a design via the Design Management feature, which is permitted since it's their own project. This step sets up the payload (design file) that will be escalated during the move. The technical approach relies on GitLab's permission model allowing Reporters full control over their namespaces. Prerequisites include the Reporter project from setup; outcomes include an issue with an attached design ready for moving.

## Requirements

1. Reporter access to the source project
2. Design file ready (e.g., image or PDF)
3. GitLab Design Management enabled in the instance

## Defense

Defensive measures and detection strategies:

- Disable or restrict Design Management for Reporter roles
- Log all design uploads and review for anomalies in user projects
- Implement file type and size restrictions on uploads

## Objectives

1. Create a migratable issue with attached design
2. Confirm upload succeeds in Reporter context
3. Prepare for permission bypass in next steps

## Instructions

### Step 1: Create New Issue

**Context**: Initiate the issue in the Reporter Project to host the design.

**Instructions**: In 'Reporter Project', click Issues > New issue, add title (e.g., 'Test Issue') and description, then Create issue.

> Issue opens in view mode; confirm it's listed under Issues.

### Step 2: Upload Design File

**Context**: Attach the design to enable migration with payload.

**Instructions**: In the issue, expand the right sidebar, find Designs section, click Upload or drag-and-drop a design file (e.g., test.png).

> Design appears in the Designs panel; verify it's associated with the issue.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[issue-creation]]
- [[design-upload]]
