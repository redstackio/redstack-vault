---
type: procedure
description: >-
  Enumerates the names of linked databases on a target MSSQL Server instance to
  map network architecture and identify potential targets.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Remote System Discovery|T1018 - Remote System Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Determine Names of Linked Databases]]'
  - '[[tags/Linked Database]]'
  - '[[tags/MSSQL Server]]'
commands: []
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# Enumerate-Linked-Databases-in-MSSQL

## Summary

This procedure enumerates the names of linked databases on a target MSSQL Server, allowing an attacker to map interconnected database architectures across servers. By querying linked servers via the OPENQUERY function, it reveals remote database names that could serve as pivots for lateral movement or further exploitation in a network.

## Description

Linked servers in MSSQL enable distributed queries between database instances, often spanning multiple servers in an enterprise environment. This technique leverages the OPENQUERY function to execute a remote query on a linked server, retrieving a list of database names from sys.databases. It is useful during post-exploitation phases to discover hidden network segments, identify high-value targets like production databases, and understand data flow. The procedure assumes access to a compromised MSSQL instance with linked server configurations and requires PowerShell with SQL Server cmdlets enabled. Success provides visibility into remote systems without direct network access, aiding in reconnaissance for privilege escalation or data exfiltration.

## Requirements

1. Valid credentials or access to an MSSQL Server instance with linked server configurations.
2. PowerShell environment with SQL Server module (e.g., SqlServer or sqlps) installed and imported.
3. Network connectivity to the target MSSQL instance (typically TCP port 1433).
4. Sufficient privileges (e.g., db_owner or sysadmin) to execute queries on linked servers.

## Defense

Defensive measures and detection strategies:

- Disable or remove unnecessary linked servers using sp_dropserver and audit configurations regularly.
- Implement principle of least privilege, restricting query execution on linked servers to authorized users only.
- Enable SQL Server auditing for distributed queries and monitor logs for OPENQUERY usage or unusual sys.databases access.
- Use network segmentation and firewalls to limit inter-server database communication.
- Deploy endpoint detection tools to monitor PowerShell executions involving SQL cmdlets.

## Objectives

1. Retrieve a list of database names from linked servers on the target MSSQL instance.
2. Map the interconnected database architecture to identify potential lateral movement paths.
3. Spot high-value remote databases for targeted exploitation, such as sensitive data stores.

## Instructions

### Step 1: Prepare the PowerShell Environment

**Context**: Ensure the SQL Server PowerShell module is available to execute queries against the target instance. This step sets up the necessary cmdlets like Get-SQLQuery for remote execution.

Import the SqlServer module if not already loaded:

```powershell
import-module SqlServer
```

> This verifies the environment supports MSSQL interactions. Expected output: No errors, module loaded successfully.

### Step 2: Execute the Linked Database Enumeration Query

**Context**: Use the provided code snippet to query the linked server via OPENQUERY, replacing placeholders with actual values. This retrieves database names from the remote instance linked to the current database.

**Code** ([[codes/PowerShell-Query-Linked-Databases-via-OpenQuery]]):

```ps1
Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query "select * from openquery('<DatabaseLinkName>','select name from sys.databases')" -Verbose
```

> The Get-SQLQuery cmdlet connects to the specified MSSQL instance and runs the OPENQUERY to fetch database names from the linked server named in <DatabaseLinkName>. The -Verbose flag provides execution details. Expected output: A table listing database names (e.g., master, tempdb, model, msdb, user databases) from the remote server, confirming successful enumeration.

### Step 3: Analyze and Verify Results

**Context**: Review the output for relevant databases and validate the linked server connection. This helps prioritize targets based on database names indicating sensitive data.

Parse the results in PowerShell to filter user databases:

```powershell
$result | Where-Object { $_.name -notmatch '^(master|tempdb|model|msdb)$' } | Select-Object name
```

> Filters out system databases to focus on custom ones. Expected output: List of user database names, indicating successful discovery of linked assets.
