---
id: cmd-001
data: npm i public
tags:
  - installation
  - npm
type: command
output: Installation logs and confirmation of module installation in node_modules
executor: bash
platforms:
  - Node.js
  - macOS
created_at: '2024-01-01T12:00:00Z'
updated_at: '2025-12-14T03:16:02.751Z'
verified: false
validated: true
submitted: true
---
# npm-i-public

## Command

```bash
npm i public
```

## Description

Installs the 'public' Node.js module from the npm registry, used to set up the vulnerable static file server for XSS exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| i | Install flag (shortcut for --save) | Yes |
| public | Module name to install | Yes |

## Examples

### Basic Usage

```bash
npm i public
```

### Advanced Usage

```bash
npm i public@0.1.3
```

## Expected Output

npm WARN deprecated ... (if any), then "added 1 package in X s", with node_modules/public created.

## Related

- [[Related Procedure|procedures/Install-and-Run-Vulnerable-Public-Module]]
