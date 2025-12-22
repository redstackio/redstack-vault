---
type: code
language: SQL
verified: true
tags:
  - sql-injection
  - bypass
  - payload
platforms:
  - Web
validated: true
---

# SQL-Union-Select-Admin-Bypass-Payload

## Code

```sql
admin' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055'
```

## Description

This SQL code snippet is a UNION-based injection payload designed to bypass authentication in vulnerable web login forms. It closes the original query with a single quote and false condition (AND 1=0), then appends a SELECT statement that returns hardcoded administrator credentials: username 'admin' and MD5 hash '81dc9bdb52d04dc20036dbd8313ed055' (corresponding to plaintext password '1234'). When injected into the username parameter, it tricks the application into validating the fabricated admin row as a successful login.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The payload is static; the hash is fixed for password '1234'. Customize the username or hash if known target details differ. | N/A |

## Usage

Inject this payload into the username field of a login form via manual tampering, Burp Suite Repeater, or tools like curl. For example, in a POST request: username=admin' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055'. It assumes a two-column query (username, password_hash) and MySQL-compatible syntax. Test on vulnerable apps like DVWA or custom forms.

## Detection

- Web application logs showing UNION SELECT keywords or anomalous query structures.
- Database error logs with syntax issues from the single quote or UNION.
- Intrusion detection systems (IDS) alerting on SQLi signatures in HTTP payloads.
- Unusual successful logins with admin privileges from untrusted IPs.

## Related

- [[procedures/Routed-Injection-Admin-Login-Bypass]]
- [[curl-post-sql-injection-payload]]
