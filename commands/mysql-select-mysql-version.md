---
id: d0fd07e1-3081-4231-85be-585d8714bf41
name: MySQL Select MySQL Version
type: command
executor: sql
data: SELECT @@version; SELECT version();
output: null
created_at: '2023-04-06T03:56:36.832753+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - mysql
  - discovery
verified: true
validated: true
---

# MySQL Select MySQL Version

## Command

```sql
SELECT @@version;
-- OR
SELECT version();
```

## Description

These commands retrieve the full MySQL server version, including build details, to identify the database system during SQLi enumeration or WAF bypass attempts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @@version | System variable for full server version | Yes |
| version() | Function returning server version | Yes |

## Examples

### Basic Usage

```sql
SELECT @@version;
```

### Alternative

```sql
SELECT version();
```

### In Injection Context

```sql
' UNION SELECT @@version--
```

## Expected Output

+-------------------------+
| @@version               |
+-------------------------+
| 5.6.31-0ubuntu0.15.10.1 |
+-------------------------+

## Related

- [[procedures/SQL Injection WAF Bypass using MySQL Specific Commands]]
- [[MySQL Select InnoDB Version]]
