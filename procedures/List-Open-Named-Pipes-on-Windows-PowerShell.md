---
id: 6ccdca75-5cb4-4df8-9cac-f39510cc4d6d
name: List-Open-Named-Pipes-on-Windows-PowerShell
type: procedure
verified: true
submitted: true
created_at: '2020-04-29T00:05:04.370427+00:00'
updated_at: '2023-05-25T19:42:12.099710+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - enumeration
commands:
  - '[[commands/List-Open-Named-Pipes-PowerShell]]'
platforms:
  - Windows
tools: []
validated: true
---

# List-Open-Named-Pipes-on-Windows-PowerShell

## Summary

This procedure uses PowerShell to enumerate open named pipes on a Windows system, revealing inter-process communication channels that may indicate active services, processes, or potential attack vectors such as accessible pipe endpoints for privilege escalation or lateral movement.

## Description

Named pipes in Windows provide a mechanism for inter-process communication (IPC), allowing processes to exchange data in a FIFO manner. They are often used by system services like LSASS, RPC, and others for secure communication. Enumerating open named pipes helps attackers identify running services, potential injection points, or misconfigurations. This technique is commonly employed during reconnaissance phases to map the system's internal structure without requiring elevated privileges, though some pipes may only be visible to administrators. The procedure leverages the .NET System.IO namespace to query the pipe directory (\\.\pipe\) and list all accessible pipes, providing insights into system activity and potential exploitation opportunities.

## Requirements

1. Access to a Windows system with PowerShell enabled (version 2.0 or later).
2. Local execution privileges; administrative rights may reveal more pipes but are not strictly required.
3. No external tools needed, as this uses built-in PowerShell and .NET classes.

## Defense

Defensive measures include monitoring PowerShell execution for suspicious .NET invocations via Event ID 4104 (Script Block Logging) or Sysmon logs for process creation involving powershell.exe. Restrict named pipe access using Windows security descriptors and audit pipe creation/access events (Event ID 5145). Use endpoint detection tools to flag enumeration of system directories like \\.\pipe\.

## Objectives

1. Identify active named pipes to understand system services and processes.
2. Detect potential IPC vulnerabilities or accessible endpoints for further exploitation.
3. Gather reconnaissance data for targeted attacks on specific services like LSASS or RPC.

## Instructions

### Step 1: Enumerate Open Named Pipes

**Context**: This step queries the named pipe directory using .NET methods in PowerShell to list all currently open pipes, providing a snapshot of active IPC channels. It helps in identifying system-critical pipes (e.g., lsass, scerpc) and any unusual or user-created ones.

**Command** ([[commands/List-Open-Named-Pipes-PowerShell]]):
```powershell
[System.IO.Directory]::GetFiles("\\.\pipe\")
```

> This command accesses the \\.\pipe\ directory as a file system path and returns an array of pipe names. Run it in a PowerShell console or script. If pipes are protected, some may not be listed without elevated privileges. Review the output for familiar system pipes and any anomalies indicating malware or custom applications.
