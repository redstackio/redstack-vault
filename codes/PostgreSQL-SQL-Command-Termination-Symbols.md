---
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.395111+00:00'
updated_at: '2023-04-10T20:23:21.773343+00:00'
platforms:
  - PostgreSQL
tags:
  - sqli
  - injection-symbols
validated: true
---

# PostgreSQL-SQL-Command-Termination-Symbols

## Code

```sql
; #Used to terminate a SQL command. The only place it can be used within a statement is within a string constant or quoted identifier.
|| #or statement 

# usage examples: 
/?whatever=1;(select 1 from pg_sleep(5))
/?whatever=1||(select 1 from pg_sleep(5))
```

## Description

This SQL snippet documents key symbols for terminating commands in PostgreSQL SQL injection attacks. The semicolon (;) ends the original query prematurely, allowing appended malicious code, while the double pipe (||) serves as a string concatenation or logical OR operator to chain payloads or bypass conditions.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| whatever | Vulnerable parameter name in URL or form | q, id, username |
| 1 | Placeholder value to maintain query validity | Any non-malicious input |

## Usage

Embed these symbols in HTTP parameters or POST data during SQL injection testing. For example, append ; followed by a sleep function for blind time-based confirmation, or use || to concatenate a UNION SELECT for data exfiltration. Deliver via tools like curl or sqlmap in web application pentests targeting PostgreSQL.

## Detection

- Scan inputs for unescaped ; or || in web logs or database query traces.
- WAF rules flagging multiple statements or concatenation in user-supplied SQL.
- Anomalous query delays (e.g., pg_sleep) or error logs showing terminated statements.

## Related

- [[procedures/PostgreSQL-SQL-Command-Termination-Injection]]
- [[tools/sqlmap]]
