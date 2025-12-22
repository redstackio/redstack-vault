---
type: command
executor: sql
data: |-
  sp_configure 'external scripts enabled', 1;
  RECONFIGURE;
output: null
platforms:
  - Windows
tags:
  - mssql
  - execution
verified: true
validated: true
---

# mssql-enable-external-scripts

## Command

```sql
sp_configure 'external scripts enabled', 1;
RECONFIGURE;
```

## Description

This SQL command enables the execution of external scripts (e.g., Python, R) in Microsoft SQL Server by setting the advanced configuration option to 1 and applying the change. Use this when you need to integrate non-T-SQL scripting into SQL queries, such as for data analysis or, in adversarial contexts, to enable code execution on the host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'external scripts enabled' | The configuration option name (quoted string) | Yes |
| 1 | Value to enable the feature (0 to disable) | Yes |
| RECONFIGURE | Applies the configuration change immediately | Yes |

## Examples

### Basic Usage

```sql
sp_configure 'external scripts enabled', 1;
RECONFIGURE;
```

### Verify Configuration

```sql
sp_configure 'external scripts enabled';
```

> Expected output: "Config_value" column shows 1 if enabled.

## Expected Output

Messages: "Configuration option 'external scripts enabled' changed from 0 to 1. Run the RECONFIGURE statement to install." followed by "RECONFIGURE Statement: Changes applied."

## Related

- [[procedures/Enable-and-Execute-External-Scripts-in-MSSQL]]
