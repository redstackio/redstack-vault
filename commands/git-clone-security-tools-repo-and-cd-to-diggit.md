---
id: 4710ed81-67fd-46dd-952a-77eefdd8b755
name: git-clone-security-tools-repo-and-cd-to-diggit
type: command
executor: bash
data: |
  git clone https://github.com/bl4de/security-tools/ && cd security-tools/diggit
output: null
created_at: '2023-04-06T03:55:59.928786+00:00'
updated_at: '2023-04-10T20:33:56.614609+00:00'
platforms:
  - Linux
tags:
  - git
  - clone
  - setup
verified: true
validated: true
---

# git-clone-security-tools-repo-and-cd-to-diggit

## Command

```bash
git clone https://github.com/bl4de/security-tools/ && cd security-tools/diggit
```

## Description

This command clones the bl4de/security-tools GitHub repository, which contains the diggit.py tool, and changes the current directory to the diggit subdirectory for immediate use.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/bl4de/security-tools/ | URL of the repository to clone | Yes |
| security-tools/diggit | Target directory after clone | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/bl4de/security-tools/ && cd security-tools/diggit
```

### Advanced Usage

If the repository is private, add authentication:

```bash
git clone https://username:token@github.com/bl4de/security-tools/ && cd security-tools/diggit
```

## Expected Output

Cloning into 'security-tools'...
remote: Enumerating objects: X, done.
remote: Counting objects: 100% (X/X), done.
remote: Compressing objects: 100% (X/X), done.
remote: Total X (delta X), reused X (delta X), pack-reused 0
Receiving objects: 100% (X/X), X MiB | X MiB/s, done.
Resolving deltas: 100% (X/X), done.

(Directory change is silent, confirm with pwd showing /path/to/security-tools/diggit)

## Related

- [[procedures/Download-Git-Repository-Object-Using-Diggit]]
- [[tools/diggit]]
