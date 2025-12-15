---
id: cmd-git-add-commit-push
data: git add -A . && git commit -m "page1.rmd" && git push
tags:
  - git
  - commit
  - push
type: command
output: |-
  [master abc1234] page1.rmd
   1 file changed, 10 insertions(+)
  To git@gitlab.example.com:root/proj1.wiki.git
     abc1234..def5678  master -> master
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.016Z'
verified: false
validated: true
submitted: true
---
# git-add-commit-push

## Command

```bash
git add -A . && git commit -m "page1.rmd" && git push
```

## Description

Stages all changes (-A .), commits with a message, and pushes to the remote wiki repo, uploading the malicious file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -A . | Add all changes recursively | Yes |
| -m "page1.rmd" | Commit message | Yes |

## Examples

### Basic Usage

```bash
git add -A . && git commit -m "Add exploit" && git push
```

### Advanced Usage

```bash
git add page1.rmd && git commit -m "Exploit update" && git push origin master
```

## Expected Output

Commit and push success messages indicating file uploaded.

## Related

- [[commands/git-clone-wiki-repo]]
- [[procedures/Commit-and-Push-Malicious-File-to-Wiki]]
