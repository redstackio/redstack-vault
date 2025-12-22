---
id: c264f6d6-9de4-4fac-83bd-ab95c3f268d7
name: git-add-all-changes
type: command
executor: bash
data: git add -A .
output: null
created_at: '2025-12-09T00:20:45.059Z'
updated_at: '2025-12-09T00:20:45.059Z'
platforms:
  - Linux
tags:
  - git
  - add
verified: false
validated: true
submitted: true
---

# git-add-all-changes

## Command

```bash
git add -A .
```

## Description

Stages all changes in the current directory for commit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-A` | Add all changes | Yes |
| `.` | Current directory | Yes |

## Examples

### Basic Usage

```bash
git add -A .
```

## Expected Output

Stages files for commit.

## Related

- #git-commit-changes
- [[Add Malicious RMD File to Wiki]]
