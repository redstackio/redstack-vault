---
id: b0763f09-8a13-4841-b2be-1bccd47d4449
name: npm-init-package
type: command
executor: bash
data: npm init -y
output: null
created_at: '2025-12-11T03:48:06.048Z'
updated_at: '2025-12-11T03:48:06.048Z'
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

# npm-init-package

## Command

```bash
npm init -y
```

## Description

Initializes a new npm package with default settings, creating a package.json file without interactive prompts. Used when preparing to publish a new package.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-y` | Accept defaults without prompting | No |

## Examples

### Basic Usage

```bash
npm init -y
```

### Advanced Usage

```bash
npm init --scope=@organization
```

## Expected Output

Creates a package.json file with default values, ready for editing and publishing.

## Related

- [[commands/npm-publish-package]]
- [[procedures/Register-Packages-on-Public-npm-Registry]]
