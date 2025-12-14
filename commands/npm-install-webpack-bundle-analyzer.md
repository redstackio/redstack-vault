---
data: npm i webpack-bundle-analyzer
tags:
  - installation
  - npm
type: command
output: Installation logs and confirmation
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:36.951Z'
id: 3f74b967-9521-43c4-bd2a-8a3d20308015
verified: false
validated: true
submitted: true
---
# npm-install-webpack-bundle-analyzer

## Command

```bash
npm i webpack-bundle-analyzer
```

## Description

Installs the webpack-bundle-analyzer package via npm, specifically version 3.0.3 for vulnerability reproduction, adding it to the local node_modules and package.json.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Install flag (short for install) | Yes |
| `webpack-bundle-analyzer` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm i webpack-bundle-analyzer
```

### Advanced Usage

```bash
npm i webpack-bundle-analyzer@3.0.3
```

## Expected Output

npm notice created a lockfile as package-lock.json. You should commit this file.
+ webpack-bundle-analyzer@3.0.3
added 1 package in X ms

## Related

- [[commands/npm-install-poc]]
- [[procedures/Install-Vulnerable-webpack-bundle-analyzer]]
