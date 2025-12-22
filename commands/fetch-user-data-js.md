---
data: >-
  fetch('https://dust.tt/api/user',{method:'GET',headers:{'accept':'*/*','x-commit-hash':'41c0391'},credentials:'include'})
tags:
  - fetch
  - api
  - user
type: command
output: JSON with user data including workspaces and ID
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.386Z'
id: 53759654-d9f0-4f03-a827-411cf49ef8b4
verified: false
validated: true
submitted: true
---
# fetch-user-data-js

## Command

```javascript
fetch('https://dust.tt/api/user',{method:'GET',headers:{'accept':'*/*','x-commit-hash':'41c0391'},credentials:'include'})
```

## Description

Fetches the current user's data from Dust API using browser credentials to get workspaces and IDs for escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| method | GET | Yes |
| headers | Accept and commit hash | Yes |
| credentials | 'include' for cookies | Yes |

## Examples

### Basic Usage

```javascript
fetch('https://dust.tt/api/user',{method:'GET',headers:{'accept':'*/*','x-commit-hash':'41c0391'},credentials:'include'})
```

## Expected Output

JSON response with user object, including workspaces array.

## Related

- [[commands/promote-to-admin-js]]
