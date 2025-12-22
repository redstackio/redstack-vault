---
id: b527415d-2adf-4ccc-b542-2d7686d78b0b
name: mssql-switch-to-bulk-logged-recovery
type: command
executor: sql
data: |-
  ALTER DATABASE database_name SET RECOVERY BULK_LOGGED
  GO
output: null
created_at: '2023-04-06T03:56:33.914917+00:00'
updated_at: '2023-04-10T20:22:42.032361+00:00'
platforms:
  - Windows
tags:
  - mssql
  - defense-evasion
verified: true
validated: true
---

# mssql-switch-to-bulk-logged-recovery

## Command

```sql
ALTER DATABASE database_name SET RECOVERY BULK_LOGGED
GO
```

## Description

This command alters the recovery model of an MSSQL database to BULK_LOGGED, enabling bulk operations like file imports/reads via OpenRowset without full transaction logging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| database_name | Name of the database to modify | Yes |

## Examples

### Basic Usage

```sql
ALTER DATABASE MyDB SET RECOVERY BULK_LOGGED
GO
```

### Advanced Usage

Switch and verify in one session:

```sql
ALTER DATABASE MyDB SET RECOVERY BULK_LOGGED
GO
SELECT recovery_model_desc FROM sys.databases WHERE name = 'MyDB'
```

## Expected Output

Commands completed successfully.
No rows affected. (or similar confirmation; no data returned on success)

## Related

- [[procedures/MSSQL-Read-File-via-INI-Disclosure]]
- [[commands/mssql-check-recovery-model]]
