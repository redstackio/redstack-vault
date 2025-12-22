---
type: tool
verified: true
platforms:
  - Windows
tags:
  - firewall
  - Network
commands:
  - '[[commands/netsh-disable-legacy-firewall]]'
url: >-
  https://learn.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh-contexts
validated: true
---

# netsh

**Status**: ✓ Verified

## Overview

Netsh is a command-line utility built into Windows operating systems for viewing and modifying network configuration settings. It is commonly used in security testing for tasks like configuring interfaces, managing IP settings, and especially for firewall operations such as adding exceptions or disabling protections to facilitate network access during engagements.

## Description

Netsh provides a scripting interface to automate network tasks and is particularly useful in post-exploitation scenarios for evading defenses by altering firewall rules. It supports various contexts like 'interface', 'ip', 'firewall' (legacy), and 'advfirewall' (modern). In offensive security, it's often employed to disable or weaken Windows Firewall to allow inbound/outbound traffic for tools like reverse shells or data exfiltration.

## Features

- Network interface configuration (IP, DNS, etc.)
- Firewall rule management (legacy and advanced)
- Wireless profile handling
- Interface state control (enable/disable adapters)
- Scripting support for batch operations

## Installation

### Requirements

- Windows XP or later (built-in on all versions)

### Install Commands

Netsh is pre-installed on all modern Windows releases. No additional installation required.

To verify availability:

```command_prompt
netsh /?
```

## Basic Usage

```command_prompt
netsh
```

This enters the netsh interactive mode. Use `netsh context` to list available contexts.

### Common Options

| Option | Description |
|--------|-------------|
| `/a` | Saves changes to all profiles |
| `/c` | Specifies context (e.g., `/c firewall`) |
| `/?` | Shows help for the current context |
| `dump` | Exports current configuration |

## Examples

### Example 1: Basic Usage

View current firewall state (legacy context):

```command_prompt
netsh firewall show opmode
```

### Example 2: Advanced Usage

Switch to advanced firewall context and show rules:

```command_prompt
netsh advfirewall firewall show rule name=all
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Disable or Modify Tools]] Impair Defenses: Disable or Modify Tools (Windows Firewall)

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Command-line logging showing 'netsh firewall' or 'netsh advfirewall' executions
- Event ID 5038 in Windows Security log (firewall state changes)
- Unexpected firewall rule additions or disables via Sysmon process creation events
- Network traffic anomalies following netsh execution

## Related Procedures

- [[procedures/Disable-Windows-Firewall]]

## Related Tools

- [[PowerShell]] (for scripting netsh commands)
- [[cmd.exe]] (native command prompt executor)

## References

- Official Microsoft Documentation: https://learn.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh-overview
