---
tags:
  - gitlab
  - api
  - information-disclosure
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-fetch-gitlab-snippets]]'
platforms:
  - Web
  - GitLab
techniques:
  - '[[T1213.003]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f2a150e4-f7f9-48e1-aae0-f5e4f45b8db1
created_at: '2025-12-14T17:32:10.400Z'
updated_at: '2025-12-14T17:32:10.400Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1213.003]]'
---
# Fetch-All-Snippets-via-GitLab-API

## Summary

This procedure uses the GitLab API to list all snippets in a project, bypassing access controls to reveal private snippet metadata.

## Description

Exploiting the vulnerability, an authenticated user queries the /projects/:id/snippets endpoint, which returns private snippets from public/internal projects without checks. This discloses IDs, titles, and authors, enabling further retrieval. Requires a valid PRIVATE-TOKEN.

## Requirements

1. GitLab API token (personal access token with api scope)
2. Project ID from setup
3. curl or similar HTTP client

## Defense

Defensive measures and detection strategies:

- Patch GitLab to version 9.5.6+ where this is fixed
- Monitor API logs for excessive snippet queries
- Implement token scoping to limit API access

## Objectives

1. List all snippets including private ones
2. Extract snippet IDs for content retrieval
3. Confirm disclosure of unauthorized metadata

## Instructions

### Step 1: Query Snippets Endpoint

**Context**: Send an authenticated GET request to fetch the snippets list.

**Command** ([[commands/curl-fetch-gitlab-snippets]]):
```bash
curl --header "PRIVATE-TOKEN: XXXXXXXXXXXXXX" "http://gitlab-instance/api/v3/projects/1/snippets"
```

> This returns a JSON array with snippet objects, including private ones like {"id":6,"title":"Secret snippet","author":{"name":"User"},...}. Look for unexpected private entries.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[T1213.003]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-gitlab-snippets]]

## Tools Used

- [[tools/curl]]

## Tags

- [[api]]
- [[information-disclosure]]
