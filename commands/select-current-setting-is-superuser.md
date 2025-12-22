---
id: cb5c403a-56f0-45e7-9c4c-f5563afdc14e
name: select-current-setting-is-superuser
type: command
executor: sql
data: SELECT current_setting('is_superuser');
output: null
created_at: '2023-04-06T03:56:35.596487+00:00'
updated_at: '2023-04-10T20:23:22.132689+00:00'
platforms:
  - Linux
  - Database
tags:
  - postgresql
  - discovery
verified: true
validated: true
---

# select-current-setting-is-superuser

## Command

```sql
SELECT current_setting('is_superuser');
```

## Description

This SQL command retrieves the 'is_superuser' configuration setting for the current PostgreSQL session as a string value. It is useful for scripted checks or when integrating into application logic to detect privilege levels dynamically.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; uses current session context | N/A |

## Examples

### Basic Usage

```sql
SELECT current_setting('is_superuser');
```

### Remote Execution via psql

```bash
psql -h target_host -U current_user -d database_name -c "SELECT current_setting('is_superuser');"
```

## Expected Output

If superuser:

```
 current_setting 
----------------
 on
(1 row)
```

If not:

```
 current_setting 
----------------
 off
(1 row)
```

## Related

- [[procedures/Check-PostgreSQL-Current-User-Superuser-Privileges]]
