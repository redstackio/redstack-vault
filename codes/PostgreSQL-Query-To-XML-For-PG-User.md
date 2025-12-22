---
id: 6784cdf2-4e11-45d9-8057-b3e2b68776e3
name: PostgreSQL-Query-To-XML-For-PG-User
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.763412+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Databases
tags:
  - exfiltration
  - postgresql
validated: true
---

# PostgreSQL-Query-To-XML-For-PG-User

## Code

```sql
select query_to_xml('select * from pg_user',true,true,''); -- returns all the results as a single xml row
```

## Description

This SQL snippet uses PostgreSQL's query_to_xml function to convert the entire pg_user system catalog into a single, indented XML row, facilitating the exfiltration of database user information including privileges and names.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'select * from pg_user' | Subquery targeting system users | 'select usename from pg_user' |
| true | Flag to include column names in XML | true |
| true | Flag for XML indentation/readability | true |
| '' | Root element name for the XML | 'users' |

## Usage

Inject this SQL via a vulnerable parameter in a web application or execute directly in psql. Capture the XML output for parsing; ideal for initial reconnaissance in SQL injection attacks to identify admin users.

## Detection

- Monitor PostgreSQL logs for query_to_xml executions on system catalogs like pg_user.
- Alert on XML-formatted query outputs in application responses.
- Use query auditing tools to flag serialization functions in untrusted inputs.

## Related

- [[procedures/PostgreSQL-XML-Data-Exfiltration]]
- [[commands/postgresql-query-to-xml-pg-user]]
