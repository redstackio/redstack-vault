---
id: cmd-uuid-2
data: >-
  node -e "const JSONbig = require('json-bigint'); console.log('Loaded:',
  JSONbig);"
tags:
  - node-js
  - require
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.298Z'
verified: false
validated: true
submitted: true
---
# node-require-module

## Command

```bash
node -e "const JSONbig = require('json-bigint'); console.log('Loaded:', JSONbig);"
```

## Description

Executes a Node.js one-liner to require and log the json-bigint module, verifying successful import of the vulnerable version.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-e` | Inline JavaScript code to execute | Yes |

## Examples

### Basic Usage

```bash
node -e "const JSONbig = require('json-bigint'); console.log('Loaded:', JSONbig);"
```

### Advanced Usage

```bash
node -e "const JSONbig = require('json-bigint'); console.log(JSONbig.parse('{}'));"
```

## Expected Output

"Loaded: [Function: parse]" or module object details, confirming no import errors.

## Related

- [[Related Procedure]]
