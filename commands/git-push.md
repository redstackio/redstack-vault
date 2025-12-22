---
id: cmd-git-push
data: git push
tags:
  - git
  - push
type: command
output: Push success
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.119Z'
verified: false
validated: true
submitted: true
---
# git-push

## Command

```bash
git push
```

## Description

Pushes the committed wiki changes to the remote GitLab repository, making the payload available for rendering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
git push
```

### Advanced Usage

```bash
git push origin master
```

## Expected Output

'Writing objects: 100% ... To https://gitlab.com/user/project.wiki.git
   abc1234..def5678  master -> master'

## Related

- [[commands/git-commit-wiki]]
- [[procedures/Deploy-Wiki-Payload-via-Git]]
