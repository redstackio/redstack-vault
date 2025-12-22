---
id: f48cd342-82df-4edd-b441-315af87d2af5
name: reset-tty-after-backgrounding
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:24.983449+00:00'
updated_at: '2023-04-10T20:25:31.246275+00:00'
platforms:
  - Linux
  - Unix
tags:
  - tty
  - reset
  - post-exploitation
validated: true
---

# reset-tty-after-backgrounding

## Code

```bash
# Background with Ctrl+Z first
stty raw -echo
fg
reset
export SHELL=bash
export TERM=xterm-256color
stty rows $(tput lines) columns $(tput cols)
```

## Description

This script sequence backgrounds a non-interactive shell, sets it to raw mode, foregrounds it, resets terminal attributes, and configures environment variables for full TTY functionality, including proper sizing and color support.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $(tput lines) | Current terminal rows | 24 |
| $(tput cols) | Current terminal columns | 80 |

## Usage

Execute in a reverse shell after backgrounding (Ctrl+Z) to upgrade to interactive TTY. Run `echo $TERM && tput lines && tput cols` first to get dimensions, then substitute into stty.

## Detection

- Audit logs showing stty invocations or export of SHELL/TERM variables.
- Process monitoring for suspended (T) shells followed by fg.
- Behavioral analytics on unusual terminal resets in shells.

## Related

- [[procedures/Spawn-TTY-Shell-from-Existing-Session]]
