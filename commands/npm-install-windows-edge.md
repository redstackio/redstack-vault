---
data: npm i windows-edge
tags:
  - installation
  - npm
type: command
executor: bash
platforms:
  - Windows
  - Node.js
id: b31a1653-f657-424c-a8da-00691c8a22cd
created_at: '2025-12-14T17:23:20.040Z'
updated_at: '2025-12-14T17:23:20.040Z'
verified: false
validated: true
submitted: true
---
# npm-install-windows-edge

## Command

```bash
npm i windows-edge
```

## Description

Installs the windows-edge Node.js package from the npm registry, defaulting to version 1.0.1, which is vulnerable to command injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Install mode flag | Yes |
| `windows-edge` | Package name | Yes |

## Examples

### Basic Usage

```bash
npm i windows-edge
```

### Advanced Usage

```bash
npm i windows-edge@1.0.1
```

## Expected Output

Installation logs and confirmation of module installation in node_modules, e.g., 'added 1 package'.

## Related

- [[Related Procedure: Install-Vulnerable-windows-edge]]
