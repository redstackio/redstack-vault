---
id: cmd-git-config-user-email-001
data: 'git config --global user.email "#{h git_user_email}"'
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
updated_at: '2025-12-13T23:55:06.920Z'
verified: false
validated: true
submitted: true
---
# git-config-user-email

## Command

```bash
git config --global user.email "#{h git_user_email}"
```

## Description

Configures the global Git email for commits. Displayed in GitLab project setup with potential XSS injection points in the email placeholder, enabling script execution when rendered unsanitized.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--global` | Sets for all repos | Yes |
| `user.email` | Key for email config | Yes |
| `"#{h git_user_email}"` | Interpolated email value, vulnerable if h escaping fails | Yes |

## Examples

### Basic Usage

```bash
git config --global user.email "user@example.com"
```

### Advanced Usage

```bash
git config --global user.email "#{h git_user_email}"  # Vulnerable display in GitLab
```

## Expected Output

Silent success; check with `git config --global user.email`.

## Related

- [[commands/git-config-user-name]]
- [[procedures/Create-Blank-Project-to-Host-XSS-Payload]]
