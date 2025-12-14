---
tags:
  - gitlab
  - issue-creation
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
updated_at: '2025-12-13T23:52:34.050Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 1e0c3832-f4f5-4423-b7f4-b0d16bf44379
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-New-Issue-in-GitLab-Project

## Summary

This procedure creates a new issue in a GitLab project to serve as the vector for injecting the stored XSS payload into comments.

## Description

GitLab issues allow users with appropriate permissions to add comments containing notes, which are processed by vulnerable components like SyntaxHighlightFilter. This step prepares the attack surface by navigating the UI to create an issue, ensuring the comment field is available for payload submission. It targets any project where the attacker has write access and assumes a logged-in session.

## Requirements

1. Logged-in GitLab user with project member role (Developer or higher)
2. Access to the GitLab web interface
3. No special tools; standard browser sufficient

## Defense

Defensive measures and detection strategies:

- Restrict issue creation to trusted users via role-based access control
- Monitor for anomalous issue creation patterns in audit logs
- Enable project visibility restrictions to limit exposure

## Objectives

1. Establish a comment-submission point for XSS payload
2. Confirm user permissions for exploitation
3. Set up for payload injection without alerting defenses

## Instructions

### Step 1: Navigate to Project

**Context**: Log in and select the target project to access issue tracking.

**Command** (UI action):

Browse to the project dashboard and click "Issues" in the left sidebar.

> Ensures the project is loaded; verify no permission errors.

### Step 2: Create Issue

**Context**: Use the issue creation form to start a new thread.

**Command** (UI action):

Click "New issue" button, enter a title (e.g., "Test Issue"), and proceed to the description/comment area without submitting yet.

> The form opens with a Markdown-enabled comment box ready for payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- issue-creation
