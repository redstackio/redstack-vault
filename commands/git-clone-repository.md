---
id: cmd-uuid-1
data: 'git clone git@gitlab.com:user/project'
tags:
  - git
  - clone
type: command
output: |-
  Cloning into 'project'...
  remote: Enumerating objects: 3, done.
  remote: Counting objects: 100% (3/3), done.
  ...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.330Z'
verified: false
validated: true
submitted: true
---
---

# git-clone-repository

## Command

```bash
git clone git@gitlab.com:user/project
```

## Description

Clones a GitLab repository to create a local working copy, essential for setting up project environments in attacks involving git manipulations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `git@gitlab.com:user/project` | SSH URL of the repository to clone | Yes |

## Examples

### Basic Usage

```bash
git clone git@gitlab.com:user/project
```

### Advanced Usage

```bash
git clone -b branch git@gitlab.com:user/project
```

## Expected Output

Directory created with repository contents and Git history initialized.

## Related

- [[commands/git-push-changes]]
- [[procedures/Initialize-GitLab-Project-and-Wiki-Repositories]]
