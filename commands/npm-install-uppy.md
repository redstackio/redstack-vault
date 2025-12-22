---
data: npm install
tags:
  - install
  - dependencies
type: command
executor: bash
platforms:
  - Node.js
id: 292d0bc4-a495-485d-a282-e3159bfd0ce8
created_at: '2025-12-14T03:16:14.062Z'
updated_at: '2025-12-14T03:16:14.062Z'
verified: false
validated: true
submitted: true
---
# npm-install-uppy

## Command

```bash
npm install
```

## Description

Installs the Node.js dependencies listed in package.json for the Uppy project, including dev dependencies needed for the dashboard.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Installs from package.json | No |

## Examples

### Basic Usage

```bash
npm install
```

### Advanced Usage

```bash
npm install --production
```

## Expected Output

Lists installed packages and completes without errors, creating node_modules directory.

## Related

- [[Related Procedure: Setup-Uppy-Development-Environment]]
