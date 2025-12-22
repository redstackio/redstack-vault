---
data: >-
  git clone $1 && cd $(basename $1 .git) && git add . && git commit -m "$2" &&
  git push origin main
tags:
  - git
  - deployment
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:31.245Z'
id: cc81476f-388d-479f-80fb-11fb59593158
verified: false
validated: true
submitted: true
---
# git-clone-push

## Command

```bash
git clone $1 && cd $(basename $1 .git) && git add . && git commit -m "$2" && git push origin main
```

## Description

Clones a GitHub repo, adds files, commits, and pushes to deploy content for subdomain takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $1 | Repo URL | Yes |
| $2 | Commit message | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/user/repo.git && cd repo && echo 'content' > file && git add . && git commit -m 'deploy' && git push
```

### Advanced Usage

Full chain as above.

## Expected Output

Git output confirming push, e.g., "To https://github.com/user/repo.git ..."

## Related

- [[Related Procedure]]
