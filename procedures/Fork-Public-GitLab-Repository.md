---
id: proc-fork-public-gitlab-repo
tags:
  - gitlab
  - fork
  - initial-access
type: procedure
tools:
  - '[[tools/GDK-GitLab-Development-Kit]]'
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
updated_at: '2025-12-13T23:52:20.780Z'
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
# Fork-Public-GitLab-Repository

## Summary

This procedure involves forking a public GitLab repository to create a controllable copy, enabling subsequent modifications like creating branches with malicious payloads for XSS exploitation.

## Description

In the context of exploiting GitLab's persistent XSS in email notifications, forking a public repo provides a starting point without needing write access to the original. This is done via the GitLab web UI on a local or remote instance. Prerequisites include an authenticated user account and access to a public repo. Expected outcome: A forked repo under the attacker's namespace, ready for branch creation.

## Requirements

1. Authenticated GitLab account with forking permissions.
2. Access to a public repository (e.g., HTML5 boilerplate).
3. Running GitLab instance (local GDK recommended for testing).

## Defense

Defensive measures and detection strategies:

- Monitor fork activities on public repos for unusual patterns.
- Implement rate limiting on fork operations.
- Use repo access logs to detect forks followed by malicious MRs.

## Objectives

1. Establish control over a repo copy for payload injection.
2. Prepare for merge request submission to original repo.
3. Enable targeting of original repo maintainers via emails.

## Instructions

### Step 1: Select and Fork Repository

**Context**: Identify a suitable public repo and initiate the fork to your namespace.

No specific command; use GitLab UI:

- Navigate to the public repo page, e.g., `http://yourserver:3000/root/html5-boilerplate`.
- Click the 'Fork' button.

> This creates a copy in your namespace without affecting the original.

**Expected Output**: Fork confirmation and redirect to your forked repo.

### Step 2: Verify Fork Access

**Context**: Confirm the fork is accessible and under your control.

- Visit the forked repo's main page.

> Ensures you can proceed to create branches.

**Expected Output**: Dashboard loads with your namespace in the URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GDK-GitLab-Development-Kit]]

## Tags

- gitlab
- fork
- reconnaissance
