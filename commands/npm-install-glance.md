---
id: cmd-uuid-1
data: npm install glance
tags:
  - installation
  - npm
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:15:46.954Z'
verified: false
validated: true
submitted: true
---
# npm-install-glance

## Command

```bash
npm install glance
```

## Description

Installs the Glance Node.js package using npm, setting up the vulnerable module for static file serving and XSS exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `glance` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm install glance
```

### Advanced Usage

```bash
npm install glance --save
```

## Expected Output

Installation logs, e.g., "added 5 packages from 3 contributors and audited 1 package in 2s", with glance in node_modules.

## Related

- [[commands/run-glance-server]]
- [[procedures/Install-Glance-Node-Module]]
