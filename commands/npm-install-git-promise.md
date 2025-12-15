---
id: cmd-uuid-1
data: npm i git-promise
tags:
  - installation
  - npm
type: command
output: >-
  Installation logs and confirmation of git-promise@0.3.1 being added to
  node_modules
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.752Z'
verified: false
validated: true
submitted: true
---
# npm-install-git-promise

## Command

```bash
npm i git-promise
```

## Description

Installs the vulnerable git-promise Node.js module from the npm registry, specifically version 0.3.1, to set up the environment for RCE exploitation demonstration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Short for --install; installs the specified package | Yes |
| `git-promise` | The package name to install | Yes |

## Examples

### Basic Usage

```bash
npm i git-promise
```

### Advanced Usage

```bash
npm i git-promise@0.3.1 --save
```

## Expected Output

npm notice created a lockfile as package-lock.json. You should commit this file.
npm WARN enoent ENOENT: no such file or directory, open '/path/to/package.json'
npm WARN project@1.0.0 No description
npm WARN project@1.0.0 No repository field.

added 1 package from 1 contributor and audited 1 package in 2s

found 0 vulnerabilities

## Related

- [[Related Procedure: Install-and-Execute-git-promise-RCE-POC]]
