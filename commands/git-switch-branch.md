---
id: cmd-git-switch-branch-001
data: 'git switch -c #{default_branch_name}'
tags:
  - git
  - branch
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.913Z'
verified: false
validated: true
submitted: true
---
# git-switch-branch

## Command

```bash
git switch -c #{default_branch_name}
```

## Description

Creates and switches to a new branch. This is the primary injection point in GitLab XSS, where the unsanitized default_branch_name allows <script> tags to execute when the command is rendered in pre tags on the project page.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `switch -c` | Create and switch to new branch | Yes |
| `#{default_branch_name}` | Branch name; direct XSS vector if unescaped | Yes |

## Examples

### Basic Usage

```bash
git switch -c main
```

### Advanced Usage (Vulnerable)

```bash
git switch -c #{default_branch_name}  # Injects <script>alert(1);</script>
```

## Expected Output

Switches to new branch; error if name invalid.

## Related

- [[commands/git-push-branch]]
- [[procedures/Inject-Malicious-Payload-into-Default-Branch-Name]]
