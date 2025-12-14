---
data: npm install stattic
tags:
  - installation
  - npm
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.634Z'
id: 7b3f072b-e58c-4698-bcb1-9c3d1374be43
verified: false
validated: true
submitted: true
---
# npm-install-stattic

## Command

```bash
npm install stattic
```

## Description

Installs the 'stattic' Node.js module from the npm registry, defaulting to the latest version (0.2.3 in vulnerable context), adding it to node_modules and updating package.json.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `stattic` | Module name to install | Yes |

## Examples

### Basic Usage

```bash
npm install stattic
```

### Advanced Usage

```bash
npm install stattic@0.2.3
```

## Expected Output

Installation logs such as "added 1 package in Xms" and creation of node_modules/stattic directory.

## Related

- [[Related Procedure: Install-Vulnerable-Stattic-Module]]
