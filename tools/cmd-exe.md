---
url: >-
  https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmd
tags:
  - execution
  - windows
type: tool
platforms:
  - Windows
description: Windows Command Prompt for executing system commands and scripts.
id: 8f12f4b1-058e-4305-accb-beecf5b7df22
created_at: '2025-12-14T17:29:44.259Z'
updated_at: '2025-12-14T17:29:44.259Z'
verified: false
validated: true
submitted: true
---
# cmd.exe

**Status**: Verified

## Overview

cmd.exe is the native Windows command-line interpreter, used for running batch scripts, system utilities like msiexec, and verification commands like whoami in security testing and exploitation.

## Description

In offensive security, cmd.exe facilitates local execution of exploits, such as MSI repairs for DLL hijacking. It's always available on Windows, making it ideal for low-privilege to high-privilege transitions without additional tools.

## Features

- Feature 1: Executes native Windows commands (e.g., msiexec, dir)
- Feature 2: Supports batch scripting for automation
- Feature 3: Interactive shell for real-time verification

## Installation

### Requirements

- Windows OS (pre-installed)

### Install Commands

```cmd
# No installation needed; access via Win+R > cmd
```

## Basic Usage

```cmd
cmd /?
```

### Common Options

| Option | Description |
|--------|-------------|
| /c | Run command and terminate
| /k | Run command and keep shell open
| /q | Quiet mode (no echo)

## Examples

### Example 1: Basic Usage

```cmd
cmd /c dir C:\Windows\Installer
```

### Example 2: Advanced Usage

```cmd
cmd /k "msiexec /fa path_to_msi.msi"
```

> Keeps the shell open post-execution for monitoring.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Command Shell]] Windows Command Shell

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor cmd.exe spawns from unusual parents (e.g., MsiExec)
- Log command-line arguments via Sysmon Event ID 1
- Detect elevated cmd.exe without UAC traces

## Related Procedures

- [[Initiate MSI Repair Process]]
- [[Verify SYSTEM Privilege Escalation]]

## Related Tools

- [[PowerShell]]
- [[Powershell Empire]]

## References

- Official documentation: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmd
