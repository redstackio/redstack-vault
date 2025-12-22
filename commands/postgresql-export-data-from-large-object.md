---
id: b23a592d-7aff-4dae-af4a-a8294ba281c8
type: command
executor: psql
data: 'SELECT lo_export($_OID, ''$_FILE_PATH'');'
output: null
created_at: '2023-04-06T03:56:35.993589+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - postgresql
  - large-object
  - file-write
verified: true
validated: true
---

# postgresql-export-data-from-large-object

## Command

```sql
SELECT lo_export($_OID, '$_FILE_PATH');
```

## Description

Exports a large object's contents to a server file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_OID | Large object ID | Yes |
| $_FILE_PATH | Export path (e.g., '/tmp/testexport') | Yes |

## Examples

### Basic Usage

```sql
SELECT lo_export(1001, '/tmp/testexport');
```

## Expected Output

1 for successful export.

## Related

- [[procedures/PostgreSQL-File-Write-with-Reverse-Shell-Payload]]
- [[commands/postgresql-create-large-object-with-oid]]
