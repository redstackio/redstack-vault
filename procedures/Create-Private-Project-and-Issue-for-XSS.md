---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - gitlab
  - setup
  - private-project
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-13T23:52:43.825Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-Private-Project-and-Issue-for-XSS

## Summary

This procedure sets up a private GitLab project and issue to serve as an inaccessible reference, enabling the storage of encoded XSS payloads that will be unencoded during redaction for unauthorized viewers.

## Description

In the context of exploiting GitLab's stored XSS via ReferenceRedactorFilter, create a private project using an account with permissions. Add an issue to this project, which will be referenced in a public comment. The privacy ensures the link triggers redaction, leading to payload injection. This targets GitLab instances running Ruby 2.6.5 and Rails with markdown processing. Expected outcome: A hidden resource for payload linkage, setting the stage for XSS without alerting authorized users.

## Requirements

1. GitLab account with project creation permissions
2. Access to GitLab web interface
3. No special tools; UI-based setup

## Defense

Defensive measures and detection strategies:

- Monitor for rapid private project creation followed by public references
- Enforce project visibility audits and restrict cross-project linking
- Implement client-side sanitization for all rendered markdown

## Objectives

1. Establish a private reference point for XSS payload injection
2. Ensure the resource is inaccessible to target victims
3. Prepare for linking in public content to trigger exploitation

## Instructions

### Step 1: Create Private Project

**Context**: Use GitLab UI to initiate a new private project, preventing unauthorized access.

**Command** (UI Action):
No CLI command; navigate to Projects > New Project, set visibility to Private, name it (e.g., private-project), and create.

> This creates a project at a URL like https://gitlab.com/username/private-project. Expected: Confirmation page with project dashboard.

### Step 2: Create Issue in Private Project

**Context**: Add an issue to the private project to serve as the target reference.

**Command** (UI Action):
No CLI; in the project, go to Issues > New Issue, add a title and description (minimal content), and submit as issue #1.

> Expected: Issue created at /private-project/-/issues/1, visible only to project members.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[setup]]
