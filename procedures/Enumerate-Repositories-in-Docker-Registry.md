---
tags:
  - docker
  - enumeration
  - access-control
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/docker-catalog-enumerate]]'
verified: false
platforms:
  - Docker
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:30.939Z'
sub_techniques: []
id: aa99a721-83b0-4631-aba7-0d6eb8f6cf40
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enumerate Repositories in Docker Registry

## Summary

This procedure enumerates all repositories hosted in an unauthenticated Docker Registry by querying the /v2/_catalog endpoint, revealing available images for further exploitation.

## Description

Targeting an exposed Docker Registry API v2, this procedure sends an unauthenticated GET request to list repositories. In the attack scenario, this bypasses access controls on a .mil-hosted service, exposing confidential repositories. Prerequisites include a reachable registry IP; outcomes include a JSON list of repositories for tag enumeration.

## Requirements

1. Exposed registry IP/domain
2. curl or similar HTTP client
3. No authentication needed

## Defense

Defensive measures and detection strategies:

- Enable authentication on registry endpoints
- Log and monitor API calls to /v2/_catalog
- Use network segmentation to hide registries

## Objectives

1. List all repositories without credentials
2. Identify targets for image download
3. Confirm improper access control

## Instructions

### Step 1: Query Catalog Endpoint

**Context**: Retrieve the list of repositories via HTTP GET.

**Command** ([[commands/docker-catalog-enumerate]]):
```bash
curl -X GET 'https://TARGET_IP/v2/_catalog' -H 'Host: TARGET_IP' -H 'Accept: */*'
```

> Returns JSON like {"repositories":["namespace/repo1","namespace/repo2"]} if successful.

### Step 2: Parse Response

**Context**: Extract repository names for next steps.

**Command** ([[commands/jq-parse-json]]):
```bash
curl -s 'https://TARGET_IP/v2/_catalog' | jq '.repositories[]'
```

> Filters the JSON to list repositories individually.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/docker-catalog-enumerate]]
- [[commands/jq-parse-json]]

## Tools Used


## Tags

- docker
- enumeration
- registry
