---
type: command
executor: bash
data: npm update $_PACKAGE_NAME
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

# npm-update-package

## Command

```bash
npm update $_PACKAGE_NAME
```

## Description

Updates a Node.js package to the latest version available in the registry. In dependency confusion, this pulls the attacker's higher-version malicious package.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PACKAGE_NAME | The name of the package to update (e.g., internal-auth-lib) | Yes |
| -g | Update globally | No |

## Examples

### Basic Usage

```bash
npm update internal-auth-lib
```

### Global Update

```bash
npm update -g internal-auth-lib
```

## Expected Output

added 1 package, removed 0 packages, and updated 1 package in 2s

Postinstall scripts execute on update.

## Related

- [[commands/npm-install-package]]
