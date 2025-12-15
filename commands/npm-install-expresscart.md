---
id: cmd-004
data: npm install
tags:
  - npm
  - install
  - dependencies
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:27:23.109Z'
verified: false
validated: true
submitted: true
---
# npm-install-expresscart

## Command

```bash
npm install
```

## Description

Installs Node.js dependencies for the express-cart project, including Express framework and MongoDB drivers, preparing the environment for the vulnerable application.

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
npm install --save-dev
```

## Expected Output

added 150 packages, and audited 151 packages in 10s. node_modules created.

## Related

- [[commands/change-to-expresscart-directory]]
- [[procedures/Local-Setup-of-Express-Cart-Application]]
