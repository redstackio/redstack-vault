---
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:33.284527+00:00'
updated_at: '2023-04-10T20:22:26.625356+00:00'
tags:
  - hql-injection
  - error-based
  - payload
platforms:
  - Web
  - Java
validated: true
---

# HQL-Error-Inducing-Payload-for-Column-Enumeration

## Code

```sql
from BlogPosts
where title like '%'
  and DOESNT_EXIST=1 and ''='%' -- 
  and published = true
```

## Description

This HQL payload is designed to inject into a vulnerable query parameter to reference a non-existent column (DOESNT_EXIST), triggering a Hibernate SQLGrammarException. The error response leaks the full underlying SQL SELECT statement, revealing all column names from the target table (e.g., BlogPosts). The trailing comment (--) neutralizes the rest of the original query to avoid syntax issues.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| % | Wildcard placeholder for the search term; replace with actual input if needed | '%' |
| DOESNT_EXIST | Invalid column name to induce error; can be any non-existent identifier | 'FAKE_COLUMN' |
| BlogPosts | Target entity/table name; adjust based on known schema | 'Users' |
| published | Existing condition; modify to match the application's query | 'active' |

## Usage

Inject this payload into a user-controlled HQL parameter, such as a search field in a web form (e.g., title= ' + payload). Use a proxy like Burp Suite to modify POST/GET requests. This is typically the second step in HQL injection after confirming vulnerability with a single quote test. Once columns are leaked, proceed to data extraction via union or blind techniques.

## Detection

- Application logs showing SQLGrammarException or unhandled Hibernate errors.
- WAF alerts for injection patterns like '--' comments or invalid column references in queries.
- Increased error rates in database access logs with malformed HQL.
- Monitor for anomalous search queries with wildcards and logical operators.

## Related

- [[procedures/HQL-Error-Based-Column-Enumeration]]
