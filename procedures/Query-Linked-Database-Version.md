---
type: procedure
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Linked Database]]'
  - '[[tags/MSSQL Server]]'
  - '[[tags/Query Version of Linked Database]]'
commands:
  - '[[commands/Get-SQLQuery-Linked-DB-Version]]'
tools: []
platforms:
  - Windows
skill_level: intermediate
impact_level: low
detection_risk: medium
verified: true
validated: true
---

# Query-Linked-Database-Version

## Summary

This procedure retrieves the version information of a linked database in an MSSQL Server environment using a PowerShell-based SQL query. It leverages the OPENQUERY function to execute a version check (@@version) on the remote linked server, helping attackers identify the database software version for potential vulnerability assessment during discovery phases.

## Description

In an MSSQL Server setup with linked databases, attackers with access can query remote server details to map the environment. This technique uses the built-in OPENQUERY to pass-through a simple @@version query to the linked instance, revealing the exact SQL Server edition, version, and build number. This information is crucial for tailoring exploits, such as targeting known vulnerabilities in specific SQL Server versions (e.g., CVE-2017-0144 for older builds). The procedure assumes the linked server is already configured and accessible, typically requiring db_owner or similar permissions on the local instance. It operates in a Windows environment with PowerShell and SQL Server connectivity modules loaded.

## Requirements

1. Valid credentials with execute permissions on the local MSSQL instance and read access to the linked server.
2. PowerShell environment with SQL Server module (e.g., SqlServer or dbatools) installed to provide the Get-SQLQuery cmdlet.
3. Network connectivity to the linked database server (DBSERVERNAME\DBInstance).
4. The linked server must be pre-configured in the local MSSQL instance.

## Defense

- Restrict linked server configurations to only necessary remote endpoints and use least-privilege accounts for links.
- Enable SQL Server auditing for query execution on linked servers to log version queries.
- Implement database firewalls (e.g., Azure SQL Firewall) to limit inter-server queries.
- Regularly patch SQL Server instances to mitigate version-specific vulnerabilities.

## Objectives

1. Retrieve the exact version details of the linked database server.
2. Identify potential vulnerabilities based on the reported SQL Server version.
3. Map the database environment for further discovery or exploitation planning.

## Instructions

### Step 1: Connect and Execute Version Query

**Context**: Establish a connection to the local SQL Server instance and use OPENQUERY to remotely execute the @@version command on the linked server. This step verifies the link is functional and extracts version info without direct remote access.

**Command** ([[commands/Get-SQLQuery-Linked-DB-Version]]):
```powershell
Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query "select * from openquery('<DBSERVERNAME\DBInstance>','select @@version')" -Verbose
```

> This command connects to the specified local instance, executes the pass-through query to the linked server, and outputs the version details. The -Verbose flag provides execution logs for troubleshooting. Replace <DBSERVERNAME\DBInstance> with the actual linked server name (e.g., "PRODSQL\SQLEXPRESS"). Expected output includes the SQL Server version string, such as "Microsoft SQL Server 2019 (RTM) - 15.0.2000.5". If the link fails, check permissions or configuration.

### Step 2: Verify and Parse Output

**Context**: Review the query results to confirm successful retrieval and extract key details like major version and patch level for vulnerability research.

**Command** (Use built-in PowerShell parsing):
```powershell
$result = Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query "select * from openquery('<DBSERVERNAME\DBInstance>','select @@version')" -Verbose
$result | Select-String -Pattern "SQL Server (\d+)" | ForEach-Object { $_.Matches.Groups[1].Value }
```

> This follow-up parses the output to isolate the major version number (e.g., "2019"). Success is indicated by a clean version string without errors like "Login failed" or "Invalid object name". Use this to cross-reference against CVE databases for exploitable weaknesses.
