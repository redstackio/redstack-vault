---
id: 26a2442d-1f72-4166-89fa-32d3d06bc8f9
name: git-clone-git-dumper-repository
type: command
executor: bash
data: 'git clone https://github.com/arthaud/git-dumper'
output: null
created_at: '2023-04-06T03:55:59.891741+00:00'
updated_at: '2023-04-10T20:33:54.555211+00:00'
platforms:
  - Linux
tags:
  - git
  - clone
  - installation
verified: true
validated: true
---

# git-clone-git-dumper-repository

## Command

```bash
git clone https://github.com/arthaud/git-dumper
```

## Description

This command clones the git-dumper tool repository from GitHub to the local machine, creating a 'git-dumper' directory with the necessary Python scripts for recovering exposed Git repositories.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/arthaud/git-dumper | Fixed URL of the git-dumper repository | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/arthaud/git-dumper
```

### With Specific Directory

```bash
git clone https://github.com/arthaud/git-dumper ./tools/git-dumper
```

## Expected Output

Cloning into 'git-dumper'...
remote: Enumerating objects: 50, done.
remote: Counting objects: 100% (50/50), done.
remote: Compressing objects: 100% (30/30), done.
remote: Total 50 (delta 20), reused 40 (delta 15)
Receiving objects: 100% (50/50), 10.00 KiB | 2.00 MiB/s, done.
Resolving deltas: 100% (20/20), done.

## Related

- [[procedures/Recover-Source-Code-from-Insecure-Git-Repository-Using-Git-Dumper]]
- [[tools/git-dumper]]
