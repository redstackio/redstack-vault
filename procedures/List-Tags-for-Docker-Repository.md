---
tags:
  - docker
  - tags
  - enumeration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/docker-tags-list]]'
verified: false
platforms:
  - Docker
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:30.937Z'
sub_techniques: []
id: 5ef9eeed-5850-484d-aab6-3a1b2e2e5b8d
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# List Tags for Docker Repository

## Summary

This procedure lists available tags for a specific repository in an unauthenticated Docker Registry, identifying versioned images for manifest retrieval and download.

## Description

After enumerating repositories, query the /v2/<namespace>/<repo>/tags/list endpoint to get tags like '3.0.1'. This exploits the lack of auth on a public .mil registry, allowing selection of images with source code. Requires registry access; yields JSON tags for further steps.

## Requirements

1. Known repository namespace and name
2. HTTP client like curl
3. Accessible registry endpoint

## Defense

Defensive measures and detection strategies:

- Require auth for tag list endpoints
- Rate-limit API requests
- Audit logs for unauthorized tag queries

## Objectives

1. Retrieve tags for a repository
2. Select a tag for image exploitation
3. Expose version information

## Instructions

### Step 1: Request Tags

**Context**: GET the tags list for the chosen repository.

**Command** ([[commands/docker-tags-list]]):
```bash
curl -X GET 'https://TARGET_IP/v2/NAMESPACE/REPO/tags/list' -H 'Host: TARGET_IP' -H 'Accept: */*'
```

> Outputs JSON like {"name":"namespace/repo","tags":["3.0.1"]}.

### Step 2: Select Tag

**Context**: Choose a tag from the response for manifest retrieval.

**Command** ([[commands/echo-select-tag]]):
```bash
echo '3.0.1'
```

> Manually select and note the tag for use in subsequent commands.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/docker-tags-list]]
- [[commands/echo-select-tag]]

## Tools Used


## Tags

- docker
- tags
- enumeration
