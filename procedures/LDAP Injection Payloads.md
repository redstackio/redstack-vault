---
id: 57b9760b-b5e7-44be-b1d1-864c1e1996ca
name: LDAP Injection Payloads
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:01.607030+00:00'
updated_at: '2023-04-10T20:36:28.407087+00:00'
tags:
- '[[LDAP Injection]]'
- '[[Payloads]]'
---

# LDAP Injection Payloads

## Summary

LDAP Injection is a type of injection attack that allows an attacker to modify LDAP queries used by an application to authenticate users. This can allow the attacker to bypass authentication or elevate privileges. The payloads provided in this command can be used to test for LDAP injection vulnerab

## Description

# Description

LDAP Injection is a type of injection attack that allows an attacker to modify LDAP queries used by an application to authenticate users. This can allow the attacker to bypass authentication or elevate privileges. The payloads provided in this command can be used to test for LDAP injection vulnerabilities in an application. An attacker can use these payloads to modify the LDAP query to perform malicious actions such as authenticating as an administrative user, retrieving sensitive information, or modifying data within the LDAP directory.

 

## Requirements

1. Access to the application with authentication credentials

1. Knowledge of the LDAP query structure used by the application

 

## Defense

1. Input validation and sanitization can help prevent LDAP injection attacks

1. Using parameterized queries or prepared statements can help prevent LDAP injection attacks

1. Limiting access to the LDAP directory can help mitigate the impact of a successful LDAP injection attack

 

## Objectives

1. Test for LDAP injection vulnerabilities in an application

1. Bypass authentication or elevate privileges

 

# Instructions

1. 1. Try each payload against the application's authentication mechanism.
2. Observe any changes in behavior or error messages that indicate a successful injection attack.
3. Modify the payloads as needed to bypass authentication or elevate privileges.

 



**Code**: [[*
*)(&
*))%00
)(cn=))\x00
*()|%26'
*()|&'
*(|(mail]]



> Each payload in the command represents a different LDAP injection attack that can be used to test for vulnerabilities in an application. The payloads include various characters and symbols that can modify the LDAP query used for authentication. For example, the payload 'admin*((|userpassword=*)' can be used to authenticate as an administrative user by modifying the LDAP query to return all users with a non-empty userpassword attribute.

## Tags

- [[LDAP Injection]]
- [[Payloads]]


