---
id: f5555197-62cd-45cd-b344-49038113cc4a
name: mssql-identify-sensitive-information-get-tables-and-column-details
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:19.917908+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Data from Local System|T1005 - Data from Local System]]'
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Get Tables from a Specific Database]]'
  - '[[tags/Identify Sensitive Information]]'
  - '[[tags/MSSQL Server]]'
  - mssql
  - database-discovery
  - sensitive-data
commands:
  - '[[commands/get-mssql-tables-from-database]]'
  - '[[commands/get-mssql-column-details-from-table]]'
platforms:
  - Windows
tools:
  - '[[tools/dbatools]]'
validated: true
---

# mssql-identify-sensitive-information-get-tables-and-column-details

## Summary

This procedure uses PowerShell commands from the dbatools module to enumerate tables within a specific MSSQL database and then retrieve detailed column information for those tables, enabling the identification of sensitive data such as usernames, passwords, or confidential records. It is particularly useful in red team engagements for discovering database structures that may contain valuable information, or in defensive audits to assess data exposure risks.

## Description

In an offensive security context, this procedure allows an attacker with database access to map out the schema of an MSSQL instance, focusing on tables and columns that might hold sensitive information. By first listing tables in a target database and then inspecting column details like data types (e.g., varchar for strings potentially holding credentials), nullability, and other metadata, the procedure reveals potential targets for data exfiltration. The technical approach leverages the dbatools PowerShell module, which interacts with SQL Server via SMO (SQL Server Management Objects) to query system views like INFORMATION_SCHEMA.TABLES and INFORMATION_SCHEMA.COLUMNS without requiring direct SQL injection or advanced privileges beyond read access to metadata. Prerequisites include valid credentials for the MSSQL instance, and outcomes include a structured view of the database schema that can guide further collection efforts. This maps to discovery of system information and collection of data from local systems in MITRE ATT&CK.

## Requirements

1. Valid credentials with read access to the MSSQL database metadata (e.g., db_datareader role or equivalent).
2. PowerShell environment with the dbatools module installed.
3. Network access to the MSSQL server instance (default port 1433).
4. Knowledge of the target database name, which can be obtained via prior enumeration (e.g., using Get-SQLDatabase).

## Defense

- Implement principle of least privilege by restricting database roles to only necessary permissions, avoiding broad metadata read access for service accounts.
- Enable SQL Server auditing for SELECT queries on system views like INFORMATION_SCHEMA to log schema enumeration attempts.
- Use database encryption (e.g., TDE) and column-level encryption for sensitive data to limit exposure even if schema is discovered.
- Regularly scan for and remove unnecessary databases or tables, and monitor for anomalous PowerShell execution on systems with dbatools installed.

## Objectives

1. Enumerate all tables in a specified MSSQL database to identify potential data stores.
2. Retrieve column details for targeted tables to detect sensitive data types and structures.
3. Assess the overall security posture by highlighting exposed sensitive information in the database schema.

## Instructions

### Step 1: Enumerate Tables in the Target Database

**Context**: This step retrieves a list of all tables within the specified database, excluding system defaults if specified, to provide an overview of the data structure. Use this to identify tables likely containing sensitive information based on names (e.g., users, credentials).

**Command** ([[commands/get-mssql-tables-from-database]]):
```powershell
Get-SQLInstanceDomain | Get-SQLTable -DatabaseName <DatabaseName> -NoDefaults
```

> Replace `<DatabaseName>` with the actual database name (e.g., 'AdventureWorks'). This command connects to the SQL instance via domain discovery and pipes the instance object to Get-SQLTable, which queries the schema. Expected output includes table names, schemas, and types. If `-NoDefaults` is omitted, it includes default system tables; use it to focus on user-created tables.

### Step 2: Retrieve Column Details for a Specific Table

**Context**: After identifying a table of interest from Step 1, this step fetches detailed column information such as names, data types, lengths, and nullability. Analyze for sensitive indicators like varchar(255) columns that might hold passwords or emails.

**Command** ([[commands/get-mssql-column-details-from-table]]):
```powershell
Get-SQLInstanceDomain | Get-SQLColumn -DatabaseName <DatabaseName> -TableName <TableName>
```

> Replace `<DatabaseName>` with the database name and `<TableName>` with the target table (e.g., 'Users'). This queries column metadata via SMO. Expected output lists columns with properties like DataType (e.g., 'varchar'), MaxLength, IsNullable. Review for patterns indicating sensitive data and proceed to query actual contents if permissions allow.
