---
id: proc-uuid-4
tags:
  - idor
  - gitlab
  - interception
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/gitlab-share-project-with-group]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:28.206Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Group-Sharing-Request

## Summary

Use a proxy to intercept the POST request during project group sharing and modify the 'link_group_id' parameter to target a private group, exploiting the IDOR.

## Description

In GitLab, the group sharing feature sends a POST to /:username/:project/group_links without validating the group ID against user permissions. Intercept with Burp or similar, change link_group_id to the private ID (e.g., from 6 to 7), and forward. This grants unauthorized access.

## Requirements

1. Proxy tool like Burp Suite configured for browser traffic
2. Dummy project and known private group ID
3. Access to sharing UI

## Defense

Defensive measures and detection strategies:

- Validate group_id against user's accessible groups in controller
- Rate-limit sharing requests and log parameter anomalies

## Objectives

1. Tamper with object reference
2. Bypass authorization
3. Trigger privilege escalation

## Instructions

### Step 1: Navigate to Sharing and Intercept

**Context**: Go to dummy project sharing and select a public group to capture the request.

No command; UI: Visit http://gitlab-instance/jane/dummy-project/group_links, select public group, intercept POST before submit.

### Step 2: Modify and Forward Request

**Context**: Alter the group ID in the intercepted request.

Execute [[commands/gitlab-share-project-with-group]] equivalent via proxy or curl:

```bash
curl -X POST http://gitlab-instance/jane/dummy-project/group_links \
  -d 'utf8=%E2%9C%93&authenticity_token=...&link_group_id=7&link_group_access=40' \
  -H 'Cookie: session=...'
```

> Request forwards, sharing succeeds with private group.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/gitlab-share-project-with-group]]

## Tools Used


## Tags

- [[idor]]
- [[gitlab]]
- [[interception]]
