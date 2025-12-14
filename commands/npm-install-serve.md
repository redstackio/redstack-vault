---
data: npm i serve
tags:
  - installation
  - npm
type: command
executor: bash
platforms:
  - Node.js
id: 1271808d-65ec-4c99-966b-ab1ed81c09fa
created_at: '2025-12-14T03:15:41.877Z'
updated_at: '2025-12-14T03:15:41.877Z'
verified: false
validated: true
submitted: true
---
# npm-install-serve

## Command

```bash
npm i serve
```

## Description

Installs the serve package from the npm registry into the local node_modules directory, used to set up the vulnerable static server for XSS exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Alias for install flag | Yes |
| `serve` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm i serve
```

### Advanced Usage

```bash
npm i serve@7.0.1
```

## Expected Output

Installation logs: "added 1 package in X ms" and confirmation of serve@version in node_modules.

## Related

- [[Related Procedure|procedures/Install-Serve-Module]]
