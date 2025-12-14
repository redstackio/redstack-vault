---
data: npm i mcstatic
tags:
  - installation
  - node-js
type: command
executor: bash
platforms:
  - Node.js
id: 9cb741c9-35ad-4dc9-9958-52f10d982b8a
created_at: '2025-12-14T17:26:16.785Z'
updated_at: '2025-12-14T17:26:16.785Z'
verified: false
validated: true
submitted: true
---
# npm-i-mcstatic

## Command

```bash
npm i mcstatic
```

## Description

Installs the mcstatic Node.js module from the npm registry, used as the initial step to set up the vulnerable static HTTP server for path traversal exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Install mode, shorthand for --save to add to package.json | Yes |
| `mcstatic` | Package name to install (vulnerable in v0.0.20) | Yes |

## Examples

### Basic Usage

```bash
npm i mcstatic
```

### Advanced Usage

```bash
npm i mcstatic@0.0.20 --save-dev
```

## Expected Output

Installation progress with lines like "added 1 package in 1s" and creation of node_modules/mcstatic directory.

## Related

- [[Related Procedure|procedures/Install-Vulnerable-mcstatic-Module]]
