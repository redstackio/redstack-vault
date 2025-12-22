---
data: >-
  const query = require('query-mysql'); query.configure({ 'host':'127.0.0.1',
  'user':'root', 'password':'root', 'database':'test' });
  query.base.fetchById('users','noob','username',(msg, res)=>{ console.log(msg,
  res) });
tags:
  - node.js
  - query
type: command
output: 'fetchById success [ RowDataPacket { username: ''noob'', password: ''noob'' } ]'
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.055Z'
id: eea2c2bf-3d63-46fd-969e-89619a742c1c
verified: false
validated: true
submitted: true
---
# node-normal-fetch

## Command

```javascript
const query = require('query-mysql'); query.configure({ 'host':'127.0.0.1', 'user':'root', 'password':'root', 'database':'test' }); query.base.fetchById('users','noob','username',(msg, res)=>{ console.log(msg, res) });
```

## Description

Configures query-mysql and fetches a single user by username 'noob' using fetchById, demonstrating normal operation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| host | MySQL host | Yes |
| user | DB user | Yes |
| fetchById | Function call | Yes |
| id | 'noob' | Yes |

## Examples

### Basic Usage

```javascript
query.base.fetchById('users','noob','username', callback);
```

## Expected Output

Single record for 'noob'.

## Related

- [[Related Procedure|procedures/Demonstrate-Normal-Data-Fetch]]
