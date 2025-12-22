---
data: git push origin main
tags:
  - git
  - push
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 49f4fdab-9992-4fd7-b400-3833c469ba7e
created_at: '2025-12-13T23:52:55.039Z'
updated_at: '2025-12-13T23:52:55.039Z'
verified: false
validated: true
submitted: true
---
---

# git-push-origin-main

## Command

```bash
git push origin main
```

## Description

Pushes local commits to the remote GitLab wiki repository's main branch, making the malicious payload live.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `origin` | Remote name (default after clone) | Yes |
| `main` | Target branch | Yes |

## Examples

### Basic Usage

```bash
git push origin main
```

### Advanced Usage

```bash
git push -u origin main  # Set upstream
```

## Expected Output

To github.com:repo.git
   abc1234..def5678  main -> main

## Related

- [[Related Procedure: Commit and Push Malicious Changes to GitLab Wiki]]
