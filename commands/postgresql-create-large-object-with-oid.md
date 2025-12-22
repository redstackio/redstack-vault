---
id: 3c6af9af-d475-47e4-9494-7a028a3b0a77
type: command
executor: psql
data: 'SELECT lo_from_bytea($_OID, $_BYTEA_DATA);'
output: null
created_at: '2023-04-06T03:56:35.993442+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - postgresql
  - large-object
  - binary
verified: true
validated: true
---

# postgresql-create-large-object-with-oid

## Command

```sql
SELECT lo_from_bytea($_OID, $_BYTEA_DATA);
```

## Description

Creates a PostgreSQL large object from bytea data and returns its OID for further use.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_OID | Object ID (integer) | Yes |
| $_BYTEA_DATA | Binary data as bytea (e.g., decode('payload', 'hex')) | Yes |

## Examples

### Basic Usage

```sql
SELECT lo_from_bytea(1001, 'your file data goes in here'::bytea);
```

## Expected Output

The assigned OID (e.g., 1001).

## Related

- [[procedures/PostgreSQL-File-Write-with-Reverse-Shell-Payload]]
- [[commands/postgresql-export-data-from-large-object]]
