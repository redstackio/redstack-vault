---
data: npm run build
tags:
  - build
  - npm
  - webpack
type: command
output: >-
  Webpack Bundle Analyzer is started at http://127.0.0.1:8888\nUse Ctrl+C to
  close it
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:36.914Z'
id: f5e609c4-df05-4d30-9991-817c529cd5c0
verified: false
validated: true
submitted: true
---
# npm-run-build

## Command

```bash
npm run build
```

## Description

Runs the build script in package.json, using webpack to compile with malicious module names and automatically start the analyzer on generated stats.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `run` | Flag to execute npm scripts | Yes |
| `build` | Script name defined in package.json | Yes |

## Examples

### Basic Usage

```bash
npm run build
```

### Advanced Usage

```bash
npm run build -- --mode production
```

## Expected Output

> poc-webpack-bundle-analyzer@1.0.0 build
> webpack && webpack-bundle-analyzer dist/stats.json

Webpack Bundle Analyzer is started at http://127.0.0.1:8888

## Related

- [[commands/node-run-analyzer]]
- [[procedures/Reproduce-with-Git-Clone-and-Build]]
