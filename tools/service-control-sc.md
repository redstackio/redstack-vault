---
type: tool
verified: true
platforms:
  - Windows
tags:
  - enumeration
  - process
  - service-attacks
  - defense-evasion
url: >-
  https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-control
description: >-
  Command-line tool for managing Windows services, including starting, stopping,
  querying, and configuring them.
validated: true
---

# Service Control (sc)

**Status**: ✓ Verified

## Overview

Service Control (sc) is a built-in Windows command-line utility for interacting with the Service Control Manager (SCM) and individual services. It enables administrators and security testers to query service status, start or stop services, modify configurations like startup types, create or delete services, and more. In offensive security, sc is commonly used for persistence (creating rogue services), defense evasion (disabling security tools like Windows Defender), and lateral movement preparation.

## Description

The sc.exe executable communicates directly with the SCM database to retrieve or alter service properties without requiring GUI tools like services.msc. It supports a wide range of subcommands, making it versatile for automation via batch scripts or command prompt. Key use cases in red teaming include disabling antivirus services to avoid detection, enumerating running processes via service queries, and establishing persistence by registering malicious binaries as services. sc requires administrative privileges for most operations, such as stopping protected services or changing configurations.

## Features

- **Query Services**: Retrieve detailed information about service states, dependencies, and configurations.
- **Start/Stop Services**: Initiate or halt service execution, useful for evasion or disruption.
- **Configure Services**: Modify startup types (e.g., automatic, manual, disabled), binaries, or dependencies.
- **Create/Delete Services**: Register new services for persistence or remove unwanted ones.
- **Enumeration**: List all services, binaries, and users with service access.

## Installation

### Requirements

- Windows operating system (XP and later).
- Administrative privileges for configuration changes.

### Install Commands

sc is pre-installed on all modern Windows installations. No additional setup is required. Verify availability by running:

```command_prompt
sc.exe
```

## Basic Usage

```command_prompt
sc.exe /?
```

This displays help for all subcommands.

### Common Options

| Option | Description |
|--------|-------------|
| `query` | Queries the status of a service or all services. |
| `config` | Changes the configuration of a service (e.g., startup type). |
| `start` | Starts a service. |
| `stop` | Stops a running service. |
| `create` | Creates a new service. |
| `delete` | Deletes a service. |
| `description` | Sets or queries a service's description. |

## Examples

### Example 1: Query a Service Status

```command_prompt
sc query WinDefend
```

### Example 2: Stop and Disable Windows Defender

Use the related commands to stop and disable the WinDefend service:

- [[commands/sc-stop-windefend]]
- [[commands/sc-config-windefend-start-disabled]]

### Example 3: Enumerate All Services

```command_prompt
sc query type= service state= all
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Disable or Modify Tools]] Impair Defenses: Disable or Modify Tools (e.g., disabling Windows Defender).
- [[Windows Service]] Create or Modify System Process: Windows Service (e.g., creating persistent services).
- [[Process Discovery]] Process Discovery (via service enumeration).

### Tactics

- [[Defense Evasion]] Defense Evasion.
- [[Privilege Escalation]] Privilege Escalation.
- [[Persistence]] Persistence.

## Detection

- Monitor Event ID 7045 (new service creation) and 7036 (service start/stop) in Windows Event Logs.
- Watch for sc.exe executions from non-standard paths or with unusual arguments via Sysmon (Event ID 1: Process Creation).
- Baseline service configurations and alert on changes to critical services like WinDefend.
- Use tools like Autoruns to detect anomalous service binaries.

## Related Procedures

No related procedures documented yet.

## Related Tools

- [[tools/tasklist]] (for process enumeration).
- [[net]] (for network service queries).
- [[psexec]] (for remote service management).

## References

- [Microsoft Docs: sc.exe](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-control)
- [MITRE ATT&CK: Service Manipulation](https://attack.mitre.org/techniques/T1543/003/)
