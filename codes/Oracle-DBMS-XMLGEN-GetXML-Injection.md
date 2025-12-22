---
id: 2c8cde83-f353-45bd-bfb0-f11467cb01a0
type: code
language: sql-oracle
verified: true
created_at: '2023-04-06T03:56:33.370007+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Database
  - Oracle
tags:
  - sql-injection
  - dbms-magic-functions
  - hql-injection
validated: true
---

# Oracle-DBMS-XMLGEN-GetXML-Injection

## Code

```sql
DBMS_XMLGEN.getxml(&#39;SQL&#39;)
```

## Description

This Oracle built-in function generates an XML document from the result of a provided SQL query. It is exploited in HQL injections to execute arbitrary SQL and format outputs as XML, facilitating data export or conditional testing in restricted environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| &#39;SQL&#39; | The SQL query to execute and convert to XML | &#39;SELECT * FROM sensitive_table&#39; |

## Usage

Embed in HQL-vulnerable inputs to force XML output from arbitrary queries. Useful for data exchange in attacks or chaining with NVL for blind checks. Customize with additional DBMS_XMLGEN options for formatting.

## Detection

- Log analysis for DBMS_XMLGEN calls in user-supplied queries.
- Intrusion detection on XML-formatted responses from database interactions.
- Input sanitization to block XML generation functions.

## Related

- [[procedures/DBMS-Magic-Functions-Injection]]
