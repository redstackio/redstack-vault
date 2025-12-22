---
type: command
executor: sql
data: SELECT lo_import('/etc/shadow');
output: null
platforms:
  - PostgreSQL
tags:
  - large-object
  - import
verified: true
validated: true
---

# postgresql-import-file-as-large-object

## Command

```sql
SELECT lo_import('/etc/shadow');
```

## Description

Imports a file as a large object and returns its OID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| '/etc/shadow' | File path | Yes |

## Examples

### Basic Usage

```sql
SELECT lo_import('config.txt');
```

### Advanced Usage

```sql
SELECT lo_import('/var/log/postgresql.log');
```

## Expected Output

The OID integer, e.g. 16420.

## Related

- [[procedures/Read-Files-via-PostgreSQL-Server-Functions]]
