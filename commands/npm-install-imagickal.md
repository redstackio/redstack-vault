---
id: cmd-uuid-1
data: npm i imagickal@4.2.0
tags:
  - installation
  - npm
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.178Z'
verified: false
validated: true
submitted: true
---
# npm-install-imagickal

## Command

```bash
npm i imagickal@4.2.0
```

## Description

Installs the specific vulnerable version (4.2.0) of the imagickal Node.js package from the npm registry, enabling exploitation of its command injection vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Install mode flag | Yes |
| `imagickal@4.2.0` | Package name and version | Yes |

## Examples

### Basic Usage

```bash
npm i imagickal@4.2.0
```

### Advanced Usage

```bash
npm i imagickal@4.2.0 --save
```

## Expected Output

Installation logs such as "added 1 package in X ms" and updates to package-lock.json, confirming the vulnerable module is now available.

## Related

- [[Related Procedure: Install-Vulnerable-imagickal-Module]]
