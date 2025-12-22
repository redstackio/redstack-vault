---
id: b656467b-e640-4edc-adbd-4485168f413b
name: git-log-all-branches
type: command
executor: bash
data: git log --all
output: >-
  commit 766c5f1a2f95e117244d9128bff7a579ca1d4968 (HEAD -> master,
  origin/master)

  Author: bob <bob@corp.net>

  Date:   Sat Oct 29 12:01:40 2018 +0530

      changed auth - potential secret mention

  commit c130757dbbefdb3af3966fbd5ca273496180dc913

  Author: bob <bob@corp.net>

  Date:   Sat Oct 29 11:56:32 2018 +0530

      added mysql config
created_at: '2019-10-16T22:13:26.097794+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - git
  - commit-messages
  - secrets
verified: true
validated: true
---

# git-log-all-branches

## Command

```bash
git log --all
```

## Description

This command lists commit history from all branches in the Git repository, focusing on messages that might inadvertently reveal sensitive information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--all` | Traverse all branches and tags | Yes |
| `--grep=<pattern>` | (Optional) Search commit messages for a pattern | No |

## Examples

### Basic Usage

```bash
git log --all
```

### Advanced Usage

```bash
git log --all --grep='password\|key'
```

Filter commit messages for potential secrets.

## Expected Output

```
commit 766c5f1a2f95e117244d9128bff7a579ca1d4968 (HEAD -> master, origin/master)
Author: bob <bob@corp.net>
Date:   Sat Oct 29 12:01:40 2018 +0530

    changed auth

commit c130757dbbefdb3af3966fbd5ca273496180dc913
Author: bob <bob@corp.net>
Date:   Sat Oct 29 11:56:32 2018 +0530

    added mysql
```

## Related

- [[procedures/Enumerate-Git-Repository-for-Secrets]]
- [[commands/git-log-with-patches]]
