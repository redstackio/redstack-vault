---
id: cmd-curl-check-team-members
data: >-
  curl -X GET 'https://platform.enjin.io/api/project/YOUR_PROJECT_ID/team' -H
  'Authorization: Bearer YOUR_TOKEN'
tags:
  - web
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.475Z'
verified: false
validated: true
submitted: true
---
# curl-check-team-members

## Command

```bash
curl -X GET 'https://platform.enjin.io/api/project/YOUR_PROJECT_ID/team' -H 'Authorization: Bearer YOUR_TOKEN'
```

## Description

Retrieves the list of team members for a specific Enjin project to verify if the member limit bypass was successful.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| YOUR_PROJECT_ID | ID of the project | Yes |
| YOUR_TOKEN | Bearer token | Yes |

## Examples

### Basic Usage

```bash
curl -X GET 'https://platform.enjin.io/api/project/123/team' -H 'Authorization: Bearer eyJ...'
```

### Advanced Usage

```bash
curl -X GET 'https://platform.enjin.io/api/project/123/team' -H 'Authorization: Bearer eyJ...' -H 'Accept: application/json'
```

## Expected Output

JSON array: [{"id":1,"email":"user1@example.com"}, {"id":2,"email":"user2@example.com"}], with count exceeding plan limit.

## Related

- [[Related Procedure|procedures/Exploit-Enjin-Invitation-Race-Condition]]
