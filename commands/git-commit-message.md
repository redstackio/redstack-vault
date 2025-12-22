---
id: cmd-uuid-4
data: git commit -am "Added file to initialize project repository"
tags:
  - git
  - commit
type: command
output: |-
  [main (root-commit) abc1234] Added file to initialize project repository
   1 file changed, 0 insertions(+), 0 deletions(-)
   create mode 100644 some-file
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.325Z'
verified: false
validated: true
submitted: true
---
---

# git-commit-message

## Command

```bash
git commit -am "Added file to initialize project repository"
```

## Description

Commits staged changes with a descriptive message, using -a to stage all modifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-a` | Stage all changes | No |
| `-m` | Commit message | Yes |
| `"message"` | The commit description | Yes |

## Examples

### Basic Usage

```bash
git commit -am "Initial commit"
```

### Advanced Usage

```bash
git commit -m "Update submodule"
```

## Expected Output

Commit hash and summary of changes.

## Related

- [[commands/git-push-changes]]
- [[procedures/Add-Wiki-as-Relative-Git-Submodule]]
