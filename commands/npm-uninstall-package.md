---
type: command
executor: bash
data: npm uninstall $_PACKAGE_NAME
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

# npm-uninstall-package

## Command

```bash
npm uninstall $_PACKAGE_NAME
```

## Description

Removes an installed Node.js package and its dependencies. Used in cleanup after simulating a dependency confusion install.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PACKAGE_NAME | The name of the package to remove (e.g., internal-auth-lib) | Yes |
| -g | Uninstall globally | No |

## Examples

### Basic Usage

```bash
npm uninstall internal-auth-lib
```

### Global Uninstall

```bash
npm uninstall -g internal-auth-lib
```

## Expected Output

removed 1 package

## Related

- [[commands/npm-install-package]]
