---
id: cmd-ponse-install-001
data: npm i --save ponse@2.0.1
tags:
  - installation
  - npm
type: command
output: |-
  added 1 package, and audited X packages in Xs
  found 0 vulnerabilities
  (Updates package.json with "ponse": "^2.0.1")
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.636Z'
verified: false
validated: true
submitted: true
---
# install-ponse-module

## Command

```bash
npm i --save ponse@2.0.1
```

## Description

Installs the specific vulnerable version of the ponse Node.js module and saves it as a dependency in package.json. This is used to set up a reproducible environment for exploiting the path traversal vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Install mode | Yes |
| `--save` | Saves to package.json dependencies | Yes |
| `ponse@2.0.1` | Specifies the vulnerable version | Yes |

## Examples

### Basic Usage

```bash
npm i --save ponse@2.0.1
```

### Advanced Usage

```bash
npm i --save ponse@2.0.1 --registry https://registry.npmjs.org
```

## Expected Output

Installation confirmation, package added to node_modules, and package.json updated. No vulnerabilities reported for this specific version in basic audit.

## Related

- [[commands/start-ponse-server]]
- [[procedures/Install-Vulnerable-Ponse-Module]]
