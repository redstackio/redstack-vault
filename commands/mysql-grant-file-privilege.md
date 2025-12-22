---
id: 27bb1736-8814-4ca8-93df-d5ae7beed0c2
name: mysql-grant-file-privilege
type: command
executor: sql
data: GRANT FILE ON *.* TO 'root'@'localhost'; FLUSH PRIVILEGES;
output: null
created_at: '2023-04-06T03:56:34.767876+00:00'
updated_at: '2023-04-10T20:22:51.267705+00:00'
platforms:
  - Linux
tags:
  - mysql
  - privilege-escalation
verified: true
validated: true
---

# mysql-grant-file-privilege

## Command

```sql
GRANT FILE ON *.* TO 'root'@'localhost'; FLUSH PRIVILEGES;
```

## Description

This command grants the FILE privilege to the root user on localhost, enabling LOAD_FILE and related functions. Use only if you have administrative access; in injection scenarios, this requires the injecting user to have GRANT OPTION.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'root'@'localhost' | Target user and host | Yes |
| *.* | All databases and tables | Yes |
| FLUSH PRIVILEGES | Reloads grant tables to apply changes immediately | Yes |

## Examples

### Basic Usage

```sql
GRANT FILE ON *.* TO 'root'@'localhost'; FLUSH PRIVILEGES;
```

### For Current User

```sql
GRANT FILE ON *.* TO CURRENT_USER(); FLUSH PRIVILEGES;
```

## Expected Output

Query OK, 0 rows affected (0.00 sec)
Query OK, 1 row affected (0.01 sec)

No errors indicate success; verify with SHOW GRANTS.

## Related

- [[procedures/mysql-file-content-extraction-via-injection]]
- [[commands/mysql-check-file-privilege]]
