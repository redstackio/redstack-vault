---
data: git push
tags:
  - git
  - ssh
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: d0879bdc-93ac-43ea-9cf2-37e642340a79
created_at: '2025-12-11T03:47:39.317Z'
updated_at: '2025-12-11T03:47:39.317Z'
verified: false
validated: true
submitted: true
---
# git-push-over-ssh

## Command

```bash
git push
```

## Description

This command pushes local git commits to a remote repository over SSH, used in this context to upload unauthorized changes to GitHub gists after authentication bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `push` | The push subcommand | Yes |
| (implied remote) | Configured remote (e.g., origin) | No |

## Examples

### Basic Usage

```bash
git push
```

### Advanced Usage

```bash
git push origin main --force
```

## Expected Output

Output like 'Everything up-to-date' or details of pushed commits if successful; errors if authentication fails.

## Related

- [[procedures/Exploit-SSH-Authentication-to-Modify-GitHub-Gists]]
- #git
