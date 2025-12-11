---
id: e5ca0b5b-e12c-426e-8c90-c3b48e4b54eb
name: git-clone-wiki-repo
type: command
executor: bash
data: 'git clone git@gitlab-docker.local:root/proj1.wiki.git'
output: null
created_at: '2025-12-11T06:10:13.237Z'
updated_at: '2025-12-11T06:10:13.237Z'
platforms:
  - Linux
tags:
  - git
  - clone
verified: false
validated: true
submitted: true
---

# git-clone-wiki-repo

## Command

```bash
git clone git@gitlab-docker.local:root/proj1.wiki.git
```

## Description

Clones the wiki git repository for adding malicious files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| git@gitlab-docker.local:root/proj1.wiki.git | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone git@gitlab-docker.local:root/proj1.wiki.git
```

## Expected Output

Cloned repository

## Related

- [[commands/git-add-all]]
- [[procedures/Clone-Wiki-Repository-and-Add-Malicious-RMD-File]]
