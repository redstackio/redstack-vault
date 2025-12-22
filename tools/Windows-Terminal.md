---
id: 06d90c58-8d69-48ac-9833-0ec30d998d44
type: tool
verified: true
created_at: '2020-03-26T06:04:31.946016+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - terminal
  - execution
  - administrator
  - setup
url: 'https://github.com/microsoft/terminal'
validated: true
---

# Windows-Terminal

**Status**: ✓ Verified

## Overview

Windows Terminal is a modern, open-source terminal application for Windows that supports multiple command-line tools and shells like Command Prompt, PowerShell, and WSL. It provides tabbed interfaces, customizable profiles, GPU-accelerated text rendering, and Unicode support, making it essential for security professionals conducting local or remote operations on Windows systems.

## Description

Windows Terminal enhances command-line productivity with features like multiple tabs and panes for simultaneous shell sessions, searchable output, and integration with Azure Cloud Shell. In offensive security, it's used post-compromise for efficient execution of commands, scripting, and managing multiple tools without switching windows. It replaces older terminals like conhost.exe with better performance and aesthetics but requires local GUI access; remote sessions (e.g., RDP) can utilize it for interactive shells.

## Features

- **Tabbed and Paned Interface**: Run multiple shells in tabs or split panes for multitasking during engagements.
- **Customizable Profiles**: Configure starting directories, themes, and commands for tools like PowerShell or CMD.
- **GPU Acceleration**: Smooth rendering for large outputs, useful for parsing logs or running verbose scans.
- **Unicode and Emoji Support**: Better handling of international characters and visual indicators in scripts.
- **Integration with WSL**: Seamless access to Linux environments on Windows for cross-platform testing.
- **Keyboard Shortcuts**: Default bindings like Ctrl+Shift+T for new tabs, customizable via settings.json.

## Installation

### Requirements

- Windows 10 version 18362.0 or higher (build 19041 or higher for preview features).
- .NET Desktop Runtime 6.0 or later for some extensions.

### Install Commands

```cmd
# Via Winget (Windows Package Manager)
winget install Microsoft.WindowsTerminal

# Via Microsoft Store (GUI or link)
# Browse to: https://aka.ms/windowsterminal

# Manual Download from GitHub
# Download latest .msixbundle from releases and double-click to install
```

Tip: During Microsoft Store installation, close any login prompts; the app installs anyway.

## Basic Usage

```cmd
wt.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| `wt.exe new-tab` | Opens a new tab with the default profile |
| `wt.exe -d <path>` | Starts Terminal in the specified directory |
| `wt.exe split-pane` | Splits the current pane |
| `wt.exe --help` | Shows help and available commands |

## Examples

### Example 1: Basic Usage

```cmd
wt.exe
```

Launches Windows Terminal with the default PowerShell profile.

### Example 2: Advanced Usage

```cmd
wt.exe new-tab powershell.exe -d C:\Temp ; split-pane -p "Command Prompt"
```

Opens a new PowerShell tab in C:\Temp and splits a pane with Command Prompt.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[PowerShell]] PowerShell
- [[Windows Command Shell]] Windows Command Shell

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring: Look for wt.exe spawning child processes like powershell.exe or cmd.exe.
- Event logs: Windows Event ID 4688 for wt.exe creation, especially with unusual parent processes.
- Network: If integrated with remote shells, monitor for RDP or WinRM alongside wt.exe activity.
- File system: Check for settings.json modifications in %LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[PowerShell]]
- [[Command-Prompt]]

## References

- Official GitHub Repository: https://github.com/microsoft/terminal
- Microsoft Documentation: https://learn.microsoft.com/en-us/windows/terminal/
