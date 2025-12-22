---
id: cmd-003
data: node poc.js
tags:
  - node
  - poc
  - execution
type: command
output: null
executor: bash
platforms:
  - Windows
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.560Z'
verified: false
validated: true
submitted: true
---
# run-node-poc-script

## Command

```bash
node poc.js
```

## Description

Executes a Node.js proof-of-concept script that triggers the RCE vulnerability in treekill by calling the kill function with a command-injecting PID string on Windows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `poc.js` | Path to the PoC JavaScript file | Yes |

## Examples

### Basic Usage

```bash
node poc.js
```

### Advanced Usage

```bash
node poc.js --trace-warnings
```

## Expected Output

Minimal console output, possibly an error from taskkill on invalid PID, but no explicit success message; success confirmed by file creation.

## Related

- [[Related Procedure|procedures/Execute-treekill-RCE-PoC]]
