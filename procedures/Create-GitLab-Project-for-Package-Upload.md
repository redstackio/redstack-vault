---
id: proc-gitlab-create-project
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
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T17:32:20.506Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Create-GitLab-Project-for-Package-Upload

## Summary

This procedure sets up a new GitLab project to serve as a container for uploading PyPi packages, providing the necessary project ID for subsequent API interactions in XSS exploitation.

## Description

In the context of exploiting the stored XSS in GitLab's PyPi endpoint, a project must be created to host packages. This is done via the GitLab web interface or API, requiring a personal access token. The project ID is critical for targeting uploads to /api/v4/projects/:id/packages/pypi. No technical vulnerabilities are exploited here; it's preparatory setup.

## Requirements

1. GitLab account with create project permissions
2. Personal access token for API access (if using API creation)
3. Web browser or curl for project creation

## Defense

Defensive measures and detection strategies:

- Monitor for rapid project creation from suspicious IPs
- Enforce project naming policies and review new projects

## Objectives

1. Obtain a valid project ID for package uploads
2. Ensure API access is configured
3. Prepare environment for payload injection

## Instructions

### Step 1: Access GitLab and Create Project

**Context**: Log in to GitLab and initiate project creation to get the ID.

**Command** (Optional API method using [[tools/curl]]):
```bash
curl --header "PRIVATE-TOKEN: $TOKEN" --request POST "https://gitlab.com/api/v4/projects" --form "name=TestProject" --form "path=test-project"
```

> This creates a project named 'TestProject' and returns JSON with the ID (e.g., "id": 18315917). Alternatively, use the web UI: New Project > Create blank project.

### Step 2: Verify Project Access

**Context**: Confirm the project ID and token permissions for package uploads.

**Command** (Test API access):
```bash
curl --header "PRIVATE-TOKEN: $TOKEN" "https://gitlab.com/api/v4/projects/18315917"
```

> Expected output: Project details JSON. Success confirms setup.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- [[gitlab]]
- [[setup]]
