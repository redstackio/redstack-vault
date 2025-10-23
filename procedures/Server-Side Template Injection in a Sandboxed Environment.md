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





![9bf77550-c9c0-488d-880c-788b87d6d852.png]()



2. Edit one of the product description templates. 





![756f2f8a-538a-4423-975c-93a1cfe2b4b7.png]()



3. Load the JavaDoc for the `Object` class to find methods that should be available on all objects. Confirm that you can execute `${object.getClass()}` using the `product` object.





![abbcb8a5-f3bd-4c36-93e3-fb520a3010ee.png]()





4. Find a sequence of method invocations that grant access to a class with a static method that lets you read a file, such as:



*`${product.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().resolve('/home/carlos/my_password.txt').toURL().openStream().readAllBytes()?join(" ")*}`





![8c2178c3-c5fc-4e03-8b92-0bc1cf7ccc58.png]()



5. The output will contain the contents of the file as decimal ASCII code points.





![30f6d225-eb73-4367-9b5b-bfe0216a5aa7.png]()





## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Server Side Template Injection]]
- [[SSTI]]
- [[Web Applications]]


