---
id: edcbb4cb-0025-4b64-8a16-55b4fd0f5763
name: git-add-all
type: command
executor: bash
data: git add -A .
output: null
created_at: '2025-12-11T06:10:13.246Z'
updated_at: '2025-12-11T06:10:13.246Z'
platforms:
  - Linux
tags:
  - git
  - add
verified: false
validated: true
submitted: true
---

# git-add-all

## Command

```bash
git add -A .
```

## Description

Stages all changes in the repository for commit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -A | Add all changes | Yes |

## Examples

### Basic Usage

```bash
git add -A .
```

## Expected Output

Files staged

## Related

- [[commands/git-commit-message]]
- [[procedures/Push-Changes-and-Trigger-Wiki-Rendering]]
