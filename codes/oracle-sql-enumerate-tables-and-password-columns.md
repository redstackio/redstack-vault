---
id: d32f2545-9810-492e-92a4-283b1e7727d7
name: oracle-sql-enumerate-tables-and-password-columns
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.238211+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Oracle Database
tags:
  - database-discovery
  - sql-injection
validated: true
---

# oracle-sql-enumerate-tables-and-password-columns

## Code

```sql
SELECT table_name FROM all_tables;
SELECT owner, table_name FROM all_tables;
SELECT owner, table_name FROM all_tab_columns WHERE column_name LIKE '%PASS%';
```

## Description

This SQL code snippet combines three queries to enumerate Oracle database tables and identify potential password columns. It first lists all tables, then tables with owners, and finally tables containing columns with 'PASS' in the name. Use this in SQL injection scenarios to systematically map schema and target sensitive data without modifying the database.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| '%PASS%' | Wildcard pattern for filtering column names | '%PASSWORD%' |

## Usage

Inject the queries sequentially into a vulnerable endpoint using tools like sqlmap or manual payloads (e.g., via Burp Suite). For blind SQLi, wrap in conditional statements to extract results bit by bit. This code is typically used during the discovery phase after confirming SQLi, chaining into data extraction from identified tables.

## Detection

- Monitor database logs for queries accessing ALL_TABLES or ALL_TAB_COLUMNS from application users.
- Alert on LIKE patterns involving '%PASS%' or schema enumeration keywords.
- Web application firewall (WAF) rules for UNION SELECT involving system views.
- Anomalous query volumes from single IPs.

## Related

- [[procedures/Oracle-SQL-List-Tables-and-Columns]]
- [[tools/sqlmap]]
