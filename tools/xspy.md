---
id: 20c26a10-0851-4292-99ec-4ac260f243d7
name: xspy
type: tool
verified: true
created_at: '2019-08-28T21:17:33.083655+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - x11
  - keystroke-sniffing
  - credential-access
  - post-exploitation
url: 'https://www.kali.org/tools/xspy/'
validated: true
---

# xspy

**Status**: Unverified

## Overview

xspy is a lightweight tool for sniffing keystrokes on local or remote X11 (X-Windows) servers. It intercepts key press and release events, making it useful for credential capture or input monitoring during penetration testing and red team operations.

## Description

xspy operates by connecting to an X11 display and listening for keyboard events. It can target local displays (e.g., :0) or remote ones over the network, provided the X server allows connections (often requiring xhost + or similar configuration). Commonly used in Linux environments for post-exploitation to capture passwords, commands, or sensitive input. Note: Modern X11 setups with authentication (e.g., Xauthority) may require additional setup for remote access.

## Features

- Feature 1: Real-time keystroke event capture (KeyPress and KeyRelease)
- Feature 2: Support for local and remote X11 displays
- Feature 3: Lightweight and dependency-free (uses standard Xlib)
- Feature 4: Output redirection for logging captured events

## Installation

### Requirements

- Linux system with X11 development libraries (libX11-dev)
- Network access for remote sniffing

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install xspy

# From source (if needed)
git clone https://gitlab.com/kalilinux/packages/xspy.git
cd xspy
make
sudo make install
```

## Basic Usage

```bash
xspy --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and exit |
| `DISPLAY` | Specify the X display to sniff (e.g., :0 or remotehost:0) |

## Examples

### Example 1: Basic Usage

Sniff on local display:

```bash
xspy :0
```

### Example 2: Advanced Usage

Remote sniffing with output logging:

```bash
xspy remotehost:0 | tee keystrokes.log
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Keylogging]] Keylogging (Linux/Unix)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor X11 connections from unexpected sources (e.g., via xwininfo or netstat for X11 ports ~6000)
- Detection method 2: Process listing showing xspy running (ps aux | grep xspy)
- Detection method 3: Audit logs for unauthorized X server access or unusual key event queries

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Wireshark]] (for broader network sniffing including X11 traffic)
- [[tools/xwd]] (X11 display dumping utility)

## References

- Official Kali documentation: https://www.kali.org/tools/xspy/
- X11 Protocol Reference: https://www.x.org/releases/X11R7.7/doc/
