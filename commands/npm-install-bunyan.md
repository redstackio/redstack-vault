---
id: cmd-uuid-1
data: npm install bunyan@1.8.12
tags:
  - installation
type: command
output: null
executor: bash
platforms:
  - Node.js
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.160Z'
verified: false
validated: true
submitted: true
---
# npm-install-bunyan

## Command

```bash
npm install bunyan@1.8.12
```

## Description

Installs the specific vulnerable version of the bunyan Node.js logging module from the npm registry, enabling access to the CLI tool for command injection exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `install` | npm subcommand for package installation | Yes |
| `bunyan@1.8.12` | Package name and version specifier | Yes |

## Examples

### Basic Usage

```bash
npm install bunyan@1.8.12
```

### Advanced Usage

```bash
npm install bunyan@1.8.12 --save
```

## Expected Output

Installation logs showing download progress, dependency resolution, and confirmation: "added 1 package in X ms". The node_modules/bunyan directory is created with the bin/bunyan script.

## Related

- [[Related Procedure|procedures/Install-Bunyan-Module]]
