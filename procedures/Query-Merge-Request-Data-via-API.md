---
id: proc-gitlab-api-query-mr-001
tags:
  - gitlab
  - api
  - bypass
  - query
type: procedure
tools:
  - '[[tools/Postman]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-gitlab-mr-get]]'
  - '[[commands/curl-gitlab-mr-todo-post]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:11.095Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Query-Merge-Request-Data-via-API

## Summary

This procedure uses a personal access token to query GitLab API endpoints for assigned MR data as a Guest user, bypassing access controls and exposing sensitive information.

## Description

Send HTTP requests to MR-specific API paths (e.g., /merge_requests/:id) using the token, retrieving details like title, commits, changes, and pipelines. Also test POST to /todo for interaction. This exploits the failure to revoke API access on demotion. Expected outcomes: Unauthorized data retrieval.

## Requirements

1. Personal access token with api scopes
2. Known project_id and MR_id (e.g., 123 and 1)
3. API client like Postman or curl
4. Network access to GitLab API

## Defense

Defensive measures and detection strategies:

- Enforce consistent permission checks across UI and API
- Audit API access logs for anomalous Guest token usage
- Revoke tokens on role changes

## Objectives

1. Confirm API bypass for MR data exposure
2. Retrieve confidential elements (commits, approvals)
3. Demonstrate interaction capability (e.g., TODO creation)

## Instructions

### Step 1: Query Main MR Endpoint

**Context**: Fetch core MR details to validate access.

Execute [[commands/curl-gitlab-mr-get]] to send GET request:

```bash
curl --header "Authorization: Bearer <token>" "https://gitlab.com/api/v4/projects/<project_id>/merge_requests/<mr_id>"
```

> Returns JSON with title, description, participants despite Guest role.

### Step 2: Access Additional Endpoints

**Context**: Probe related data for full exposure.

Use similar curl for /participants, /commits, /changes, /pipelines, /approvals, /versions.

For interaction, execute [[commands/curl-gitlab-mr-todo-post]]:

```bash
curl --request POST --header "Authorization: Bearer <token>" --header "Content-Type: application/json" -d '{"target_type":"MergeRequest","target_id":<mr_id>}' "https://gitlab.com/api/v4/projects/<project_id>/merge_requests/<mr_id>/todo"
```

> Successful responses confirm bypass; TODO created.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used

- [[commands/curl-gitlab-mr-get]]
- [[commands/curl-gitlab-mr-todo-post]]

## Tools Used

- [[tools/Postman]]

## Tags

- gitlab
- api-bypass
