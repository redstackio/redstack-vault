---
id: 6cb4f1f4-ae5c-4937-bc1f-d88be48ff77b
name: Enumerate-Linked-MSSQL-Servers-via-Database-Crawling
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.070542+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Crawl Links for Instances in the Domain]]'
  - '[[tags/Linked Database]]'
  - '[[tags/MSSQL Server]]'
  - sql-enumeration
  - domain-discovery
commands:
  - '[[commands/powershell-get-sql-instances-and-links]]'
  - '[[commands/sql-query-sysservers]]'
platforms:
  - Windows
tools: []
validated: true
---

# Enumerate-Linked-MSSQL-Servers-via-Database-Crawling

## Summary

This procedure enumerates linked MSSQL servers in a domain by querying SQL instances and their linked database connections. It identifies remote SQL servers connected via linked servers, which can reveal potential lateral movement paths or additional targets for privilege escalation in an Active Directory environment.

## Description

Linked servers in MSSQL allow databases on different instances to connect and query each other, often configured for legitimate data sharing but exploitable for discovery. This technique involves using PowerShell modules to discover SQL instances in the domain and then crawling their linked server configurations to map out connected MSSQL servers. It targets the sysservers system view and linked server metadata to extract server names, providers, and connection details. This is particularly useful in red team engagements for mapping internal SQL infrastructure without direct network scans, assuming authenticated access to at least one SQL instance. The procedure assumes the use of SQL Server PowerShell modules like SQLPS or custom extensions such as those from PowerSploit. Outcomes include a list of linked instances, which can inform further attacks like credential dumping or remote execution on discovered servers.

## Requirements

1. Authenticated domain access with SQL login credentials to at least one MSSQL instance.
2. PowerShell environment with SQL Server modules installed (e.g., SQLPS or Invoke-SQLcmd).
3. Network connectivity to domain SQL servers (typically TCP 1433).
4. Administrative or db_owner privileges on the target database for querying system views.

## Defense

- Avoid unnecessary linked server configurations; use views or synonyms for cross-database queries within the same instance.
- Implement network segmentation to isolate SQL servers and limit inter-server connections.
- Monitor SQL Server logs and audit queries to sysservers or linked server metadata for anomalous access.
- Enable SQL Server auditing for EXECUTE AS and linked server usage, and use least-privilege accounts for links.

## Objectives

1. Discover linked MSSQL servers to identify potential targets for lateral movement.
2. Enumerate SQL instances and their interconnections in the domain.
3. Map the SQL infrastructure for privilege escalation opportunities.

## Instructions

### Step 1: Retrieve Domain SQL Instances and Linked Servers

**Context**: First, discover all SQL instances in the domain and query their linked server configurations to identify remote connections. This step uses a piped PowerShell command to enumerate instances and extract link details, providing verbose output for troubleshooting.

**Command** ([[commands/powershell-get-sql-instances-and-links]]):

```powershell
Get-SQLInstanceDomain | Get-SQLServerLink -Verbose
```

> This command fetches domain SQL instances via Get-SQLInstanceDomain, then pipes them into Get-SQLServerLink to retrieve linked server information. The -Verbose flag outputs detailed progress and errors. Look for the DatabaseLinkName field in the results to identify valid links (non-null values indicate active linked servers). Expected output includes server names, link statuses, and provider details, such as a table listing remote servers like 'LINKED_SERVER1' with provider 'SQL Server'.

### Step 2: Query Sysservers for Additional Link Details

**Context**: Supplement the PowerShell output by directly querying the sysservers system view on the master database of a target instance. This verifies linked servers and extracts details like server IDs, names, and connection statuses, helping confirm crawlable links.

**Command** ([[commands/sql-query-sysservers]]):

```sql
select * from master..sysservers
```

> Execute this SQL query using sqlcmd, Invoke-Sqlcmd, or a similar tool against a discovered SQL instance. It returns all rows from sysservers, including columns like srvid (server ID), name (linked server name), and status (connection flags). Valid linked servers will have entries beyond the local server (name != '##MS_SQLServer_Local##' or similar). Expected output is a result set showing linked servers, e.g., rows with names like 'REMOTE_DC01' and status indicating RPC or data access enabled. Cross-reference with Step 1 output to build a complete map of linked instances.

### Step 3: Analyze and Crawl Identified Links

**Context**: Review the outputs from previous steps to identify valid links, then iteratively connect to discovered remote servers (using credentials from the initial access) to repeat the enumeration. This creates a crawl of the linked database graph.

**Code** ([[codes/PowerShell-Enumerate-Linked-SQL-Servers]]):

Embed or execute the provided PowerShell code snippet to automate the initial query if needed for scripting.

> Manually connect to each identified linked server (e.g., via sqlcmd -S LINKED_SERVER -U username -P password) and run the sysservers query again. Document the chain of links to enumerate the full domain SQL topology. Success is indicated by discovering new instances not visible from the initial access point.
