---
id: 2d4a5772-8a8e-4930-aa52-4a565d37d26a
type: tool
name: Quasar
verified: true
created_at: '2019-08-28T21:17:28.445255+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - rat
  - post-exploitation
  - remote-access
  - c-sharp
url: 'https://github.com/quasar/Quasar'
description: >-
  Open-source remote administration tool (RAT) for Windows, providing
  capabilities for remote control, surveillance, and post-exploitation
  activities.
validated: true
---

# Quasar

**Status**: Unverified

## Overview

Quasar is a fast, lightweight remote administration tool (RAT) developed in C# for Windows environments. It is designed for remote management of target systems, offering features like file transfer, keylogging, screen capture, webcam access, and shell execution. In security testing contexts, it is used for post-exploitation simulations, red team operations, and demonstrating persistence and command-and-control (C2) techniques. Quasar emphasizes stability and a user-friendly GUI for the server component.

## Description

Quasar consists of a server application (C2 controller) and client payloads (implants deployed on targets). The server allows operators to manage multiple clients, send commands, and receive data streams. Key capabilities include:
- Remote shell execution
- File manager for upload/download
- Registry editing
- Password recovery from browsers
- System information gathering
- Anti-virus disabling (in advanced configurations)

It supports encrypted communications via TCP and is customizable for payload generation, including binders and stubs to evade detection. Quasar is particularly useful in Windows-centric environments for simulating advanced persistent threats (APTs).

## Features

- **Remote Control**: Full desktop access, mouse/keyboard control.
- **Surveillance**: Keylogger, screenshot capture, microphone/webcam streaming.
- **File Operations**: Browse, upload, download, and execute files remotely.
- **Persistence**: Install as service or startup entry.
- **Stealth**: Hidden processes, encrypted traffic, and customizable icons.
- **Multi-Client Support**: Manage multiple infected hosts from a single interface.

## Installation

### Requirements

- .NET Framework 4.5 or later (Windows only)
- Visual Studio 2017+ for building from source (Community edition sufficient)
- Git for cloning the repository

### Install Commands

First, clone the repository:

Use [[commands/git-clone-quasar-repo]] to download the source code.

Then, open the solution in Visual Studio and build:

Use [[commands/msbuild-build-quasar]] to compile the binaries.

For pre-built binaries, download releases from the GitHub repository and extract to a working directory.

## Basic Usage

```bash
Quasar.exe
```

Launch the server GUI by running `Quasar.exe`. The interface includes tabs for client management, builder for payload creation, and settings for server configuration.

### Common Options

Quasar is primarily GUI-driven, but server startup can be configured via command-line arguments for the executable:

| Option | Description |
|--------|-------------|
| `-h, --help` | Display available command-line options |
| `-c, --config <file>` | Load configuration from a specified file |
| `-p, --port <port>` | Specify listening port (default: 4795) |
| `-e, --encrypt` | Enable encryption for client connections |

## Examples

### Example 1: Basic Usage

Start the Quasar server:

```bash
Quasar.exe -p 4444 -e
```

This launches the server on port 4444 with encryption enabled.

### Example 2: Advanced Usage

Build a custom client payload using the integrated builder (GUI), then deploy via social engineering or exploit. Once connected, use the server to issue commands like file download:

In the GUI: Select client > File Manager > Download > Specify path.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote Access Tools]] Remote Access Software
- [[Windows Remote Management]] Windows Remote Management
- [[PowerShell]] PowerShell
- [[Hidden Window]] Hidden Window

### Tactics

- [[Command and Control]] Command And Control
- [[Persistence]] Persistence
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic on non-standard ports (e.g., TCP 4795) with C# binary patterns.
- Processes named `Quasar.exe` or disguised names; check for .NET assemblies.
- Registry keys under `HKCU\Software\Quasar` or service entries.
- Anomalous file I/O or webcam/microphone access without user interaction.
- Use EDR tools to monitor for RAT behaviors like persistent TCP connections to C2.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Covenant]]
- [[tools/Empire]]
- [[Meterpreter]]

## References

- Official GitHub: https://github.com/quasar/Quasar
- Documentation: Included in repository README
- Related resources: MITRE ATT&CK for RAT techniques
