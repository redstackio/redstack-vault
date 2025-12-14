---
data: sudo npm
tags:
  - npm
  - sudo
  - escalation
type: command
output: Depends on npm subcommand
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.375Z'
id: bd1ad9a2-f505-4e33-9928-4db496e6941d
verified: false
validated: true
submitted: true
---
# sudo-npm

## Command

```bash
sudo npm
```

## Description

Runs npm with root privileges via sudo, loading .npmrc from the current directory and executing onload-scripts as root.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Subcommand | e.g., install, help | Varies |

## Examples

### Basic Usage

```bash
sudo npm
```

### With Subcommand

```bash
sudo npm ls
```

## Expected Output

Output based on the subcommand provided.

## Related

- [[commands/sudo-npm-i-g-eslint]]
- [[procedures/Load-and-Execute-onload-Script]]
