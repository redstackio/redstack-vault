---
id: proc-create-gitlab-repo
tags:
  - gitlab
  - setup
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:08.800Z'
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
# Create-GitLab-Repository-for-Testing

## Summary

This procedure sets up a test repository in GitLab to provide commits necessary for exploiting the Git log functionality in the Commits API.

## Description

In the attack scenario, a repository with at least one commit is required to trigger Git commands like log and rev-list via Gitaly. This is done using GitLab's UI or API to create a project and add a file, ensuring the ref_name injection can reference valid commits. The target environment is GitLab 12.0.3, and no special privileges are needed beyond basic user access.

## Requirements

1. Valid GitLab account or API token
2. Network access to GitLab instance
3. GitLab UI or curl for API calls

## Defense

Defensive measures and detection strategies:

- Monitor project creation logs for anomalous activity
- Enforce API rate limiting on project endpoints

## Objectives

1. Establish a testable repository with commits
2. Obtain project ID for API exploitation
3. Ensure minimal footprint for stealth

## Instructions

### Step 1: Create New Project

**Context**: Use GitLab API or UI to create a repository.

**Command** (GitLab UI recommended, or API):
No specific command; use web interface to create project ID 5 and commit a file like README.md.

> Creates a project with commits for log output.

### Step 2: Verify Repository

**Context**: Confirm the repo has commits.

**Command** (Optional curl check):
```bash
curl 'http://target/api/v4/projects/5/repository/commits'
```

> Returns list of commits if setup successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- [[gitlab]]
- [[setup]]
