---
id: ef0f3bec-9f5f-4a5b-a608-9654150fa9a5
name: sql-enable-ole-automation
type: command
executor: sql
data: >-
  EXEC sp_configure 'show advanced options', 1; GO RECONFIGURE; GO EXEC
  sp_configure 'Ole Automation Procedures', 1; GO RECONFIGURE; GO
output: null
created_at: '2023-04-06T03:56:20.471863+00:00'
updated_at: '2023-04-10T20:36:31.774363+00:00'
platforms:
  - Windows
tags:
  - configuration
  - ole
verified: true
validated: true
---

# sql-enable-ole-automation

## Command

```sql
EXEC sp_configure 'show advanced options', 1;
GO
RECONFIGURE;
GO
EXEC sp_configure 'Ole Automation Procedures', 1;
GO
RECONFIGURE;
GO
```

## Description

Enables OLE Automation procedures on the MSSQL instance for COM object usage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Built-in SQL commands; run as sysadmin | No |

## Examples

### Basic Usage

Run the full script in SSMS or sqlcmd.

## Expected Output

Configuration option changed successfully. RECONFIGURE completed.

## Related

- [[procedures/MSSQL-OLE-Automation-Command-Execution]]
