---
type: code
language: sql
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - web
tags:
  - payload
  - sql-injection
validated: true
---

# basic-sql-injection-or-payload

## Code

```sql
' or 'SOMETHING
```

## Description

This SQL snippet is a basic injection payload that closes a string literal and appends an OR condition. In the context of raw hash bypass, the binary hash emulates this to make the authentication query always true (e.g., replacing SOMETHING with 1=1).

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| SOMETHING | Tautology or condition | 1=1 |

## Usage

Inject into username or password fields in vulnerable forms. For raw hash attacks, the payload is indirectly delivered via the hash binary output. Use with tools like Burp Suite or curl for testing.

## Detection

- Input validation failures in logs.
- Database errors showing unescaped quotes.
- SIEM alerts on OR 1=1 patterns in queries.

## Related

- [[procedures/SQL-Injection-Authentication-Bypass-Using-Raw-MD5-and-SHA1-Hashes]]
- [[commands/boolean-sql-injection-test]]
