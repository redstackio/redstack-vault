---
id: 34c25117-0928-40fa-9e3c-70a4fb30ebb4
name: git-commit-changes
type: command
executor: bash
data: git commit -m "page1.rmd"
output: null
created_at: '2025-12-09T00:20:45.064Z'
updated_at: '2025-12-09T00:20:45.064Z'
platforms:
  - Linux
tags:
  - git
  - commit
verified: false
validated: true
submitted: true
---

# git-commit-changes

## Command

```bash
git commit -m "page1.rmd"
```

## Description

Commits staged changes with a message.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m` | Commit message flag | Yes |
| `"page1.rmd"` | Message text | Yes |

## Examples

### Basic Usage

```bash
git commit -m "page1.rmd"
```

## Expected Output

Commits changes successfully.

## Related

- #git-push-changes
- [[Add Malicious RMD File to Wiki]]
