---
type: tool
description: >-
  Empire is a post-exploitation framework that provides command and control
  capabilities using PowerShell agents for Windows and Python agents for
  Linux/OS X.
url: 'https://github.com/BC-SECURITY/Empire'
tags:
  - c2
  - post-exploitation
  - powershell
  - python
platforms:
  - Linux
  - Windows
  - macOS
verified: true
created_at: '2019-08-28T21:17:41.443646+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
validated: true
---

# Empire

**Status**: Unverified

## Overview

Empire is a post-exploitation framework designed for command and control (C2) operations. It specializes in evading detection while managing agents on compromised systems. The framework includes a pure PowerShell 2.0 agent for Windows targets and a pure Python 2.6/2.7 agent for Linux and OS X systems. Empire uses cryptographically secure communications for agents to connect back to the C2 server and receive instructions.

Common use cases include deploying payloads, executing scripts, privilege escalation, and lateral movement during red team engagements.

## Description

Empire functions as a flexible C2 server that loads stagers, modules, and listeners at startup. It supports executing PowerShell scripts, .NET assemblies, and third-party tools without requiring additional installations on the target. Key capabilities include:

- Agent management for multiple compromised hosts
- Modular design for extensibility
- Evasion techniques to bypass antivirus and EDR
- Integration with tools like Mimikatz for credential dumping

Empire is particularly useful in environments where PowerShell is restricted, as it can use alternative agents and obfuscation methods.

## Features

- **Cross-Platform Agents**: PowerShell for Windows, Python for Unix-like systems
- **Modular Architecture**: Includes built-in modules for common post-exploitation tasks such as PowerUp (privilege escalation checks), BypassUAC, Sherlock (vulnerability scanning), Mimikatz (credential extraction), PowerDump, EgressCheck (network testing), and Keylogger
- **Secure Communications**: Uses AES-256 encryption for agent-server interactions
- **Listener Support**: HTTP/HTTPS, DNS, and other protocols for agent callbacks
- **Stager Generation**: Creates launchers for initial agent deployment via various methods (e.g., phishing, drive-by downloads)

## Installation

### Requirements

- Python 2.7 or 3.x (for server)
- Git for cloning the repository
- PostgreSQL (optional, for persistent storage)
- Supported on Kali Linux, Ubuntu, and other Debian-based distributions

### Install Commands

On Kali Linux (pre-packaged):

```bash
# Empire is available via apt
sudo apt update
sudo apt install powershell-empire
```

Manual installation from source:

```bash
# Clone the BC-Security fork
git clone https://github.com/BC-SECURITY/Empire.git
cd Empire
./setup/install.sh
```

For Ubuntu:

```bash
sudo apt install python2.7 python-pip git
# Then follow manual installation steps
```

After installation, initialize the database if using PostgreSQL:

```bash
./setup/database.sh
```

## Basic Usage

```bash
powershell-empire
```

This launches the Empire server, prompting for a negotiation password (press Enter for random generation). The server loads modules, stagers, and listeners, then enters an interactive console.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help for the empire command |
| `--rest` | Start the RESTful API server (requires Flask) |
| `--profile <path>` | Use a custom profile directory |

## Examples

### Example 1: Basic Usage

Launch the Empire server:

```bash
powershell-empire
```

Expected behavior: The server starts, displays the ASCII art banner, loads 298+ modules (version-dependent), and shows 0 active listeners/agents initially. Enter commands like `listeners` to manage listeners or `usestager` to generate payloads.

### Example 2: Advanced Usage

Start with REST API enabled:

```bash
powershell-empire --rest
```

This allows API interactions for automated operations.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol (for C2 communications)
- [[PowerShell]] PowerShell (agent execution)
- [[Abuse Elevation Control Mechanism]] Abuse Elevation Control Mechanism (via modules like BypassUAC)
- [[Credential Dumping]] OS Credential Dumping (via Mimikatz integration)

### Tactics

- [[Command and Control]] Command and Control
- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic: Unusual outbound connections to listener ports (e.g., HTTP/HTTPS on non-standard ports) with encrypted payloads
- Process monitoring: powershell.exe spawning with encoded commands or unusual child processes
- File artifacts: Presence of Empire binaries, logs, or profiles in user directories
- Behavioral: High entropy network data, PowerShell logging showing module loads (e.g., reflective PE injection)
- EDR rules: Signatures for known Empire stagers or module names like "PowerUp.ps1"

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Covenant]] (alternative .NET C2 framework)
- [[Cobalt-Strike]] (commercial C2 platform)
- [[Metasploit]] (exploitation framework with C2 modules)

## References

- Official GitHub: https://github.com/BC-SECURITY/Empire
- Original Empire Project: https://github.com/EmpireProject/Empire (archived)
- Documentation: Included in the repository under docs/
- Blog posts on usage: Search for "Empire C2 red team" for tutorials
