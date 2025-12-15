---
data: npm i npm-git-publish
tags:
  - installation
  - npm
type: command
executor: bash
platforms:
  - Linux
  - Node.js
id: a49aacb3-8fac-4067-9224-3d97e4865dbd
created_at: '2025-12-14T17:23:20.086Z'
updated_at: '2025-12-14T17:23:20.086Z'
verified: false
validated: true
submitted: true
---
# npm-install-npm-git-publish

## Command

```bash
npm i npm-git-publish
```

## Description

Installs the npm-git-publish package from the npm registry, specifically targeting the vulnerable 0.2.4-beta version in this context to enable RCE exploitation via command injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Shorthand for install; adds to dependencies by default | Yes |
| `npm-git-publish` | Package name to install | Yes |

## Examples

### Basic Usage

```bash
npm i npm-git-publish
```

### Advanced Usage

```bash
npm i npm-git-publish@0.2.4-beta --save-dev
```

## Expected Output

Installation logs such as:

> npm notice created a lockfile as package-lock.json. You should commit this file.
> + npm-git-publish@0.2.4-beta
> added 1 package in 1s

Confirms download and placement in node_modules.

## Related

- [[Related Procedure|procedures/Install-Vulnerable-npm-git-publish-Module]]
