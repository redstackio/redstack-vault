---
id: 3014cb1c-7add-4107-bece-cdd73a9680e0
name: DB2-ASCII-Concatenation-Example
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:33.067078+00:00'
updated_at: '2023-04-10T20:22:01.559841+00:00'
platforms:
  - Database
  - DB2
tags:
  - sql-injection
  - db2
  - ascii
  - bypass
validated: true
---

# DB2-ASCII-Concatenation-Example

## Code

```sql
SELECT chr(65)||chr(68)||chr(82)||chr(73) FROM sysibm.sysdummy1 -- returns “ADRI”. Works without select too
```

## Description

This SQL code snippet for IBM DB2 demonstrates constructing a string ('ADRI') by concatenating characters from their ASCII values using the CHR() function and || operator. It avoids using quotes, making it ideal for SQL injection payloads where quote filters are in place. The sysibm.sysdummy1 table ensures execution on a dummy row.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 65 | ASCII value for 'A' | 65 |
| 68 | ASCII value for 'D' | 68 |
| 82 | ASCII value for 'R' | 82 |
| 73 | ASCII value for 'I' | 73 |

No runtime variables; values are hardcoded but can be replaced with dynamic ASCII numbers in payloads.

## Usage

Embed this pattern in SQL injection payloads, e.g., to form 'OR 1=1': admin' || CHR(79)||CHR(82)||' 1=1 --. Execute via vulnerable web inputs or direct DB2 client. Useful in blind or error-based injections to test/exploit without quotes.

## Detection

- Query logs showing frequent CHR() calls or || with numeric arguments.
- WAF alerts on ASCII patterns in inputs (e.g., sequences like chr(65)).
- Anomalous string constructions in audit trails, indicating obfuscated injection attempts.

## Related

- [[procedures/DB2-SQL-Injection-Using-ASCII-Concatenation]]
- [[commands/db2-concatenate-ascii-values]]
