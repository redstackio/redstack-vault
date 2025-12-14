---
data: node --experimental-permission --allow-fs-read=/tmp/
tags:
  - node.js
  - setup
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.388Z'
id: 87761664-5c66-4bc0-86fc-a9ea1d61a1fb
verified: false
validated: true
submitted: true
---
# node-enable-permissions

## Command

```bash
node --experimental-permission --allow-fs-read=/tmp/
```

## Description

Starts Node.js with the experimental permission model enabled and restricts file system reads to the /tmp directory, setting up a sandboxed environment for testing path traversal bypasses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--experimental-permission` | Enables the experimental permission model | Yes |
| `--allow-fs-read=/tmp/` | Limits FS reads to /tmp and subdirectories | Yes |

## Examples

### Basic Usage

```bash
node --experimental-permission --allow-fs-read=/tmp/
```

### Advanced Usage

```bash
node --experimental-permission --allow-fs-read=/tmp/ script.js
```

## Expected Output

Node.js REPL prompt (>) or script execution begins. Attempts to read outside /tmp fail with permission errors.

## Related

- [[commands/overwrite-path-resolve]]
- [[procedures/Enable-Node.js-Experimental-Permission-Model]]
