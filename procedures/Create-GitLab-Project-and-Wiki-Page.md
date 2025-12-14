---
tags:
  - gitlab
  - setup
  - wiki
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
updated_at: '2025-12-13T23:52:55.493Z'
sub_techniques: []
id: f2450710-43c2-41c2-bec0-cfba5cea2491
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-GitLab-Project-and-Wiki-Page

## Summary

This procedure sets up a GitLab project and initializes a wiki page, providing the foundation for injecting malicious content in subsequent exploitation steps.

## Description

In the context of exploiting the stored XSS vulnerability, an attacker needs a project with wiki access to create the '_sidebar' page where the payload will be stored. This step requires authenticated access to GitLab and navigates through the UI to enable wiki features. The target environment is any GitLab instance (version affected by CVE or similar), and success allows progression to payload injection without alerting defenses.

## Requirements

1. Valid GitLab user credentials with project creation permissions
2. Web browser access to the GitLab instance
3. No special network requirements beyond standard HTTPS

## Defense

Defensive measures and detection strategies:

- Enforce project creation approvals or rate limiting
- Monitor for rapid wiki page creations in new projects
- Use GitLab's audit logs to track wiki modifications

## Objectives

1. Gain access to wiki editing capabilities
2. Prepare a persistent storage point for the XSS payload
3. Ensure the wiki is enabled without errors

## Instructions

### Step 1: Log In and Create Project

**Context**: Authenticate and initiate a new project to access wiki features.

Navigate to your GitLab instance, log in, and click 'New project'. Fill in project details (name, description) and create it.

**Expected Output**: Project dashboard loads with wiki option available.

### Step 2: Access and Initialize Wiki

**Context**: Enter the wiki section and create the initial page.

From the project sidebar, select 'Wiki' > 'Create your first page'. Set title to '_sidebar'.

**Expected Output**: Wiki page form opens, ready for content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[setup]]
