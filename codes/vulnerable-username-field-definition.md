---
id: 01bffa83-a316-4b11-a461-3f36c68dbbf7
name: vulnerable-username-field-definition
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.879193+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - MySQL
tags:
  - schema
  - vulnerability
validated: true
---

# vulnerable-username-field-definition

## Code

```sql
`username` varchar(20) not null
```

## Description

This SQL code defines a vulnerable username column in a MySQL table, using varchar(20) without length checks in queries, enabling truncation-based injection attacks where payloads longer than expected are silently truncated.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | Fixed definition; adjust varchar length to simulate vuln (e.g., smaller for easier truncation) | N/A |

## Usage

Use this in database setup for testing environments (e.g., CREATE TABLE users (id INT, `username` varchar(20) not null, password VARCHAR(50));). In attacks, exploit by sending payloads that rely on truncation to alter query logic, as shown in [[procedures/Bypass-Admin-Login-via-MySQL-Injection-and-Truncation]].

## Detection

- Review schema for short varchar fields on user inputs.
- Enable SQL logging to capture truncation warnings (SET sql_mode='STRICT_TRANS_TABLES').
- Use tools like sqlmap to probe for injection points.

## Related

- [[procedures/Bypass-Admin-Login-via-MySQL-Injection-and-Truncation]]
