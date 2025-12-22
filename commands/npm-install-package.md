---
type: command
executor: bash
data: npm install $_PACKAGE_NAME
output: null
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - package-management
  - node
verified: true
validated: true
---

# npm-install-package

## Command

```bash
npm install $_PACKAGE_NAME
```

## Description

Installs a Node.js package and its dependencies from the npm registry. Resolves the highest version matching the name unless specified otherwise, making it vulnerable to dependency confusion if private packages lack scopes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PACKAGE_NAME | The name of the package to install (e.g., internal-auth-lib) | Yes |
| -g | Install globally | No |
| --registry $_URL | Custom registry URL | No |

## Examples

### Basic Usage

```bash
npm install internal-auth-lib
```

### Global Install

```bash
npm install -g internal-auth-lib
```

## Expected Output

added 1 package, and audited 1 package in 2s

Postinstall scripts may run, producing additional logs or executing code.

## Related

- [[commands/npm-update-package]]
- [[commands/npm-uninstall-package]]
