---
id: 9c54787c-48ff-4bf2-a6e5-5904f075568d
name: show-is-superuser
type: command
executor: sql
data: SHOW is_superuser;
output: null
created_at: '2023-04-06T03:56:35.596384+00:00'
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

# show-is-superuser

## Command

```sql
SHOW is_superuser;
```

## Description

This SQL command displays the superuser status of the current PostgreSQL session. It is used during database reconnaissance to quickly determine if the connected user has administrative privileges, which is essential for planning escalation or exploitation paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; runs in the current session | N/A |

## Examples

### Basic Usage

```sql
SHOW is_superuser;
```

### In psql Client

Connect via psql and execute directly:

```bash
psql -h target_host -U current_user -d database_name -c "SHOW is_superuser;"
```

## Expected Output

If the user is a superuser:

```
 is_superuser 
--------------
 on
(1 row)
```

If not:

```
 is_superuser 
--------------
 off
(1 row)
```

## Related

- [[procedures/Check-PostgreSQL-Current-User-Superuser-Privileges]]
