---
data: >-
  curl --header "Authorization: Bearer <<ADMIN TOKEN>>"
  "https://gitlab.domain.com/api/v4/projects/<PROJECT_ID>/members" --data
  "user_id=2&access_level=40"
tags:
  - rest
  - project-member
type: command
output: Success response adding member
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.477Z'
id: 13753e85-fca2-4777-a7c3-bc38826b98fc
verified: false
validated: true
submitted: true
---
# curl-add-user-to-project

## Command

```bash
curl --header "Authorization: Bearer <<ADMIN TOKEN>>" "https://gitlab.domain.com/api/v4/projects/<PROJECT_ID>/members" --data "user_id=2&access_level=40"
```

## Description

Adds a user to a GitLab project as a member using REST API, requiring admin token; used to grant access for mutation tests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data "user_id=2"` | ID of user to add | Yes |
| `--data "access_level=40"` | Access level (40=developer) | Yes |
| `-H 'Authorization: Bearer <<ADMIN TOKEN>>'` | Admin auth | Yes |

## Examples

### Basic Usage

```bash
curl --header "Authorization: Bearer <<ADMIN TOKEN>>" "https://gitlab.domain.com/api/v4/projects/<PROJECT_ID>/members" --data "user_id=2&access_level=40"
```

## Expected Output

201 Created with member details.

## Related

- [[commands/curl-graphql-labelcreate-mutation]]
- [[procedures/Perform-GraphQL-Mutation-with-Deactivated-Token]]
