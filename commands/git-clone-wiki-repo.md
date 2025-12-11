---
id: 614655db-aa6d-48f9-af50-54d37ff8f9af
name: git-clone-wiki-repo
type: command
executor: bash
data: 'git clone git@gitlab-docker.local:root/proj1.wiki.git'
output: null
created_at: '2025-12-09T00:20:45.056Z'
updated_at: '2025-12-09T00:20:45.056Z'
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

Clones the GitLab Wiki repository to a local machine for modification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `git@gitlab-docker.local:root/proj1.wiki.git` | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone git@gitlab-docker.local:root/proj1.wiki.git
```

## Expected Output

Clones the repository successfully.

## Related

- #git-add-all-changes
- [[Clone and Modify GitLab Wiki Repository]]
