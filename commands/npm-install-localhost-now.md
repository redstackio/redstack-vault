---
data: npm install localhost-now@1.0.2
tags:
  - installation
  - npm
type: command
output: null
executor: bash
platforms:
  - Node.js
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.648Z'
id: e8bf2b2b-78da-46bf-952f-c0a902308999
verified: false
validated: true
submitted: true
---
# npm-install-localhost-now

## Command

```bash
npm install localhost-now@1.0.2
```

## Description

Installs the specific vulnerable version 1.0.2 of the localhost-now Node.js module from the npm registry, enabling setup for path traversal exploitation testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `install` | npm subcommand for installation | Yes |
| `localhost-now@1.0.2` | Package name and version specifier | Yes |

## Examples

### Basic Usage

```bash
npm install localhost-now@1.0.2
```

### Advanced Usage

```bash
npm install localhost-now@1.0.2 --save-dev
```

## Expected Output

Installation progress: "added 1 package in Xs". No errors; module in node_modules.

## Related

- [[Related Procedure|procedures/Install-localhost-now-Module]]
