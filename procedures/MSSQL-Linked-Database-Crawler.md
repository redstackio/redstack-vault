---
type: procedure
description: >-
  Discover and crawl linked databases in an MSSQL instance to identify potential
  lateral movement paths.
verified: true
submitted: false
created_at: '2023-04-06T03:56:20Z'
updated_at: '2023-04-10T20:36:31Z'
tactics:
  - '[[Credential Access]]'
  - '[[Discovery]]'
techniques:
  - '[[Network Service Scanning]]'
  - '[[Network Sniffing]]'
sub_techniques: []
tags:
  - mssql
  - linked-servers
  - discovery
  - lateral-movement
  - crawl-links
commands:
  - '[[commands/get-sqlserverlinkcrawl-crawl-instance]]'
  - '[[commands/sqlcmd-execute-openquery-linked-servers]]'
platforms:
  - Windows
  - SQL Server
tools:
  - '[[procedures/MSSQL-Linked-Database-Crawler]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# MSSQL-Linked-Database-Crawler

## Summary

This procedure uses a PowerShell-based crawler to discover linked databases in a target MSSQL instance, enabling identification of interconnected database servers for lateral movement or further discovery. It queries system views to enumerate linked servers and recursively crawls them to uncover additional links, providing a map of database relationships in the environment.

## Description

In an MSSQL environment, linked servers allow one database to query remote instances, which can be exploited for discovery and lateral movement if credentials are compromised. This procedure leverages the Get-SQLServerLinkCrawl PowerShell cmdlet to initiate the crawl on a specified instance, retrieving linked server details from sys.servers. It then uses dynamic SQL queries via OPENQUERY to probe deeper into linked instances, revealing further connections. This is particularly useful in Active Directory-integrated environments where MSSQL instances span multiple servers. The approach assumes authenticated access to the initial instance and relies on the linked server configurations for propagation. Potential outcomes include a list of accessible remote databases, which can inform targeted attacks like credential dumping or data exfiltration.

## Requirements

1. Valid credentials with db_owner or higher privileges on the target MSSQL instance to query system catalogs and execute remote queries.
2. PowerShell environment with the necessary SQL Server module (e.g., SqlServer or custom crawler module) installed.
3. Network access to the target MSSQL instance (default port 1433) and any linked servers.
4. sqlcmd utility available for executing ad-hoc SQL queries if not using a GUI tool like SSMS.

## Defense

- Regularly audit linked servers using SQL Server Management Studio or scripts to remove unnecessary links and enforce least privilege.
- Enable SQL Server auditing for queries against sys.servers and OPENQUERY executions to detect anomalous discovery activity.
- Implement network segmentation to limit lateral connectivity between MSSQL instances and monitor for unusual SQL traffic patterns.
- Use credential guarding and just-in-time access to prevent propagation of privileges across linked servers.

## Objectives

1. Enumerate all linked servers configured on the target MSSQL instance.
2. Recursively crawl linked servers to discover additional database connections.
3. Map the database linkage topology for planning lateral movement or identifying high-value targets.

## Instructions

### Step 1: Install and Load the Crawler Tool

**Context**: Ensure the MSSQL Linked Database Crawler tool is available in your PowerShell environment. This tool provides the Get-SQLServerLinkCrawl cmdlet for automated discovery.

Install or import the module as per the tool documentation.

### Step 2: Initiate the Crawl on the Target Instance

**Context**: Use the crawler to query the target MSSQL instance for linked servers. This step starts the discovery process and provides verbose output on found links.

**Command** ([[commands/get-sqlserverlinkcrawl-crawl-instance]]):
```powershell
Get-SQLServerLinkCrawl -Instance "<DBSERVERNAME\DBInstance>" -Verbose
```

> This command connects to the specified instance and enumerates linked servers from sys.servers. The -Verbose flag outputs details on each discovered link, including server names and connection strings. Replace <DBSERVERNAME\DBInstance> with the actual server path (e.g., "sqlserver01\default").

**Expected Output**: A list of linked servers with details like name, provider, and data source, along with verbose logs of the crawling process.

### Step 3: Query Linked Servers Using OPENQUERY

**Context**: For deeper inspection, execute a nested OPENQUERY to retrieve linked server information from remote instances. This verifies connectivity and discovers further links.

**Command** ([[commands/sqlcmd-execute-openquery-linked-servers]]):
```bash
sqlcmd -S "<DBSERVERNAME>" -E -Q "select * from openquery('<instance>','select * from openquery('<instance2>',''select * from master..sysservers'')')"
```

> This runs the SQL query via sqlcmd, assuming Windows authentication (-E). It uses double-nested OPENQUERY to hop through linked servers. Replace placeholders with actual instance names discovered in Step 2. The query targets master..sysservers on the remote instance.

**Expected Output**: A result set from sysservers on the remote linked server, showing server IDs, names, and statuses for further links.

### Step 4: Analyze and Document Results

**Context**: Review the output from previous steps to map the linkage. Save results to a file for further analysis or integration into attack planning.

Export verbose output to a log file using PowerShell redirection (e.g., | Tee-Object -FilePath crawl_results.txt). Look for patterns in linked server configurations that indicate trust relationships or shared credentials.

**Expected Output**: A documented topology of linked databases, potentially including accessible remote resources.

### Step 5: Verify Connectivity to Discovered Links

**Context**: Test connections to enumerated linked servers to confirm exploitability.

Use [[commands/sqlcmd-execute-openquery-linked-servers]] iteratively on each discovered instance to validate remote access and crawl depth.

**Expected Output**: Successful query responses from remote servers without authentication errors.
