---
type: command
executor: sql
data: SELECT @@VERSION
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - mssql
  - version-check
verified: true
validated: true
---

# mssql-retrieve-server-version

## Command

```sql
SELECT @@VERSION
```

## Description

This SQL command queries the MSSQL server to return the full version string, helping identify the database version for selecting appropriate hash extraction methods.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard SQL query; no parameters needed | No |

## Examples

### Basic Usage

```sql
SELECT @@VERSION
```

## Expected Output

Microsoft SQL Server 2005 - 9.00.1399.06 (Intel X86)   Oct 14 2005 00:33:37   Copyright (c) 1988-2005 Microsoft Corporation  Standard Edition on Windows NT 5.2 (Build 3790: Service Pack 2)

## Related

- [[procedures/MSSQL-Server-Password-Hash-Extraction-and-Cracking]]
