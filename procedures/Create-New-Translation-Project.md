---
id: proc-uuid-0002
tags:
  - project-setup
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:56:03.552Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-New-Translation-Project

## Summary

This procedure sets up a new translation project in the Localize application, selecting document translation to enable the upload of files with vulnerable title fields.

## Description

Project creation is a prerequisite for accessing the document upload feature where the XSS payload will be injected. By choosing 'documents' as the translation type, the attacker navigates to the upload interface. This step leverages the application's workflow to position for exploitation without raising immediate suspicion. Outcomes include a configured project ready for tainted uploads.

## Requirements

1. Active authenticated session in Localize.
2. Permissions to create projects.
3. Web browser access to the dashboard.

## Defense

Defensive measures and detection strategies:

- Rate-limit project creations to detect automated abuse.
- Log and review new project initiations for unusual patterns.
- Enforce role-based access control (RBAC) to limit project creation.

## Objectives

1. Access document upload functionality.
2. Prepare environment for payload injection.
3. Maintain stealth in legitimate-looking actions.

## Instructions

### Step 1: Initiate Project Creation

**Context**: Start the project setup process from the dashboard.

Click the 'New Project' button on the main dashboard.

> This opens the project type selection. Expected output: Form with options like 'Documents'.

### Step 2: Select Document Translation

**Context**: Choose the specific workflow that exposes the vulnerable upload field.

Select 'Documents' for what you are translating and proceed.

> Advances to upload screen. Expected output: Interface for file upload and title input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[project-creation]]
- [[setup]]
