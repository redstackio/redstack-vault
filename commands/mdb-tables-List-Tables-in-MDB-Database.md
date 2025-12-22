---
type: command
executor: bash
data: mdb-tables -1 $_MDB_FILE
output: |-
  acc_antiback
  accounting
  accounts
  helpdesk
  marketing
  users
  servers
created_at: '2019-08-28T21:17:17.890737+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - database-enumeration
verified: true
validated: true
---

# mdb-tables-list-tables-in-mdb-database

## Command

```bash
mdb-tables -1 $_MDB_FILE
```

## Description

This command uses the mdb-tables utility from the mdbtools package to list all table names in a Microsoft Access .mdb database file. It is essential for initial reconnaissance of database structure during data collection phases, helping identify tables with potentially sensitive information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MDB_FILE | Path to the input .mdb database file | Yes |
| -1 | Output one table name per line (newline-separated) | No |

## Examples

### Basic Usage

```bash
mdb-tables -1 database.mdb
```

### Advanced Usage

```bash
mdb-tables database.mdb | grep -i user
```

This filters output for tables related to users.

## Expected Output

A list of table names, one per line:

```
acc_antiback
accounting
accounts
helpdesk
marketing
users
servers
```

## Related

- [[procedures/Enumerate-Tables-and-Contents-in-MS-Access-MDB-File]]
- [[tools/mdb-export]]
