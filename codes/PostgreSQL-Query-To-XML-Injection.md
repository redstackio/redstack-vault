---
id: 4702f705-78f2-40af-b18a-162d3db8de4b
type: code
language: sql-postgresql
verified: true
created_at: '2023-04-06T03:56:33.369937+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Database
  - PostgreSQL
tags:
  - sql-injection
  - dbms-magic-functions
  - hql-injection
validated: true
---

# PostgreSQL-Query-To-XML-Injection

## Code

```sql
query_to_xml(&#39;Arbitrary SQL&#39;)
```

## Description

This PostgreSQL-specific function executes an arbitrary SQL query provided as its argument and converts the result set into an XML document. In the context of HQL injection, it bypasses query abstractions to run unauthorized SQL, enabling data exfiltration or system interrogation via XML output.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| &#39;Arbitrary SQL&#39; | The SQL query to execute (replace with actual payload like SELECT * FROM users) | &#39;SELECT version()&#39; |

## Usage

Inject this into vulnerable HQL parameters in web app inputs (e.g., search queries). Use in blind or union-based injections where XML parsing reveals results. Chain with xpath for extraction in subsequent steps.

## Detection

- Monitor database logs for query_to_xml calls with user-controlled inputs.
- Alert on unexpected XML generation or anomalous query patterns in application logs.
- WAF rules for PostgreSQL function names in payloads.

## Related

- [[procedures/DBMS-Magic-Functions-Injection]]
