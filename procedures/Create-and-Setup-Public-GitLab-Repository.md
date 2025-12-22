---
id: proc-001
tags:
  - gitlab
  - repository-setup
  - initial-access
type: procedure
tools:
  - '[[tools/Git]]'
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
updated_at: '2025-12-14T03:46:37.777Z'
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
# Create-and-Setup-Public-GitLab-Repository

## Summary

This procedure sets up a public GitLab repository with an enabled wiki submodule, providing a vector for uploading and hosting malicious content accessible to any visitor.

## Description

In the context of exploiting GitLab's wiki XSS vulnerability, creating a public repository allows attackers to push HTML files via Git without restrictions. The wiki acts as a Git submodule, enabling file uploads that are rendered as HTML pages. This step requires a GitLab account but no special privileges, making it accessible for initial access in phishing or social engineering campaigns targeting GitLab users.

## Requirements

1. Valid GitLab account
2. Web browser for UI interaction
3. SSH key pair configured for GitLab (for later pushes)

## Defense

Defensive measures and detection strategies:

- Monitor for rapid creation of public repositories with wiki activity
- Enforce repository approval workflows for new projects
- Use GitLab's audit logs to track wiki pushes from suspicious IPs

## Objectives

1. Establish a public hosting vector for malicious wiki content
2. Obtain wiki Git URL for cloning and uploading
3. Ensure public accessibility without authentication

## Instructions

### Step 1: Create New Repository

**Context**: Use GitLab's web interface to initiate the public repo.

No command-line command; perform via UI:

1. Log in to GitLab.
2. Click 'New project' > 'Create blank project'.
3. Name: 'test', Visibility: Public, Enable wiki.
4. Create project.

> Expected output: Repo at https://gitlab.com/<username>/test with wiki enabled.

### Step 2: Note Wiki URL

**Context**: Identify the Git URL for the wiki submodule.

No command; manually note: git@gitlab.com:<username>/test-wiki.git

> Expected output: SSH URL ready for cloning.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Git]]

## Tags

- gitlab
- repository-setup
