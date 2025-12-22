---
id: 61507690-b5bd-4869-a45f-beb6c8b9ff96
name: mssql-select-version
type: command
executor: sql
data: SELECT @@version
output: null
created_at: '2023-04-06T03:56:35.420525+00:00'
updated_at: '2023-04-10T20:23:21.065431+00:00'
platforms:
  - Windows
  - Linux
tags:
  - mssql
  - enumeration
  - discovery
verified: true
validated: true
---

# mssql-select-version

## Command

```sql
SELECT @@version
```

## Description

This SQL command queries the Microsoft SQL Server instance to return detailed version information, including the product version, build number, edition, and underlying OS. Use it during reconnaissance to identify the target for vulnerability research.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This is a standalone query; parameters depend on the execution tool (e.g., server, username in sqlcmd). | No |

## Examples

### Basic Usage

Execute directly in a SQL client:

```sql
SELECT @@version;
```

### Via sqlcmd Tool

```bash
sqlcmd -S target-server -U user -P pass -Q "SELECT @@version"
```

### In SQL Injection Payload

```sql
' UNION ALL SELECT @@version --
```

## Expected Output

A string like:

```
Microsoft SQL Server 2019 (RTM) - 15.0.2000.5 (X64) 
	Sep 24 2019 18:10:08 
	Copyright (C) 2019 Microsoft Corporation
	Developer Edition (64-bit) on Windows Server 2019 Datacenter 10.0 <X64> (Build 17763: )

(1 rows affected)
```

This reveals the version (15.0.2000.5), edition (Developer), and OS (Windows Server 2019).

## Related

- [[procedures/Enumerate-MSSQL-Version]]
- [[tools/sqlcmd]] (for execution)
