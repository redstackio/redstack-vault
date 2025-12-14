---
data: npm i gity
tags:
  - installation
  - npm
type: command
output: Installation logs and successful install of gity@1.0.5
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.715Z'
id: 667cf176-644c-40c0-8409-2bae1fd40bfc
verified: false
validated: true
submitted: true
---
# npm-install-gity

## Command

```bash
npm i gity
```

## Description

Installs the vulnerable gity Node.js module from the npm registry, setting up the environment for RCE exploitation via command injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Install flag (short for --install) | Yes |
| `gity` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm i gity
```

### Advanced Usage

```bash
npm i gity@1.0.5 --save
```

## Expected Output

npm logs showing package resolution, download, and installation confirmation, e.g., 'added 1 package'.

## Related

- [[Related Procedure|procedures/Exploit-gity-RCE-with-Injected-Commands]]
