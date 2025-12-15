---
data: npm install glance
tags:
  - installation
type: command
output: Installation logs and confirmation of package installation in node_modules
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.665Z'
id: bb0a7997-e4c8-49e6-9d86-df9bc5a395cc
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

Installs the Glance Node.js module from the npm registry, setting up the vulnerable static file server for testing path traversal.

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

Logs showing download and installation, e.g., "added 1 package", with Glance in node_modules.

## Related

- [[procedures/Install-Vulnerable-Glance-Module]]
