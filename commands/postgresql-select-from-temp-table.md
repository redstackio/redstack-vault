---
type: command
executor: sql
data: SELECT * FROM temp_passwd LIMIT 5;
output: null
platforms:
  - PostgreSQL
tags:
  - query
  - data-exfil
verified: true
validated: true
---

# postgresql-select-from-temp-table

## Command

```sql
SELECT * FROM temp_passwd LIMIT 5;
```

## Description

Queries the temp table to retrieve imported file data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| temp_passwd | Table name | Yes |
| LIMIT 5 | Row limit | No |

## Examples

### Basic Usage

```sql
SELECT * FROM temp_passwd;
```

### Advanced Usage

```sql
SELECT line FROM temp_passwd WHERE line LIKE '%root%';
```

## Expected Output

Rows from the table, e.g.:

line
----
root:x:0:0:root:/root:/bin/bash

## Related

- [[procedures/Read-Files-via-PostgreSQL-Server-Functions]]
