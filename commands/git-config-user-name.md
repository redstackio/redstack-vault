---
id: cmd-git-config-user-name-001
data: 'git config --global user.name "#{h git_user_name}"'
tags:
  - git
  - configuration
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.923Z'
verified: false
validated: true
submitted: true
---
# git-config-user-name

## Command

```bash
git config --global user.name "#{h git_user_name}"
```

## Description

Sets the global Git username for commit authorship. In the GitLab XSS context, this command is displayed on project pages with interpolated variables, allowing injection via the branch name to execute scripts within the code block.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--global` | Applies the setting to all repositories for the user | Yes |
| `user.name` | The key for the username configuration | Yes |
| `"#{h git_user_name}"` | Placeholder for the escaped username; vulnerable to injection if not sanitized | Yes |

## Examples

### Basic Usage

```bash
git config --global user.name "John Doe"
```

### Advanced Usage

```bash
git config --global user.name "#{h git_user_name}"  # As displayed in vulnerable GitLab template
```

## Expected Output

No output on success; verifies with `git config --global user.name` showing the set value.

## Related

- [[commands/git-config-user-email]]
- [[procedures/Create-Blank-Project-to-Host-XSS-Payload]]
