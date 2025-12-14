---
id: cmd-uuid-npm-install
data: npm i object-path-set@1.0.0
tags:
  - installation
  - npm
  - vulnerable-module
type: command
output: null
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.525Z'
verified: false
validated: true
submitted: true
---
# npm-install-object-path-set

## Command

```bash
npm i object-path-set@1.0.0
```

## Description

This command installs the vulnerable object-path-set module version 1.0.0 using npm, setting up the environment for prototype pollution exploitation in Node.js applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Shorthand for 'install'; fetches and adds the package | Yes |
| `object-path-set@1.0.0` | Specifies the package name and exact vulnerable version | Yes |

## Examples

### Basic Usage

```bash
npm i object-path-set@1.0.0
```

### Advanced Usage

```bash
npm i object-path-set@1.0.0 --save
```

> Adds to package.json dependencies.

## Expected Output

"added 1 package, and audited X packages in Xs" followed by installation logs; module appears in node_modules.

## Related

- [[Related Procedure|procedures/Exploit-Prototype-Pollution-in-object-path-set]]
