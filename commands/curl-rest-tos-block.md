---
data: >-
  curl --header "Authorization: Bearer <TOKEN>"
  "https://gitlab.domain.com/api/v4/user"
tags:
  - rest
  - tos
type: command
output: >-
  {"message": "403 Forbidden - You (@unwilling) must accept the Terms of Service
  in order to perform this action. Please access GitLab from a web browser to
  accept these terms."}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:59.452Z'
id: 4f13e961-a6c8-4a51-b8ad-b84bf2ebec2b
verified: false
validated: true
submitted: true
---
# curl-rest-tos-block

## Command

```bash
curl --header "Authorization: Bearer <TOKEN>" "https://gitlab.domain.com/api/v4/user"
```

## Description

Tests REST access with ToS-declined token, expecting block.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H 'Authorization: Bearer <TOKEN>'` | Token | Yes |

## Examples

### Basic Usage

```bash
curl --header "Authorization: Bearer <TOKEN>" "https://gitlab.domain.com/api/v4/user"
```

## Expected Output

403 with ToS acceptance message.

## Related

- [[commands/curl-graphql-tos-bypass-query]]
