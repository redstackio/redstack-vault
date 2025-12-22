---
id: 91208c00-1036-46b5-b4f2-bf10471d6d5b
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:32.504066+00:00'
updated_at: '2023-04-06T03:56:32.507474+00:00'
tags:
  - cassandra-injection
  - auth-bypass
  - payload
platforms:
  - Web
  - Database
validated: true
---

# Cassandra-Auth-Bypass-Query-Payload

## Code

```sql
SELECT * FROM users WHERE user = 'admin'/*' AND pass = '*/and pass>'' ALLOW FILTERING;
```

## Description

This CQL injection payload targets Cassandra authentication queries to bypass password validation. By inserting a comment (/* */) after the username clause, it nullifies the password condition, then adds 'and pass>'' (a tautology due to the invalid comparison) to ensure the query returns true. The ALLOW FILTERING directive handles Cassandra's query restrictions, allowing the bypass to succeed and retrieve admin user data.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| admin | Target username for impersonation | admin |
| users | Assumed table name storing user credentials | users |

## Usage

Inject this payload into a vulnerable query parameter or login endpoint that constructs CQL dynamically. It can be delivered via manipulated POST requests to the login form. Use this in scenarios where direct query execution is possible post-initial injection or in custom Cassandra web apps.

## Detection

- Anomalous CQL queries in Cassandra logs containing comments or tautological conditions like 'pass>''.
- Query execution with ALLOW FILTERING on authentication tables, which is unusual.
- Access logs showing admin queries from unauthenticated or suspicious IPs.
- Intrusion detection signatures for SQLi in NoSQL contexts, focusing on comment injection.

## Related

- [[procedures/Cassandra-Login-Bypass-via-SQL-Injection]]
