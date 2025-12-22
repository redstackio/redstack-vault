---
id: 852c3413-e5fa-4358-b750-f9b4682838a5
name: git-reflog-with-patches
type: command
executor: bash
data: git reflog -p
output: |-
  root@kali:~# git reflog -p | grep password
  -spring.datasource.password=secretpassword
created_at: '2019-10-16T22:13:26.108552+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - git
  - reflog
  - secrets
verified: true
validated: true
---

# git-reflog-with-patches

## Command

```bash
git reflog -p
```

## Description

This command shows the Git reflog (reference log) with patch diffs (-p), revealing lost or reset commits that may contain secrets not visible in the standard history.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | Include patch/diff output for each reflog entry | Yes |
| `--all` | (Optional) Show all refs; default is current branch | No |

## Examples

### Basic Usage

```bash
git reflog -p
```

### Advanced Usage

```bash
git reflog -p | grep -i 'secret\|password\|key'
```

Search for common secret keywords in the reflog output.

## Expected Output

```
root@kali:~# git reflog -p | grep password
-spring.datasource.password=secretpassword
```

## Related

- [[procedures/Enumerate-Git-Repository-for-Secrets]]
- [[commands/git-log-with-patches]]
