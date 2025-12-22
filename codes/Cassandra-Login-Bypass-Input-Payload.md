---
id: 02dd1b51-78ff-4698-bf36-292db5d415f1
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:32.503988+00:00'
updated_at: '2023-04-06T03:56:32.507410+00:00'
tags:
  - cassandra-injection
  - login-bypass
  - payload
platforms:
  - Web
  - Database
validated: true
---

# Cassandra-Login-Bypass-Input-Payload

## Code

```sql
username: admin'/*
password: */and pass>'
```

## Description

This SQL injection payload is designed for bypassing authentication in a Cassandra web login form. It uses multi-line comments (/* */) to truncate the original CQL query after the username, effectively ignoring the password check, and appends a logical condition 'and pass>' that always evaluates to true, allowing login as the 'admin' user without credentials.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| admin | Target username (typically a privileged account) | admin |

## Usage

Enter the username payload into the username field and the password payload into the password field of the login form. Submit via the web interface or an intercepted request using a proxy tool. This is typically used in the initial access phase against vulnerable Cassandra management interfaces.

## Detection

- Web application logs showing login attempts with comment characters (/*, */) or unbalanced quotes.
- Database query logs revealing truncated or modified CQL statements.
- Failed login audits followed immediately by successful admin access without password matches.
- WAF alerts for SQLi patterns in POST parameters.

## Related

- [[procedures/Cassandra-Login-Bypass-via-SQL-Injection]]
