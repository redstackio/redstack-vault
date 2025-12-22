---
id: c9a31a82-e32a-4b1f-8f63-972a2ed50566
type: code
language: sql-oracle
verified: true
created_at: '2023-04-06T03:56:33.371121+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Database
  - Oracle
tags:
  - sql-injection
  - dbms-magic-functions
  - hql-injection
  - blind-injection
validated: true
---

# Oracle-NVL-Condition-Check-Injection

## Code

```oracle sql
NVL(TO_CHAR(DBMS_XMLGEN.getxml('select 1 where 1337>1')),'1')!='1'
```

## Description

This Oracle expression uses NVL, TO_CHAR, and DBMS_XMLGEN to evaluate a SQL condition boolean-style for blind injection. It returns true/false based on whether the inner query produces output, enabling data extraction without visible results.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 1337>1 | The condition to test (replace for payload, e.g., substring checks) | database_name like &#39;A%&#39; |

## Usage

Inject into HQL for blind SQLi, observing response differences (e.g., errors, lengths) to infer condition truth. Ideal for extracting passwords or flags character-by-character in time-based or boolean-based attacks.

## Detection

- Query logs showing nested DBMS_XMLGEN with conditions.
- Behavioral anomalies in response times or content lengths.
- Advanced logging of NVL/TO_CHAR usage in dynamic queries.

## Related

- [[procedures/DBMS-Magic-Functions-Injection]]
