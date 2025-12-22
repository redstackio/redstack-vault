---
type: code
language: SQL
verified: true
tags:
  - sqli
  - payload
  - boolean-based
  - sqlite
platforms:
  - Web
validated: true
---

# SQLite-Count-Tables-Boolean-Payload

## Code

```sql
and (SELECT count(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' ) < number_of_table
```

## Description

This SQL snippet is a boolean-based injection payload for SQLite databases. It queries the sqlite_master system table to count user-defined tables (excluding SQLite internal tables starting with 'sqlite_') and compares the count to a threshold value ('number_of_table'). When injected into a vulnerable query, it forces a conditional response based on whether the table count is less than the threshold, enabling blind enumeration of the database schema.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| number_of_table | Integer threshold for comparing the table count (used in binary search to find exact count) | 100 |

## Usage

Inject this payload into a vulnerable web application parameter, such as a login field or search query, typically appended after an OR condition: e.g., username=' OR [payload] --. Use in conjunction with tools like curl or Burp Suite to send requests and observe boolean outcomes (true if count < threshold, false otherwise). Perform binary search by varying the threshold to determine the precise number of tables, which aids in further attacks like table name enumeration.

## Detection

- Web application logs showing malformed SQL queries with 'sqlite_master' or count aggregations.
- Intrusion detection systems (IDS) alerting on SQL injection patterns like 'AND (SELECT' or unusual parameter lengths.
- Database query logs revealing repeated threshold comparisons indicating enumeration attempts.
- WAF rules matching boolean payloads or SQLite-specific schema queries.

## Related

- [[procedures/Count-Tables-in-SQLite-Database-via-Boolean-Injection]]
- [[tools/sqlmap]]
