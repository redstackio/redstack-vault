---
type: procedure
description: >-
  Identifies the version of a Microsoft SQL Server instance using PowerShell
  queries to assess vulnerabilities or available features.
verified: true
submitted: false
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Information Discovery]]'
  - '[[Software Discovery]]'
sub_techniques: []
tags:
  - mssql
  - discovery
  - version-query
  - identify-instances
commands:
  - '[[commands/get-sqlinstance-domain-powershell]]'
  - '[[commands/get-sql-query-version-powershell]]'
platforms:
  - Windows
tools: []
validated: true
---

# Query-MSSQL-Server-Version

## Summary

This procedure retrieves the version information of Microsoft SQL Server instances within a domain using PowerShell and the SQLServer module. It helps identify potential vulnerabilities by determining the exact server version, enabling targeted exploitation or patching decisions in offensive or defensive security operations.

## Description

Querying the MSSQL Server version involves enumerating SQL instances in the domain and executing a standard SQL query (@@version) against them. This technique is part of discovery activities, allowing attackers to map the environment and check for known exploits associated with specific versions, such as outdated patches leading to remote code execution. Defensively, it aids in auditing systems for compliance and vulnerability management. The process requires authenticated access to the SQL instances and assumes the target is a Windows domain with MSSQL deployed. Expected outcomes include version strings like 'Microsoft SQL Server 2019 (RTM) - 15.0.2000.5', which can be cross-referenced with CVE databases.

## Requirements

1. Authenticated domain user credentials with access to query SQL instances.
2. PowerShell environment with the SQLServer module installed (Import-Module SQLServer).
3. Network connectivity to the target domain controllers or SQL servers (typically ports 1433/TCP for SQL).

## Defense

- Apply the latest security patches to MSSQL instances to mitigate version-specific exploits.
- Restrict SQL query access using role-based permissions and firewall rules to authorized users only.
- Monitor SQL Server logs and PowerShell execution logs for anomalous queries like @@version from unexpected sources.

## Objectives

1. Enumerate all SQL Server instances in the target domain.
2. Execute version queries against discovered instances.
3. Obtain detailed version information for vulnerability assessment.

## Instructions

### Step 1: Enumerate SQL Instances in Domain

**Context**: This step discovers all running SQL Server instances across the domain, providing targets for the version query. It uses the Get-SQLInstanceDomain cmdlet to query Active Directory or network broadcasts for instances.

**Command** ([[commands/get-sqlinstance-domain-powershell]]):
```powershell
Get-SQLInstanceDomain
```

> This cmdlet lists SQL instances with details like server name and instance name. Pipe the output to subsequent commands for automation. Expected output includes a table of instances, e.g., ServerName: DC01, InstanceName: MSSQLSERVER.

### Step 2: Execute Version Query on Instances

**Context**: Once instances are identified, pipe the results to execute the SQL query 'SELECT @@VERSION' against each one. This reveals the full version string, edition, and build details, helping identify exploitable configurations.

**Command** ([[commands/get-sql-query-version-powershell]]):
```powershell
Get-Query "SELECT @@VERSION"
```

> Run this after Step 1 by piping: Get-SQLInstanceDomain | Get-Query "SELECT @@VERSION". The query returns version details for each instance. If no pipe, specify the instance manually via parameters. Expected output: A result set with columns like Version (e.g., 'Microsoft SQL Server 2019 (RTM-CU12) (KB5015680) - 15.0.2094.3 (X64) ...').

### Step 3: Verify and Parse Results

**Context**: Review the output for version parsing. If multiple instances return, filter by name or export to file for analysis (e.g., | Export-Csv versions.csv). Decision point: If no instances found, check credentials or network access; otherwise, proceed to vulnerability lookup.

**Command** (use previous commands with export):
```powershell
Get-SQLInstanceDomain | Get-Query "SELECT @@VERSION" | Export-Csv -Path versions.csv -NoTypeInformation
```

> This saves results for offline review. Success is confirmed by non-empty CSV with version data.
