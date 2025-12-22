---
id: 66f57b98-f81f-4bf8-99e5-e51f46124f10
type: tool
verified: true
created_at: '2019-08-28T21:17:19.944467+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - c2
  - red-team
  - adversary-simulation
  - post-exploitation
url: 'https://www.cobaltstrike.com/'
commands:
  - '[[commands/cobalt-strike-start-team-server]]'
  - '[[commands/cobalt-strike-connect-client]]'
validated: true
---

# Cobalt-Strike

**Status**: Unverified

## Overview

Cobalt Strike is a commercial adversary simulation platform designed for red team operations and advanced persistent threat (APT) emulation. It enables security professionals to model sophisticated attacker behaviors, including command and control (C2) communications, payload delivery, and lateral movement within networks.

## Description

Cobalt Strike provides a comprehensive suite of tools for offensive security testing, featuring the Beacon implant for stealthy post-exploitation, customizable Malleable C2 profiles to blend traffic with legitimate network activity, and collaborative features for multi-operator teams. It is widely used in penetration testing to simulate real-world attacks, validate defenses, and train blue teams. The platform includes capabilities for generating stagers, managing listeners, executing modules for privilege escalation, and exfiltrating data while evading detection.

## Features

- **Beacon Implant**: Lightweight, sleep-masked payload for persistent C2 with low detection footprint.
- **Malleable C2**: Customizable HTTP/HTTPS profiles to mimic legitimate web traffic.
- **Aggressor Scripts**: JavaScript-like scripting for automating tasks and extending functionality.
- **Team Server**: Centralized server supporting multiple clients for collaborative operations.
- **Post-Exploitation Modules**: Built-in actions for credential dumping, keylogging, screenshot capture, and more.
- **Reporting**: Generates detailed reports on operations for debriefing and compliance.

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher.
- Valid commercial license from Fortra (formerly HelpSystems).
- Supported OS: Linux (preferred for team server) or Windows.
- Network access for C2 communications (outbound ports 80/443 typically).

### Install Commands

Cobalt Strike is distributed as a licensed download. After obtaining the package:

```bash
# On Linux (team server)
chmod +x teamserver
# No traditional install; run directly

# Client launch (Linux/Windows)
java -jar cobaltstrike.jar
```

For Windows, extract the ZIP and run the executable. No package manager installation; it's a standalone application.

## Basic Usage

```bash
teamserver --help
```

Start with the team server, then connect clients.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help for team server or client |
| `--profile <path>` | Load a custom Malleable C2 profile |
| `-v` | Verbose logging for troubleshooting |

## Examples

### Example 1: Basic Usage

Start team server:

```bash
./teamserver 192.168.1.100 myteamserverpass
```

Connect client:

```bash
java -jar cobaltstrike.jar 192.168.1.100 myteamserverpass
```

### Example 2: Advanced Usage

Start with custom profile:

```bash
./teamserver 192.168.1.100 myteamserverpass ./profiles/myprofile.profile
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol (for C2 over HTTP/HTTPS)
- [[Non-Standard Port]] Non-Standard Port (custom C2 ports)
- [[PowerShell]] PowerShell (via Beacon execution)
- [[Windows Remote Management]] Windows Command Shell (task execution)
- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel

### Tactics

- [[Command and Control]] Command and Control
- [[Execution]] Execution
- [[Lateral Movement]] Lateral Movement
- [[Exfiltration]] Exfiltration

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual Java processes (cobaltstrike.jar) or teamserver binaries on endpoints.
- Network traffic matching Malleable profiles (e.g., anomalous HTTP headers like 'Profile: Beacon').
- Beacon artifacts: Sleep mask patterns in memory, registry keys (e.g., HKCU\Software\Beacon), or unusual DLLs.
- EDR alerts on PowerShell execution from non-standard paths or C2 domains resolving to team servers.
- Log analysis for connections to high/reconnaissance IPs or custom user-agents.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Metasploit]]
- [[tools/Empire]]
- [[Sliver]]

## References

- Official Documentation: https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/getting-started.htm
- Malleable C2 Profiles: https://github.com/rsmudge/Malleable-C2-Profiles
- Related Resources: MITRE ATT&CK Cobalt Strike page
