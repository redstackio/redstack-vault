---
id: 864e1527-58c4-41e5-a59b-a8c8af95713b
name: postgresql-select-with-limit
type: command
executor: sql
data: SELECT * FROM customers LIMIT 5 OFFSET 0;
output: null
created_at: '2023-04-06T03:56:35.763818+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Databases
tags:
  - exfiltration
  - postgresql
verified: true
validated: true
---

# postgresql-select-with-limit

## Command

```sql
SELECT * FROM customers LIMIT 5 OFFSET 0;
```

## Description

Retrieves a limited number of rows from a PostgreSQL table, useful for paginated exfiltration to manage response sizes in injection attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| customers | Target table name | Yes |
| 5 | Maximum rows to return | Yes |
| 0 | Starting offset for pagination | No |

## Examples

### Basic Usage

```sql
SELECT * FROM customers LIMIT 5;
```

### Advanced Usage

```sql
SELECT * FROM customers LIMIT 10 OFFSET 10;
```

## Expected Output

Tabular results limited to 5 rows:

 id | name | email
----|------|------
 1  | Alice| a@example.com
 2  | Bob  | b@example.com
 ...

## Related

- [[procedures/PostgreSQL-XML-Data-Exfiltration]]
- [[commands/postgresql-query-to-xml-custom]]
