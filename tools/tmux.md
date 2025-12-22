---
id: 98bcce60-8292-439d-9f6e-5aae154d7f57
name: tmux
type: tool
verified: true
created_at: '2020-03-17T02:16:07.611640+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
tags:
  - session
  - terminal-multiplexer
url: 'https://github.com/tmux/tmux'
commands:
  - '[[commands/tmux-attach-to-session-via-socket]]'
validated: true
---

# tmux

**Status**: ✓ Verified

## Overview

Tmux is a terminal multiplexer that enables users to create, manage, and switch between multiple terminal sessions within a single window. It is particularly useful in security testing and penetration engagements for maintaining persistent sessions that survive network disconnections, allowing operators to run long-duration tasks like scans or exploits without interruption. Similar to GNU Screen, tmux supports splitting windows into panes, detaching and reattaching sessions, and scripting for automation.

## Description

Tmux operates by creating a server-client model where sessions run on a tmux server, and clients connect to view or interact with them. This architecture makes it ideal for remote operations over SSH, where connections may drop unexpectedly. In offensive security, tmux is commonly used to manage multiple reconnaissance tools, coordinate team sessions, or ensure persistence in compromised environments by attaching to pre-configured sockets. It supports extensive customization via a configuration file (~/.tmux.conf) for key bindings, status bars, and plugins.

## Features

- **Session Management**: Create, detach, and reattach sessions without losing running processes.
- **Window and Pane Support**: Split the terminal into multiple resizable panes and windows for multitasking.
- **Persistence**: Sessions remain active in the background even after logout.
- **Scripting and Automation**: Supports command-line invocation and integration with shell scripts.
- **Copy Mode**: Built-in vi/emacs-like mode for scrolling and copying text between panes.
- **Plugin Ecosystem**: Extensible via plugins like tmux-plugin-manager for additional functionality.

## Installation

### Requirements

- POSIX-compliant system (Linux, macOS, BSD).
- Basic build tools (gcc, make) if compiling from source.

### Install Commands

#### Kali Linux
Pre-installed on Kali Linux distributions.

#### Debian/Ubuntu
```bash
sudo apt update
sudo apt install tmux
```

#### macOS (via Homebrew)
```bash
brew install tmux
```

#### From Source
```bash
wget https://github.com/tmux/tmux/releases/download/3.3a/tmux-3.3a.tar.gz
tar -xzf tmux-3.3a.tar.gz
cd tmux-3.3a
./configure && make
sudo make install
```

## Basic Usage

Start a new tmux session:
```bash
tmux new-session -s mysession
```

Detach from a session (Ctrl+b, then d).

List active sessions:
```bash
tmux list-sessions
```

### Common Options

| Option | Description |
|--------|-------------|
| `-s` | Specify session name |
| `-d` | Detach other clients from the session |
| `-t` | Target a specific session or window |
| `-S` | Specify socket path for the tmux server |

## Examples

### Example 1: Basic Usage - Create and Attach to a Named Session
```bash
tmux new-session -s recon -d  # Create detached session
# Run commands in background, e.g., nmap
 tmux send-keys -t recon 'nmap -sV target.com' Enter
tmux attach-session -t recon  # Attach to it
```

### Example 2: Advanced Usage - Attach via Custom Socket
```bash
tmux -S /tmp/custom.sock new-session -s secure
# Later, from another terminal:
tmux -S /tmp/custom.sock attach -t secure
```

## Related Commands

- [[commands/tmux-attach-to-session-via-socket]]

## References

- Official Documentation: https://github.com/tmux/tmux/wiki
- Man Page: `man tmux`
