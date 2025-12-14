---
id: 123e4567-e89b-12d3-a456-426614174004
name: npm-install-resolve-path
type: command
executor: bash
data: npm install resolve-path@1.3.3
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.842Z'
platforms:
  - Windows
  - Node.js
tags:
  - setup
  - install
verified: false
validated: true
submitted: true
---

# npm-install-resolve-path

## Command

```bash
npm install resolve-path@1.3.3
```

## Description

Installs the specific vulnerable version of the resolve-path module using NPM for testing the path traversal issue.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @1.3.3 | Version specifier for the vulnerable release | Yes |

## Examples

### Basic Usage

```bash
npm install resolve-path@1.3.3
```

## Expected Output

NPM output showing installation success, with package added to node_modules.

## Related

- [[procedures/Install-Resolve-Path-Module]]
