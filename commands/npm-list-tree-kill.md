---
data: npm list tree-kill
tags:
  - verification
  - npm
type: command
output: null
executor: bash
platforms:
  - Windows
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.621Z'
id: 1e046625-7a05-4433-b42c-dc2b1334b093
verified: false
validated: true
submitted: true
---
# npm-list-tree-kill

## Command

```bash
npm list tree-kill
```

## Description

Lists the installed version of the tree-kill package to verify the vulnerable version is present.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `tree-kill` | Package name to list | Yes |

## Examples

### Basic Usage

```bash
npm list tree-kill
```

### Advanced Usage

```bash
npm list tree-kill --depth=0
```

## Expected Output

"project@1.0.0 C:\project \ `-- tree-kill@1.2.1" confirming installation.

## Related

- [[commands/npm-install-tree-kill]]
- [[procedures/Install-Vulnerable-tree-kill-Module]]
