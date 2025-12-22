---
type: code
language: text
verified: true
platforms:
  - Web
tags:
  - ldap-injection
  - payload
validated: true
---

# LDAP-Injection-Universal-Payload

## Code

```text
*)(ATTRIBUTE_HERE=*
```

## Description

This payload is a string fragment designed for injection into user-supplied inputs in LDAP queries. It closes the original filter with `*)` and opens a new universal match for the specified attribute (e.g., `uid=*`), causing the query to return all directory entries containing that attribute. Replace `ATTRIBUTE_HERE` with a valid LDAP attribute to target specific data.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ATTRIBUTE_HERE | The LDAP attribute to match against (e.g., uid, userPassword, mail) | uid |

## Usage

Inject this payload into vulnerable fields like username in a login form: `test` + payload (e.g., `test*)(uid=*`). Submit via POST request. Use in web applications querying LDAP for authentication or searches. Combine with a proxy to iterate over attributes from [[commands/list-common-ldap-attributes]].

## Detection

- Log LDAP queries for patterns containing unbalanced parentheses, wildcards (*) in unexpected positions, or multiple filters.
- Application logs showing excessive directory results or authentication bypasses.
- Network traffic analysis for anomalous LDAP binds (port 389/636) with broad filters.

## Related

- [[procedures/LDAP-Injection-with-Default-Attributes]]
