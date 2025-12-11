---
id: f03fd9d8-14c4-4137-b010-613f55afc52c
name: npm-publish-package
type: command
executor: bash
data: npm publish
output: null
created_at: '2025-12-11T03:48:06.047Z'
updated_at: '2025-12-11T03:48:06.047Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - npm
  - package-management
verified: false
validated: true
submitted: true
---

# npm-publish-package

## Command

```bash
npm publish
```

## Description

Publishes the current package to the npm registry, making it available for installation. Requires a valid npm account and login.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Publishes the package in the current directory | No |

## Examples

### Basic Usage

```bash
npm publish
```

### Advanced Usage

```bash
npm publish --access public
```

## Expected Output

Confirmation message with the published package version and registry URL.

## Related

- [[commands/npm-init-package]]
- [[procedures/Register-Packages-on-Public-npm-Registry]]
