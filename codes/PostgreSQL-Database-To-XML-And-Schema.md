---
id: b2d2be0c-b971-45cc-bd71-d3a93c998fe7
name: PostgreSQL-Database-To-XML-And-Schema
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.763789+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Databases
tags:
  - exfiltration
  - postgresql
validated: true
---

# PostgreSQL-Database-To-XML-And-Schema

## Code

```sql
select database_to_xml(true,true,''); -- dump the current database to XML
select database_to_xmlschema(true,true,''); -- dump the current db to an XML schema
```

## Description

These SQL snippets utilize PostgreSQL functions to export the full database content (data + schema) or just the schema to XML format, enabling complete structural and data exfiltration for offline analysis.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| true | Include schema details in output | true |
| true | Include column names/types | true |
| '' | Output filename (empty for stdout) | 'full_dump.xml' |

## Usage

Execute in a compromised database session or via injection to generate XML dumps. The first line captures all data; the second focuses on structure. Parse the XML externally to reconstruct the database.

## Detection

- Log analysis for database_to_xml or database_to_xmlschema calls, especially with schema inclusion flags.
- Volume-based alerts on large XML responses from database queries.
- Integrate with database activity monitoring (DAM) tools to block schema exports.

## Related

- [[procedures/PostgreSQL-XML-Data-Exfiltration]]
- [[commands/postgresql-database-to-xml]]
