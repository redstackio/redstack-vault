---
data: node app.js
tags:
  - node.js
  - execution
type: command
output: >-
  For normal run: fetchById success [ RowDataPacket { username: 'noob',
  password: 'noob' } ]; For malicious: fetchById success [ RowDataPacket {
  username: 'admin', password: 'admin' }, RowDataPacket { username: 'user',
  password: 'user' }, RowDataPacket { username: 'noob', password: 'noob' } ]
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.053Z'
id: b4dcf707-45cb-40b5-8409-61514d5e02fd
verified: false
validated: true
submitted: true
---
# node-run-app

## Command

```bash
node app.js
```

## Description

Executes the Node.js app.js script to run query-mysql fetchById, either normally or with injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| node | Runtime | Yes |
| app.js | Script file | Yes |

## Examples

### Basic Usage

```bash
node app.js
```

## Expected Output

Console logs query results based on fetchById inputs.

## Related

- [[Related Procedure|procedures/Demonstrate-Normal-Data-Fetch]]
- [[Related Procedure|procedures/Exploit-SQL-Injection-with-Malicious-Input]]
