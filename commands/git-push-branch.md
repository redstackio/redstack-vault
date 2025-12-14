---
id: cmd-git-push-branch-001
data: 'git push -u origin #{ default_branch_name }'
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
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.902Z'
verified: false
validated: true
submitted: true
---
# git-push-branch

## Command

```bash
git push -u origin #{ default_branch_name }
```

## Description

Pushes the branch to the remote origin and sets upstream. Another key injection point for XSS in GitLab, where default_branch_name allows script execution in the rendered command.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Set upstream tracking | Yes |
| `origin` | Remote name | Yes |
| `#{ default_branch_name }` | Branch to push; XSS vector | Yes |

## Examples

### Basic Usage

```bash
git push -u origin main
```

### Advanced Usage (Vulnerable)

```bash
git push -u origin #{ default_branch_name }  # <script> injects here
```

## Expected Output

Branch abc1234 -> main; upstream set.

## Related

- [[commands/git-switch-branch]]
- [[procedures/Inject-Malicious-Payload-into-Default-Branch-Name]]
