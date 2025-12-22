---
id: d31dea9e-90dc-4000-bd6a-1e02bfdad2c0
name: mssql-switch-back-to-full-recovery
type: command
executor: sql
data: |-
  ALTER DATABASE database_name SET RECOVERY FULL
  GO
output: null
created_at: '2023-04-06T03:56:33.914999+00:00'
updated_at: '2023-04-10T20:22:42.032361+00:00'
platforms:
  - Windows
tags:
  - mssql
  - defense-evasion
verified: true
validated: true
---

# mssql-switch-back-to-full-recovery

## Command

```sql
ALTER DATABASE database_name SET RECOVERY FULL
GO
```

## Description

This command restores an MSSQL database's recovery model to FULL after temporary changes, ensuring point-in-time recovery and full logging to minimize operational impact.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| database_name | Name of the database to modify | Yes |

## Examples

### Basic Usage

```sql
ALTER DATABASE MyDB SET RECOVERY FULL
GO
```

### Advanced Usage

Switch back and verify:

```sql
ALTER DATABASE MyDB SET RECOVERY FULL
GO
SELECT recovery_model_desc FROM sys.databases WHERE name = 'MyDB'
```

## Expected Output

Commands completed successfully.
No rows affected. (confirmation of alteration)

## Related

- [[procedures/MSSQL-Read-File-via-INI-Disclosure]]
- [[commands/mssql-check-recovery-model]]
