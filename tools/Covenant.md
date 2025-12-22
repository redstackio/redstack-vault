---
id: 92272e59-e93d-416e-8c14-301f70a700aa
type: tool
verified: true
created_at: '2019-08-28T21:17:37.672237+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
  - Linux
  - macOS
tags:
  - Command & Control
url: 'https://github.com/cobbr/Covenant'
commands:
  - '[[commands/pull-covenant-docker-image]]'
  - '[[commands/run-covenant-docker-container]]'
  - '[[commands/launch-covenant-dotnet]]'
validated: true
---

# Covenant

**Status**: Unverified

## Overview

Covenant is an open-source .NET-based command and control (C2) framework designed for red team operations. It emphasizes .NET as an attack surface and provides a collaborative platform for managing implants, listeners, and tasks. Covenant is particularly useful for simulating advanced persistent threats (APTs) in Windows environments while supporting cross-platform deployment.

## Description

Covenant is built using ASP.NET Core, making it compatible with Windows, Linux, and macOS. It supports Docker for easy deployment and includes a web-based user interface for managing C2 operations. Key components include:

- **Listeners**: HTTP/HTTPS, DNS, and SMB listeners for receiving connections from compromised hosts.
- **Grunts**: .NET implants (agents) that execute tasks on target systems, supporting C# and PowerShell execution.
- **Tasks**: Pre-built and custom tasks for enumeration, privilege escalation, and lateral movement, such as BypassAmsi, Kerberoast, Keylogger, Seatbelt, and SharpUp.
- **Team Server**: Centralized management for multiple operators with role-based access.

Covenant is ideal for red team engagements requiring .NET-specific techniques, evasion of endpoint detection, and collaborative C2 management without relying on traditional tools like Cobalt Strike.

## Features

- Feature 1: Cross-platform support via .NET Core and Docker, allowing deployment on diverse infrastructures.
- Feature 2: Modular task system with built-in .NET assemblies for post-exploitation (e.g., AMSI bypass, UAC escalation).
- Feature 3: Encrypted communications and obfuscation for grunts to evade detection.
- Feature 4: Web UI for real-time management of listeners, grunts, and tasks, with API support for automation.
- Feature 5: Integration with existing .NET tools like SharpSploit for advanced capabilities.

## Installation

### Requirements

- .NET SDK 6.0 or later (for manual install).
- Docker (for containerized deployment).
- Git for cloning the repository.

### Install Commands

For Docker-based installation (recommended for quick setup):

```bash
[[commands/pull-covenant-docker-image]]
```

Then launch the container:

```bash
[[commands/run-covenant-docker-container]]
```

For manual installation:

1. Clone the repository:
   ```bash
git clone https://github.com/cobbr/Covenant.git
   cd Covenant
   ```
2. Restore dependencies:
   ```bash
dotnet restore
   ```
3. Launch the server:
   ```bash
   [[commands/launch-covenant-dotnet]]
   ```

## Basic Usage

```bash
# After installation, access the web UI
# Open browser to https://localhost:7443 (accept self-signed cert)
# Create admin user on first login
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help (for dotnet run) |
| ASPNETCORE_URLS | Set listening URLs (e.g., https://*:7443) |
| --no-launch-profile | Prevent automatic profile launch |

## Examples

### Example 1: Basic Usage

Launch via Docker and access the UI:

```bash
[[commands/run-covenant-docker-container]]
# Browse to https://$_HOST_IP:7443
```

### Example 2: Advanced Usage

Manual launch with custom data path:

```bash
export COVENANT_DATA_PATH=/custom/path/Data
[[commands/launch-covenant-dotnet]]
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol (for HTTP/HTTPS listeners)
- [[Non-Standard Port]] Non-Standard Port (custom listener ports)
- [[PowerShell]] PowerShell (grunt task execution)

### Tactics

- [[Command and Control]] Command and Control
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual .NET processes (e.g., dotnet.exe with network connections to non-standard ports like 7443).
- Detection method 2: Docker containers named 'covenant' or images from 'cobbr/covenant'.
- Detection method 3: Web traffic to self-hosted ASP.NET Core applications on high ports; monitor for grunt C2 beacons.
- Detection method 4: File system artifacts in Data directory (e.g., SQLite databases for listeners/grunts).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: Cobalt Strike]]
- [[Related Tool: Empire]]

## References

- Official GitHub: https://github.com/cobbr/Covenant
- Documentation: https://github.com/cobbr/Covenant/wiki
- Blog posts on .NET C2 evasion techniques.
