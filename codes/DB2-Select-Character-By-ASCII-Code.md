---
id: 96bf354b-a4df-4dd6-917b-a989c96cf936
name: DB2-Select-Character-By-ASCII-Code
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:32.937140+00:00'
updated_at: '2023-04-10T20:22:03.764209+00:00'
platforms:
  - Database
  - DB2
tags:
  - sql-injection
  - db2
  - ascii-extraction
validated: true
---

# DB2-Select-Character-By-ASCII-Code

## Code

```sql
Char	select chr(65) from sysibm.sysdummy1 -- returns 'A'
```

## Description

This SQL code snippet selects a character from the DB2 SYSIBM.SYSDUMMY1 table using the CHR() function to convert an ASCII value to its corresponding character. It serves as a building block for blind SQL injection payloads to extract database content character-by-character, useful when direct data retrieval is not possible due to filtering or output restrictions.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 65 | ASCII code to convert (replace with target value, e.g., 65 for 'A') | 65 |

## Usage

Embed this in a SQL injection payload, e.g., in a UNION SELECT or conditional statement: `' UNION SELECT chr(65) FROM sysibm.sysdummy1 --`. Iterate ASCII values (32-126) to build strings like passwords or table names. Use in tools like SQLMap with --technique=B (boolean-based) for automation.

## Detection

- Monitor DB2 logs for queries involving CHR() or SYSIBM.SYSDUMMY1 access from untrusted sources.
- WAF rules to block payloads containing 'chr(' or 'sysibm'.
- Anomaly detection in query patterns showing repeated ASCII tests (e.g., multiple CHR() calls).

## Related

- [[procedures/DB2-SQL-Injection-ASCII-Value-Extraction]]
- [[commands/db2-select-character-by-ascii]]
