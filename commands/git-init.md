---
id: cmd-git-init
data: git init
tags:
  - git
  - initialization
type: command
output: Initialized empty Git repository in /path/to/dir/.git/
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.782Z'
verified: false
validated: true
submitted: true
---
# git-init

## Command

```bash
git init
```

## Description

Initializes a new Git repository in the current directory, creating a .git subdirectory. Used here to set up a valid Git context for the git-lib module to avoid operational errors during exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `init` | Command to create an empty repository | Yes |

## Examples

### Basic Usage

```bash
git init
```

Creates the repo in the current folder.

### Advanced Usage

```bash
git init my-repo
```

Initializes in a named directory (not used here).

## Expected Output

Initialized empty Git repository in /current/dir/.git/

## Related

- [[Related Procedure|procedures/Exploit-git-lib-RCE-via-Command-Injection]]
