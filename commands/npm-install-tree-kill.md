---
data: npm i tree-kill@1.2.1
tags:
  - setup
  - npm
type: command
output: null
executor: bash
platforms:
  - Windows
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.644Z'
id: fee384b2-9431-4029-a4b7-46b1fda14fb1
verified: false
validated: true
submitted: true
---
# npm-install-tree-kill

## Command

```bash
npm i tree-kill@1.2.1
```

## Description

Installs the specific vulnerable version 1.2.1 of the tree-kill package using npm, preparing the environment for RCE exploitation in Node.js projects on Windows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Install flag (alias for install) | Yes |
| `tree-kill@1.2.1` | Package name and version | Yes |

## Examples

### Basic Usage

```bash
npm i tree-kill@1.2.1
```

### Advanced Usage

```bash
npm i tree-kill@1.2.1 --save
```

## Expected Output

Installation logs such as "added 1 package in X ms" and confirmation in node_modules/tree-kill.

## Related

- [[commands/npm-list-tree-kill]]
- [[procedures/Install-Vulnerable-tree-kill-Module]]
