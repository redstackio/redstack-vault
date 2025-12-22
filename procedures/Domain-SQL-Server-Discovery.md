---
id: 6ba4d15f-0028-4ade-b226-885dcd5822ae
name: Domain-SQL-Server-Discovery
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:19.802253+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Remote System Discovery|T1018 - Remote System Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Discover Domain SQL Server Instances]]'
  - '[[tags/Identify Instances and Databases]]'
  - '[[tags/MSSQL Server]]'
commands:
  - '[[commands/get-sql-instance-domain-verbose]]'
  - '[[commands/get-sql-server-info-from-instances]]'
  - '[[commands/get-database-names-from-instances]]'
platforms:
  - Windows
tools: []
validated: true
---

# Domain-SQL-Server-Discovery

## Summary

Domain SQL Server Discovery is a procedure used by attackers to identify SQL Server instances within a Windows domain. This technique helps map the database infrastructure, revealing potential targets for further exploitation such as credential dumping or data exfiltration. It leverages domain queries to enumerate instances, retrieve server details, and list databases without direct access to the servers.

## Description

In a Windows Active Directory environment, SQL Server instances can be discovered by querying domain resources for services registered under SQL-related SPNs or browser protocols. Attackers with domain access (e.g., via compromised credentials) use PowerShell modules like SQLServer to perform this enumeration. This procedure assumes the use of the SqlServer PowerShell module, which must be imported. The approach is non-intrusive initially but can lead to targeted attacks on identified databases. It is particularly useful in lateral movement phases where understanding the infrastructure aids in selecting high-value targets like production databases.

## Requirements

1. Domain-joined Windows host with PowerShell execution policy allowing scripts.
2. SqlServer PowerShell module installed (Import-Module SqlServer).
3. Valid domain credentials with query access (e.g., domain user account).
4. Network connectivity to domain controllers or SQL browsers (UDP 1434, TCP 1433).

## Defense

- Disable or restrict access to unnecessary protocols and ports like UDP 1434 (SQL Browser) and TCP 1433 (SQL Server).
- Implement network segmentation to limit access to sensitive systems, using firewalls to block lateral discovery traffic.
- Monitor network traffic for suspicious activity, such as unusual PowerShell executions or queries to domain services from non-admin accounts.
- Enable SQL Server auditing and restrict SPN registrations to prevent easy enumeration.

## Objectives

1. Identify SQL Server instances that are part of a Windows domain.
2. Gain an understanding of the domain's database infrastructure, including versions and databases.
3. Prepare for subsequent attacks like SQL injection or credential attacks on discovered instances.

## Instructions

### Step 1: Enumerate SQL Instances in Domain

**Context**: This step discovers all SQL Server instances registered in the current domain by querying domain resources. It provides a list of instances that can be targeted for further reconnaissance. Use this as the starting point to build a pipeline for deeper enumeration.

**Command** ([[commands/get-sql-instance-domain-verbose]]):
```powershell
Get-SQLInstanceDomain -Verbose
```

> This command uses the SqlServer module to scan the domain for SQL instances via browser protocols or AD queries. The -Verbose flag provides detailed output on the discovery process. Expected output includes a list of instance names, such as 'SERVER1\SQLEXPRESS' or 'SERVER2', along with connection details.

### Step 2: Retrieve Detailed Server Information

**Context**: Once instances are identified, pipe the results to gather version, edition, and configuration details for each SQL Server. This helps assess vulnerabilities, such as outdated versions prone to known exploits.

**Command** ([[commands/get-sql-server-info-from-instances]]):
```powershell
Get-SQLInstanceDomain | Get-SQLServerInfo -Verbose
```

> Pipe the output from Step 1 into Get-SQLServerInfo to fetch properties like SQL Server version (e.g., 2019), edition (e.g., Enterprise), and authentication mode. The -Verbose flag logs connection attempts. Expected output is a table or object per instance showing properties like 'Version: 15.0.2000.5', aiding in vulnerability prioritization.

### Step 3: List Database Names on Instances

**Context**: For each discovered instance, enumerate user databases to identify potential data stores. Exclude system databases with -NoDefaults to focus on custom ones that may hold sensitive information.

**Command** ([[commands/get-database-names-from-instances]]):
```powershell
Get-SQLInstanceDomain | Get-SQLDatabase -NoDefaults
```

> This pipes instance data to Get-SQLDatabase, retrieving database names like 'HR_Database' or 'Finance_Prod'. The -NoDefaults flag skips tempdb, master, etc. Expected output lists databases per instance, such as 'DatabaseName: PayrollDB', revealing business-critical assets.
