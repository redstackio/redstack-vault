---
id: b327e446-59a1-4168-b646-0c3c54079305
name: Server-Side Template Injection in a Sandboxed Environment
type: procedure
verified: true
submitted: true
created_at: '2020-08-24T06:29:17.696624+00:00'
updated_at: '2023-05-26T18:08:30.709133+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Server Side Template Injection]]'
- '[[SSTI]]'
- '[[Web Applications]]'
---

# Server-Side Template Injection in a Sandboxed Environment

**Status**: ✓ Verified

## Summary

If sandboxing is poorly implemented, it is possible to perform server-side template injection attacks. Sensitive information can be retrieved from the server using SSTI attacks. 

## Description

# Description

If sandboxing is poorly implemented, it is possible to perform server-side template injection attacks. Sensitive information can be retrieved from the server using SSTI attacks.

# Procedure

1. Login into the application

2. Edit one of the product description templates. 

3. Load the JavaDoc for the `Object` class to find methods that should be available on all objects. Confirm that you can execute `${object.getClass()}` using the `product` object.

4. Find a sequence of method invocations that grant access to a class with a static method that lets you read a file, such as:

*`${product.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().resolve('/home/carlos/my_password.txt').toURL().openStream().readAllBytes()?join(" ")*}`

5. The output will contain the contents of the file as decimal ASCII code points.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Server Side Template Injection]]
- [[SSTI]]
- [[Web Applications]]
