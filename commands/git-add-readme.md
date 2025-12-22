---
id: cmd-git-add-readme-001
data: git add README.md
tags:
  - git
  - staging
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.908Z'
verified: false
validated: true
submitted: true
---
# git-add-readme

## Command

```bash
git add README.md
```

## Description

Stages the README.md file for commit. Displayed in vulnerable GitLab pages; injection from branch name affects the overall script context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `add` | Stage files | Yes |
| `README.md` | File to add | Yes |

## Examples

### Basic Usage

```bash
git add README.md
```

### Advanced Usage

```bash
git add README.md  # GitLab template
```

## Expected Output

No output; file staged.

## Related

- [[commands/git-commit-readme]]
- [[procedures/Create-Blank-Project-to-Host-XSS-Payload]]
