---
id: cmd-npm-install-git-lib
data: npm i git-lib
tags:
  - installation
  - npm
type: command
output: >-
  Installation logs and confirmation of git-lib version 1.6.0 being added to
  node_modules
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.792Z'
verified: false
validated: true
submitted: true
---
# npm-install-git-lib

## Command

```bash
npm i git-lib
```

## Description

Installs the git-lib Node.js package from the npm registry, specifically version 1.6.0 which contains the RCE vulnerability. Use this in a Node.js project directory to add the vulnerable dependency for exploitation testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Short for 'install'; installs the package without saving to package.json if not in a project | Yes |
| `git-lib` | The package name to install | Yes |

## Examples

### Basic Usage

```bash
npm i git-lib
```

Installs the latest version (1.6.0 at time of vuln) into node_modules.

### Advanced Usage

```bash
npm i git-lib@1.6.0
```

Pins to the exact vulnerable version.

## Expected Output

npm WARN deprecated git-lib@1.6.0: ... (if any)
+ git-lib@1.6.0
added 1 package in Xs

## Related

- [[Related Procedure|procedures/Exploit-git-lib-RCE-via-Command-Injection]]
