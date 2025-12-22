---
id: cmd-uuid-8
data: git add .
tags:
  - git
  - stage
type: command
output: ''
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.312Z'
verified: false
validated: true
submitted: true
---
---

# git-add-all

## Command

```bash
git add .
```

## Description

Stages all changes, including modified .gitmodules, for commit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `.` | All files in current directory | Yes |

## Examples

### Basic Usage

```bash
git add .
```

### Advanced Usage

```bash
git add -A
```

## Expected Output

All changes staged.

## Related

- [[commands/git-commit-message]]
- [[procedures/Inject-JavaScript-Payload-into-Gitmodules-File]]
