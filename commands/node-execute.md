---
data: node poc.js
tags:
  - execute
  - node-js
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:23.918Z'
id: af3f1933-a861-4066-9521-86c57c5bc8cb
verified: false
validated: true
submitted: true
---
# node-execute

## Command

```bash
node poc.js
```

## Description

Executes a Node.js script (poc.js) that exploits the arpping module, triggering command injection during runtime.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `poc.js` | Path to the script file | Yes |

## Examples

### Basic Usage

```bash
node poc.js
```

### Advanced Usage

```bash
node --inspect poc.js
```

## Expected Output

Console output from arpping.ping() callback, potentially empty or with ping data; injected command executes without direct output.

## Related

- [[commands/npm-install]]
