---
id: cmd-uuid-placeholder-001
data: git checkout -b exploit-branch
tags:
  - git
  - branch
type: command
output: null
executor: bash
platforms:
  - Git
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.148Z'
verified: false
validated: true
submitted: true
---
# git-checkout-branch

## Command

```bash
git checkout -b exploit-branch
```

## Description

Creates and switches to a new Git branch named 'exploit-branch', used in the procedure to set up an ambiguous reference branch for commit smuggling exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b` | Create a new branch and switch to it | Yes |
| `branch-name` | Name of the branch to create (e.g., exploit-branch) | Yes |

## Examples

### Basic Usage

```bash
git checkout -b exploit-branch
```

### Advanced Usage

```bash
git checkout -b exploit-branch origin/main
```

## Expected Output

Switched to a new branch 'exploit-branch'. No changes to files, but ready for commits.

## Related

- [[Related Procedure|procedures/Exploit-Git-Reference-Ambiguity-for-Commit-Smuggling]]
