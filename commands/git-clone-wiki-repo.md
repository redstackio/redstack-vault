---
id: cmd-git-clone-wiki
data: 'git clone git@gitlab.example.com:root/proj1.wiki.git'
tags:
  - git
  - clone
type: command
output: |-
  Cloning into 'proj1.wiki'...
  remote: Enumerating objects: 3, done.
  remote: Counting objects: 100% (3/3), done.
  remote: Compressing objects: 100% (2/2), done.
  Writing objects: 100% (3/3), 243 bytes | 243.00 KiB/s, done.
  Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.024Z'
verified: false
validated: true
submitted: true
---
# git-clone-wiki-repo

## Command

```bash
git clone git@gitlab.example.com:root/proj1.wiki.git
```

## Description

Clones a GitLab wiki repository locally using SSH URL, obtaining a working copy for modifications like adding exploit files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| git@gitlab.example.com:root/proj1.wiki.git | SSH URL of the wiki repo | Yes |

## Examples

### Basic Usage

```bash
git clone git@gitlab.example.com:root/proj1.wiki.git
```

### Advanced Usage

```bash
git clone https://gitlab.example.com/root/proj1.wiki.git
```
(Use HTTPS if SSH not available)

## Expected Output

Cloning into 'proj1.wiki'...
Repository cloned with initial files.

## Related

- [[commands/git-add-commit-push]]
- [[procedures/Clone-GitLab-Wiki-Repository]]
