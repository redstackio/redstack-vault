---
type: procedure
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Software Discovery|T1518 - Software Discovery]]'
  - >-
    [[techniques/System Owner/User Discovery|T1033 - System Owner/User
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Discover Local SQL Server Instances]]'
  - '[[tags/Identify Instances and Databases]]'
  - '[[tags/MSSQL Server]]'
commands:
  - '[[commands/get-local-sql-instances-powershell]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# Discover-Local-MSSQL-Server-Instances

## Summary

This procedure identifies all Microsoft SQL Server (MSSQL) instances installed and running on the local Windows machine. It is useful in red team engagements or penetration testing to discover database services that could serve as lateral movement targets, privilege escalation vectors, or data exfiltration points.

## Description

Discovering local MSSQL instances involves querying the system's registry or services to enumerate installed SQL Server versions, instance names, editions, and configurations. This technique falls under software discovery and can reveal sensitive database environments without requiring elevated privileges in many cases. Attackers use this to map the target's infrastructure, identify weakly configured databases, or chain with other techniques like SQL injection or credential dumping. The procedure assumes a Windows environment where PowerShell is available, and it leverages built-in or custom modules to retrieve instance details non-intrusively.

## Requirements

1. Local access to a Windows machine (user-level privileges sufficient; admin not required for basic enumeration).
2. PowerShell execution policy allowing script execution (bypass if needed via Set-ExecutionPolicy).
3. Optional: SQL Server PowerShell module (SqlServer) installed for enhanced querying, though basic enumeration uses WMI or registry access.

## Defense

- Disable unnecessary SQL Server instances on non-database servers and monitor for unauthorized installations.
- Implement application whitelisting to restrict PowerShell execution and module loading.
- Enable SQL Server auditing for instance access and use endpoint detection to alert on registry queries to SQL paths (e.g., HKLM:\SOFTWARE\Microsoft\Microsoft SQL Server).

## Objectives

1. Enumerate all local MSSQL instances, including default and named instances.
2. Retrieve version, edition, and service status for each instance.
3. Identify potential attack surfaces like exposed ports (default 1433) or weak authentication configurations.

## Instructions

### Step 1: Query Local SQL Instances

**Context**: Use PowerShell to invoke a function that scans the local system for installed SQL Server instances via registry keys or WMI queries. This step provides a complete list without needing external tools.

**Command** ([[commands/get-local-sql-instances-powershell]]):
```powershell
Get-SQLInstanceLocal
```

> This command queries the Windows registry (e.g., HKLM:\SOFTWARE\Microsoft\Microsoft SQL Server) and services to list all instances. It returns details like instance name (e.g., MSSQLSERVER), version (e.g., 15.0.2000), edition (e.g., Express), and status (running/stopped). If no instances are found, it outputs an empty list or message indicating none detected. Run in an elevated PowerShell session for full access to remote registry if needed, though local enumeration works with standard user rights.
