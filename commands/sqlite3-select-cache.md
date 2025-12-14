---
data: SELECT * FROM my_cache_table;
tags:
  - query
  - cache
type: command
output: 'Rows of cache data, including cache_key, value (pickled), and rowid'
executor: sql
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.645Z'
id: 617285b9-2ae1-4fef-9f9d-9283bec4c2cb
verified: false
validated: true
submitted: true
---
# sqlite3-select-cache

## Command

```sql
SELECT * FROM my_cache_table;
```

## Description

Queries all rows from the Django cache table to identify entries for payload injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| * | Select all columns | Yes |
| my_cache_table | Name of the cache table | Yes |

## Examples

### Basic Usage

```sql
SELECT * FROM my_cache_table;
```

### Advanced Usage

```sql
SELECT rowid, cache_key FROM my_cache_table LIMIT 5;
```

> Limits to recent entries.

## Expected Output

Rows showing cache_key, value (base64 pickled), rowid; e.g., identifies rowid=2.

## Related

- [[Related Procedure]]
