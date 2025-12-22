---
type: command
executor: bash
data: /usr/bin/script -qc /bin/bash /dev/null
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - post-exploitation
  - reverse-shell
verified: true
validated: true
---

# script-create-pty-bash

## Command

```bash
/usr/bin/script -qc /bin/bash /dev/null
```

## Description

This command uses the 'script' utility to spawn an interactive bash shell within a pseudo-terminal (PTY), upgrading non-interactive reverse shells for better usability. It is particularly useful in penetration testing to enable features like command history and full terminal emulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -q | Quiet mode: Suppress the 'Script started' message | Yes |
| -c | Execute the following command instead of an interactive shell | Yes |
| /bin/bash | The shell to invoke (bash for standard Linux compatibility) | Yes |
| /dev/null | Redirect script output to null (discards logging for stealth) | Yes |

## Examples

### Basic Usage

```bash
/usr/bin/script -qc /bin/bash /dev/null
```

### Advanced Usage

To use a different shell like zsh:

```bash
/usr/bin/script -qc /bin/zsh /dev/null
```

## Expected Output

No verbose output due to -q; the command immediately drops into an interactive bash prompt (e.g., 'user@hostname:~$'). Terminal capabilities are restored, allowing tab completion, vi mode, and escape sequences. Test with 'echo $0' (should show '/bin/bash') or 'stty size' (displays rows/columns).

## Related

- [[procedures/Spawn-TTY-Shell-for-Interactive-Reverse-Shell]]
