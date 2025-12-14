---
id: schtasks-001
url: >-
  https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks
tags:
  - scheduling
  - escalation
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.072Z'
validated: true
submitted: true
---
# schtasks-exe

**Status**: Unverified

## Overview

schtasks.exe is a Windows command-line tool for managing scheduled tasks, commonly used in privilege escalation by creating tasks that run with higher privileges like SYSTEM.

## Description

It allows creating, deleting, querying, and running tasks stored in Task Scheduler. In offensive security, it's abused to execute payloads as elevated users without direct SYSTEM access, exploiting Admin rights to impersonate SYSTEM.

## Features

- Feature 1: Create tasks with custom users (/RU), schedules (/SC), and actions (/TR)
- Feature 2: Run tasks immediately (/run /I)
- Feature 3: Query and delete tasks for cleanup

## Installation

### Requirements

- Windows OS (built-in, no installation needed)

### Install Commands

```cmd
# Already available in %SystemRoot%\System32\schtasks.exe
```

## Basic Usage

```cmd
schtasks /?
```

### Common Options

| Option | Description |
|--------|-------------|
| /create | Create a new task |
| /run | Run an existing task |
| /query | List tasks |
| /delete | Delete a task |

## Examples

### Example 1: Basic Usage

```cmd
schtasks /create /TN Test /TR notepad.exe
```

### Example 2: Advanced Usage

```cmd
schtasks /create /SC ONCE /ST 12:00 /RU SYSTEM /TN Elevate /TR cmd.exe /RL HIGHEST
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Scheduled Task]] Scheduled Task/Job: Scheduled Task

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor command-line arguments for /RU SYSTEM or /RL HIGHEST in process creation logs
- Alert on unexpected task creations via Event ID 4698 in Windows Security logs
- Use Sysmon to log schtasks.exe executions

## Related Procedures

- [[procedures/Verify-Admin-Privileges-and-Escalate-to-SYSTEM]]

## Related Tools

- [[at.exe]] (older task scheduler)
- [[PowerShell Scheduled Jobs]]

## References

- Official documentation: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks
