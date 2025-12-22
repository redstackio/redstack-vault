---
id: proc-gitlab-repo-init-001
name: Initiate-GitLab-Repository-Creation
tags:
  - gitlab
  - repository
  - import
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.115Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-GitLab-Repository-Creation

## Summary

This procedure outlines accessing the GitLab web interface to start creating a new repository, selecting the import option to reach the vulnerable URL input field for SSRF exploitation.

## Description

GitLab's repository creation feature allows users to import from external sources via URL. Without validation, entering an arbitrary URL causes the server to fetch it, enabling SSRF. This procedure covers the UI steps to initiate creation and select import, assuming an authenticated session. It's a prerequisite for triggering the vulnerability.

## Requirements

1. Authenticated access to GitLab as a user with project creation permissions
2. Web browser access to the GitLab instance
3. No special tools; standard browser session

## Defense

Defensive measures and detection strategies:

- Enforce URL validation to GitHub domains only in import features
- Log and alert on import attempts with non-standard URLs
- Rate-limit repository creation to prevent abuse

## Objectives

1. Reach the repository import interface
2. Expose the URL field for SSRF payload
3. Prepare for submission without errors

## Instructions

### Step 1: Log In and Navigate to New Project

**Context**: Authenticate and access the project creation page to begin the process.

**Command**: No command; UI navigation.

> Log in to GitLab, click the "+" icon or "New project" button. Select "Create blank project" or directly "Import project". Expected: Form loads with name, namespace, and visibility fields.

### Step 2: Select Import by URL

**Context**: Choose the git repo by URL option to display the vulnerable input.

**Command**: No command; UI selection.

> In the import tab, select "CI/CD for GitLab" or "Repo by URL" if available, or directly enter URL mode. Expected: URL field appears, prompting for a Git-compatible URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- ui-exploit
- import
