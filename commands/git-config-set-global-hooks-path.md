---
id: 6f9c588b-e2ad-4ae7-86a9-0ea7302415e7
name: git-config-set-global-hooks-path
type: command
executor: bash
data: git config --global core.hooksPath $_HOOKS_DIRECTORY
output: null
created_at: '2023-04-06T03:56:18.371351+00:00'
updated_at: '2023-04-10T20:34:17.912573+00:00'
platforms:
  - Linux
tags:
  - git
  - persistence
  - config
verified: true
validated: true
---

# git-config-set-global-hooks-path

## Command

```bash
git config --global core.hooksPath $_HOOKS_DIRECTORY
```

## Description

This command sets the global Git configuration variable core.hooksPath to a specified directory, redirecting all Git hook script execution to that path for persistence purposes. Use this in scenarios where you control the user's environment and want hooks to trigger malicious actions during Git operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_HOOKS_DIRECTORY | Full path to the custom directory for hooks (e.g., /home/user/.git-hooks) | Yes |
| --global | Applies the setting to all repositories for the user (stored in ~/.gitconfig) | Built-in |
| core.hooksPath | The specific Git config key for hook directory override | Built-in |

## Examples

### Basic Usage

```bash
git config --global core.hooksPath ~/.git-hooks
```

### Advanced Usage

```bash
git config --global core.hooksPath /tmp/malicious-hooks
```

## Expected Output

No output is produced on successful execution. If the directory path is invalid or permissions are insufficient, an error like "fatal: unable to access '/path'" appears. Verify success by running [[commands/view-user-git-config]] and checking for the hooksPath entry in the [core] section.

## Related

- [[procedures/Git-Hook-Persistence]]
- [[commands/view-user-git-config]]
