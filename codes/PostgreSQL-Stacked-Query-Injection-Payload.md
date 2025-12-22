---
id: 91bb8c67-93d5-4fa5-a179-3058e0c6a01b
name: PostgreSQL-Stacked-Query-Injection-Payload
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:35.909233+00:00'
updated_at: '2023-04-10T20:23:14.082549+00:00'
platforms:
  - PostgreSQL
tags:
  - sqli-payload
  - stacked-query
  - database-injection
validated: true
---

# PostgreSQL-Stacked-Query-Injection-Payload

## Code

```sql
http://host/vuln.php?id=injection';create table NotSoSecure (data varchar(200));--
```

## Description

This SQL injection payload targets a vulnerable URL parameter in a web application connected to PostgreSQL. It terminates the original query with a quote and semicolon, then stacks a CREATE TABLE statement to inject a new table named 'NotSoSecure' with a varchar column for data storage. The trailing -- comments out any subsequent SQL, preventing errors. Used in stacked query attacks to demonstrate arbitrary DDL execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| host | The target web application hostname | target.com |
| vuln.php | The vulnerable endpoint script | vuln.php |
| injection | Placeholder for legitimate input to close the query (adjust based on app) | 1 |

## Usage

Embed this payload in an HTTP GET request to the vulnerable parameter (e.g., via curl or browser). It's delivered as part of a URL query string during SQL injection testing. After execution, verify by attempting to insert data into the new table or querying it directly if DB access is available. Commonly used in procedures like [[procedures/PostgreSQL-Stacked-Query-Injection]] for initial exploitation.

## Detection

- Web application logs showing multiple SQL statements in a single request or anomalous CREATE/INSERT operations.
- Database audit logs capturing semicolon-separated queries from untrusted sources.
- WAF alerts for SQL keywords like 'CREATE TABLE' in input parameters.
- Unexpected tables or data in the database schema.

## Related

- [[procedures/PostgreSQL-Stacked-Query-Injection]]
- [[curl-send-stacked-sqli-payload]]
