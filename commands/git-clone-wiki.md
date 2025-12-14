---
id: cmd-git-clone-wiki
data: git clone <wiki-url>.wiki.git
tags:
  - git
  - clone
type: command
output: Cloning progress
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.124Z'
verified: false
validated: true
submitted: true
---
# git-clone-wiki

## Command

```bash
git clone <wiki-url>.wiki.git
```

## Description

Clones a GitLab project wiki repository, which uses the .wiki.git suffix, for local editing of wiki pages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<wiki-url>.wiki.git` | Full wiki repo URL (e.g., https://gitlab.com/user/project.wiki.git) | Yes |

## Examples

### Basic Usage

```bash
git clone https://gitlab.com/user/project.wiki.git
```

### Advanced Usage

```bash
git clone git@gitlab.com:user/project.wiki.git  # SSH
```

## Expected Output

'Cloning into 'project.wiki'' and fetch completion.

## Related

- [[commands/git-add-wiki]]
- [[procedures/Clone-Project-Wiki-Repository]]
