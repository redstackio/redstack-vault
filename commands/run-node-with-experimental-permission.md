---
id: cmd-node-experimental-permission
data: node --experimental-permission script.js
tags:
  - nodejs
  - setup
  - permissions
type: command
output: >-
  Node.js process starts in permission-restricted mode; script executes without
  initial errors.
executor: bash
platforms:
  - Node.js
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.835Z'
verified: false
validated: true
submitted: true
---
# run-node-with-experimental-permission

## Command

```bash
node --experimental-permission script.js
```

## Description

Launches a Node.js script with the experimental permission system enabled, restricting file operations unless explicitly allowed. Used to set up a vulnerable environment for testing permission bypasses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--experimental-permission` | Enables the experimental permission model for file system controls | Yes |
| `script.js` | Path to the JavaScript file to execute | Yes |

## Examples

### Basic Usage

```bash
node --experimental-permission script.js
```

### Advanced Usage

```bash
node --experimental-permission --allow-fs-read=/safe/dir script.js
```

(Note: Omit --allow-fs-read for bypass testing.)

## Expected Output

The Node.js runtime starts, loads the script, and executes it. No permission errors on startup; subsequent file ops may appear restricted but can be bypassed.

## Related

- [[Related Procedure|procedures/Enable-Node.js-Experimental-Permission-Without-Read-Access]]
