---
id: 40da1d03-afee-4c9a-835f-3009c6a4cbc6
type: command
executor: psql
data: 'SELECT lo_put($_OID, $_OFFSET, $_DATA);'
output: null
created_at: '2023-04-06T03:56:35.993522+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - postgresql
  - large-object
verified: true
validated: true
---

# postgresql-append-data-to-large-object

## Command

```sql
SELECT lo_put($_OID, $_OFFSET, $_DATA);
```

## Description

Appends or writes data to a large object at a specified offset.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_OID | Large object ID | Yes |
| $_OFFSET | Byte offset to write at | Yes |
| $_DATA | Data to append (bytea) | Yes |

## Examples

### Basic Usage

```sql
SELECT lo_put(1001, 0, 'some other data'::bytea);
```

## Expected Output

1 for success.

## Related

- [[procedures/PostgreSQL-File-Write-with-Reverse-Shell-Payload]]
- [[commands/postgresql-create-large-object-with-oid]]
