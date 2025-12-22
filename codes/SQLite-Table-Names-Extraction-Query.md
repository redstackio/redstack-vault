---
type: code
language: SQL
verified: true
tags:
  - sqlite
  - sql-injection
  - database-enumeration
platforms:
  - Web
validated: true
---

# SQLite-Table-Names-Extraction-Query

## Code

```sql
SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'
```

## Description

This SQL query retrieves the names of all user-created tables in an SQLite database by querying the sqlite_master metadata table. It filters for tables of type 'table' and excludes SQLite system tables (those starting with 'sqlite_') to focus on application-specific schema elements. The query is designed for use in SQL injection payloads, particularly UNION SELECT statements, to leak database structure during reconnaissance.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | This is a static query with no user-defined variables; adapt by wrapping in UNION SELECT for injection. | N/A |

## Usage

Embed this query in a UNION-based SQL injection payload to extract table names from a vulnerable SQLite-backed application. For example, in a string parameter: ' UNION SELECT tbl_name FROM sqlite_master WHERE type='table' AND tbl_name NOT LIKE 'sqlite_%' --. Use tools like Burp Suite to inject and observe leaked names in responses. This is a key step in database enumeration for identifying sensitive tables like 'users' or 'sessions' before attempting data exfiltration.

## Detection

- Monitor application and database logs for queries accessing sqlite_master or using UNION SELECT, which are unusual for normal operations.
- Web application firewalls can signature-match keywords like 'sqlite_master' or 'tbl_name' in input parameters.
- Enable SQLite query logging with PRAGMA journal_mode=WAL and review for anomalous SELECT patterns.
- Behavioral detection: Sudden increases in metadata queries or errors from mismatched column counts in UNION attempts.

## Related

- [[procedures/SQLite-Table-Name-Extraction-via-Integer-String-Injection]]
