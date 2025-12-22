---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
type: command
executor: bash
data: mdb-tables $_MDB_FILE
output: |
  users
  credentials
  config
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - database-enumeration
  - reconnaissance
verified: true
validated: true
---

# mdb-tables-list-tables-in-database

## Command

```bash
mdb-tables $_MDB_FILE
```

## Description

This command lists all tables present in a Microsoft Access .mdb database file using the mdb-tables utility from the mdbtools suite. It is useful for initial reconnaissance of database structure to identify potentially sensitive tables containing user data, credentials, or configurations during offline analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MDB_FILE | Path to the input .mdb database file | Yes |

## Examples

### Basic Usage

```bash
mdb-tables database.mdb
```

### Advanced Usage

```bash
mdb-tables -1 database.mdb | grep -i user
```

This filters the output to show only tables related to users.

## Expected Output

A simple list of table names, one per line:

```
users
credentials
config
sessions
```

## Related

- [[commands/mdb-export-export-table-contents]]
- [[procedures/Enumerate-Tables-and-Contents-in-MS-Access-MDB-File]]
- [[tools/mdbtools]]
