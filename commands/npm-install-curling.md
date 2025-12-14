---
id: cmd-npm-install-001
name: npm-install-curling
type: command
executor: bash
data: npm i curling
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.411Z'
platforms:
  - Node.js
tags:
  - installation
  - npm
verified: false
validated: true
submitted: true
---

# npm-install-curling

## Command

```bash
npm i curling
```

## Description

This command installs the curling Node.js module (version 1.1.0, vulnerable to command injection) from the npm registry into the local project, enabling its use in scripts for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Install mode (shortcut for --save) | Yes |
| `curling` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm i curling
```

### Advanced Usage

```bash
npm i curling@1.1.0 --save-dev
```

## Expected Output

Installation logs showing package download, dependency resolution, and confirmation: "added 1 package in X s". The node_modules/curling directory is created.

## Related

- [[Related Procedure|procedures/Install-Vulnerable-Curling-Module]]
