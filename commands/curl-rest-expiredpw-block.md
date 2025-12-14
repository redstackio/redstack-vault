---
data: >-
  curl --header "PRIVATE-TOKEN: <TOKEN>"
  "https://gitlab.domain.com/api/v4/projects"
tags:
  - rest
  - expired-password
type: command
output: >-
  {"message":"403 Forbidden - Your password expired. Please access GitLab from a
  web browser to update your password."}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.428Z'
id: 21481f56-8f22-44cb-be5a-7b4fc6eb497f
verified: false
validated: true
submitted: true
---
# curl-rest-expiredpw-block

## Command

```bash
curl --header "PRIVATE-TOKEN: <TOKEN>" "https://gitlab.domain.com/api/v4/projects"
```

## Description

Lists projects via REST with expired password token, expecting block.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H 'PRIVATE-TOKEN: <TOKEN>'` | Token (note: PRIVATE-TOKEN header) | Yes |

## Examples

### Basic Usage

```bash
curl --header "PRIVATE-TOKEN: <TOKEN>" "https://gitlab.domain.com/api/v4/projects"
```

## Expected Output

403 with password expiration message.

## Related

- [[commands/curl-graphql-expiredpw-projects-query]]
