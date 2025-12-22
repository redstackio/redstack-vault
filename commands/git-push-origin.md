---
id: cmd-uuid-placeholder-003
data: git push origin exploit-branch
tags:
  - git
  - push
type: command
output: null
executor: bash
platforms:
  - Git
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.142Z'
verified: false
validated: true
submitted: true
---
# git-push-origin

## Command

```bash
git push origin exploit-branch
```

## Description

Pushes the local 'exploit-branch' to the remote origin repository, making it available for Pull Request creation in the GitHub Enterprise Server exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `remote` | Remote name (e.g., origin) | Yes |
| `branch` | Branch to push (e.g., exploit-branch) | Yes |

## Examples

### Basic Usage

```bash
git push origin exploit-branch
```

### Advanced Usage

```bash
git push origin exploit-branch --force
```

## Expected Output

To github.com:user/repo.git
 * [new branch]      exploit-branch -> exploit-branch
Branch 'exploit-branch' set up to track remote branch 'exploit-branch' from 'origin'.

## Related

- [[Related Procedure|procedures/Exploit-Git-Reference-Ambiguity-for-Commit-Smuggling]]
