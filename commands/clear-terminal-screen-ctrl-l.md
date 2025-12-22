---
id: 7c9bce13-1ba9-42fe-9a9c-45f5bbbaa6fe
name: clear-terminal-screen-ctrl-l
type: command
executor: bash
data: clear
output: null
created_at: '2023-04-06T03:56:24.983158+00:00'
updated_at: '2023-04-10T20:25:31.247390+00:00'
platforms:
  - Linux
  - Unix
tags:
  - terminal
  - utility
verified: true
validated: true
---

# clear-terminal-screen-ctrl-l

## Command

```bash
# Press Ctrl + L or run 'clear'
```

## Description

Clears the terminal screen to remove previous output, providing a clean view before starting listeners or sessions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Ctrl + L | Keyboard shortcut | Yes |
| clear | Equivalent command | Alternative |

## Examples

### Keyboard Shortcut

Press Ctrl + L in the terminal.

### Command Line

```bash
clear
```

## Expected Output

Terminal screen clears, showing only the current prompt at the top.

## Related

- [[procedures/Spawn-TTY-Shell-from-Existing-Session]]
