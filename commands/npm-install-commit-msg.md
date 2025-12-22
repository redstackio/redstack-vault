---
id: cmd-uuid-1
data: npm i commit-msg@0.2.3 -g
tags:
  - installation
  - npm
type: command
output: Installation logs and success message
executor: bash
platforms:
  - Linux
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.312Z'
verified: false
validated: true
submitted: true
---
# npm-install-commit-msg

## Command

```bash
npm i commit-msg@0.2.3 -g
```

## Description

Installs the vulnerable commit-msg package version 0.2.3 globally using npm, making the bin/validate script available for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Install flag (alias for install) | Yes |
| `commit-msg@0.2.3` | Package name and vulnerable version | Yes |
| `-g` | Global installation flag | Yes |

## Examples

### Basic Usage

```bash
npm i commit-msg@0.2.3 -g
```

### Advanced Usage

```bash
npm i commit-msg@0.2.3 -g --save-dev
```

## Expected Output

npm logs showing download, installation, and "added 1 package" success message.

## Related

- [[commands/git-init]]
- [[procedures/Install-Vulnerable-commit-msg-Module]]
