---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
name: require-notevil
type: command
executor: javascript
data: var safeEval = require("notevil");
output: safeEval function object
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.357Z'
platforms:
  - Node.js
tags:
  - setup
  - nodejs
verified: false
validated: true
submitted: true
---

# require-notevil

## Command

```javascript
var safeEval = require("notevil");
```

## Description

Loads the notevil module in Node.js, assigning its safeEval function to a variable for restricted JavaScript evaluation. Use this as the initial setup for sandbox escape testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| notevil | npm package name for safe evaluation | Yes |

## Examples

### Basic Usage

```javascript
var safeEval = require("notevil");
```

### Advanced Usage

```javascript
const { safeEval } = require("notevil@1.3.2");
```

## Expected Output

A function object for safeEval, ready for payload execution. No console output unless errors occur.

## Related

- [[commands/console-log-safeeval]]
- [[procedures/Load-notevil-Module-for-SafeEval]]
