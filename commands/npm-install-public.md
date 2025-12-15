---
id: cmd-uuid-1
data: npm install public
tags:
  - installation
  - npm
type: command
output: Installation logs and confirmation of package installation in node_modules
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.788Z'
verified: false
validated: true
submitted: true
---
# npm-install-public

## Command

```bash
npm install public
```

## Description

Installs the 'public' Node.js module from the npm registry, downloading version 0.1.2 which contains the path traversal vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `public` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm install public
```

### Advanced Usage

```bash
npm install public@0.1.2
```

## Expected Output

Package resolution and installation logs, ending with 'added 1 package in X ms', and creation of node_modules/public directory.

## Related

- [[Related Procedure|procedures/Install-Vulnerable-Public-Module]]
