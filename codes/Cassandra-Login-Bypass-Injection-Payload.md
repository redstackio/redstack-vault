---
id: 0b7459eb-cfe4-4142-aa5a-ae794348d512
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:32.477389+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - sql-injection
  - cassandra
  - login-bypass
  - payload
platforms:
  - Database
  - Cassandra
validated: true
---

# Cassandra-Login-Bypass-Injection-Payload

## Code

```sql
username: admin' ALLOW FILTERING; %00
password: ANY
```

## Description

This SQL injection payload is designed to bypass authentication in a vulnerable Cassandra database login interface. It exploits improper input sanitization by injecting code into the username field to execute an unauthorized query that retrieves admin credentials, ignoring the password validation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| admin | Target username for extraction (e.g., admin account) | admin |
| ALLOW FILTERING | Cassandra-specific clause to bypass partition key restrictions | N/A (fixed) |
| %00 | Null byte to terminate the injection and ignore subsequent fields | N/A (fixed) |
| ANY | Wildcard value for password field to avoid validation | N/A (fixed) |

## Usage

Enter the username payload into the login form's username field and 'ANY' into the password field. Submit the form via the web interface or client. This is typically used in penetration testing to demonstrate SQL injection vulnerabilities in database auth systems. Ensure proper authorization before use.

## Detection

- Monitor login logs for anomalous inputs containing quotes, semicolons, or keywords like 'ALLOW FILTERING'.
- Enable SQL query logging in Cassandra to detect injected statements accessing auth tables.
- Use intrusion detection systems (IDS) to flag requests with null bytes (%00) or wildcard passwords.
- Web application scanners like SQLMap can simulate and detect this pattern.

## Related

- [[procedures/Cassandra-Login-Bypass-via-SQL-Injection]]
