---
id: a6dfd24d-0ddd-423b-95fa-85b9367ec9fb
name: rlwrap-nc-with-history-completion
type: command
executor: bash
data: rlwrap -r -f . nc -nlvp $_PORT
output: null
created_at: '2023-04-06T03:56:24.983325+00:00'
updated_at: '2023-04-10T20:25:31.247390+00:00'
platforms:
  - Linux
tags:
  - netcat
  - listener
  - reverse-shell
  - history
verified: true
validated: true
---

# rlwrap-nc-with-history-completion

## Command

```bash
rlwrap -r -f . nc -nlvp $_PORT
```

## Description

Enhanced netcat listener using rlwrap with history file integration for command completion in reverse shells.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rlwrap | Readline wrapper | Yes |
| -r | Add input/output to completion list | Yes |
| -f . | Use current history file for completions | Yes |
| nc | Netcat | Yes |
| -nlvp | Listen verbose on port | Yes |
| $_PORT | Port number | Yes |

## Examples

### With History on Port 4242

```bash
rlwrap -r -f . nc -nlvp 4242
```

## Expected Output

Similar to basic nc: "listening on [any] 4242 ..." but with tab completion for previous commands.

## Related

- [[procedures/Spawn-TTY-Shell-from-Existing-Session]]
- [[commands/rlwrap-nc-connect-to-host]]
