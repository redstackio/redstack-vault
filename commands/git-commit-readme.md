---
id: cmd-git-commit-readme-001
data: git commit -m "add README"
tags:
  - git
  - commit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.905Z'
verified: false
validated: true
submitted: true
---
# git-commit-readme

## Command

```bash
git commit -m "add README"
```

## Description

Commits staged changes with a message. Standard in GitLab instructions; XSS triggers in surrounding content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m` | Commit message | Yes |
| `"add README"` | The message content | Yes |

## Examples

### Basic Usage

```bash
git commit -m "add README"
```

### Advanced Usage

```bash
git commit -m "add README"  # As displayed
```

## Expected Output

[main abc123] add README; 1 file changed.

## Related

- [[commands/git-push-branch]]
- [[procedures/Create-Blank-Project-to-Host-XSS-Payload]]
