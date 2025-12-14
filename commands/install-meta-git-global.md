---
id: 123e4567-e89b-12d3-a456-426614174011
name: install-meta-git-global
type: command
executor: bash
data: npm i meta-git -g
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.159Z'
platforms:
  - Linux
  - Node.js
tags:
  - installation
  - npm
verified: false
validated: true
submitted: true
---

# install-meta-git-global

## Command

```bash
npm i meta-git -g
```

## Description

Installs the meta-git Node.js package globally using npm, enabling the vulnerable clone command for RCE demonstration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| i | Install flag (alias for install) | Yes |
| -g | Global installation flag | Yes |
| meta-git | Package name | Yes |

## Examples

### Basic Usage

```bash
npm i meta-git -g
```

### Advanced Usage

```bash
npm i meta-git@1.1.2 -g
```

## Expected Output

Installation progress logs, ending with 'meta-git@1.1.2 installed'.

## Related

- [[Related Procedure: Install-Vulnerable-meta-git-Module]]
