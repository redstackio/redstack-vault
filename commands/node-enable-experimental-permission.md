---
id: cmd-node-enable
data: node --experimental-permission --allow-fs-read=/tmp
tags:
  - setup
  - permission
type: command
output: Welcome to Node.js v20.8.1. Type ".help" for more information.
executor: bash
platforms:
  - Node.js
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:29.881Z'
verified: false
validated: true
submitted: true
---
---
id: cmd-node-enable
type: command
executor: bash
data: |
  node --experimental-permission --allow-fs-read=/tmp
output: "Welcome to Node.js v20.8.1. Type ".help" for more information."
created_at: 2024-01-01T00:00:00Z
updated_at: 2024-01-01T00:00:00Z
platforms: ["Node.js", "Linux"]
tags: ["setup", "permission"]
---

# node-enable-experimental-permission

## Command

```bash
node --experimental-permission --allow-fs-read=/tmp
```

## Description

Starts the Node.js REPL with the experimental permission model enabled and restricts file system read operations to the /tmp directory only.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--experimental-permission` | Enables the experimental permission model | Yes |
| `--allow-fs-read=/tmp` | Limits fs.read to /tmp directory | Yes |

## Examples

### Basic Usage

```bash
node --experimental-permission --allow-fs-read=/tmp
```

### Advanced Usage

```bash
node --experimental-permission --allow-fs-read=/tmp --allow-fs-write=/tmp
```

## Expected Output

Node.js REPL prompt appears, confirming the runtime is ready with restrictions applied.

## Related

- [[Related Procedure: Node-Enable-Experimental-Permission-Model]]
