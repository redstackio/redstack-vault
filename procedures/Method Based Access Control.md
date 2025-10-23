---
id: 777fda65-727e-4bd2-ac87-848ddc1972d5
name: Method Based Access Control
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T19:19:59.458475+00:00'
updated_at: '2023-05-26T18:49:48.483999+00:00'
platforms:
- Web
tags:
- '[[access control]]'
- '[[Web Applications]]'
---

# Method Based Access Control

**Status**: ✓ Verified

## Summary

Few applications allow alternate HTTP request methods.An attacker can modify the HTTP methods to perform actions on resticted urls 

## Description

# Description

Few applications allow alternate HTTP request methods.An attacker can modify the HTTP methods to perform actions on resticted urls



# Instructions



1. Log in to the application using admin credentials





![c0a1a12a-f3d9-4030-b8e3-e0c4ac09e6f8.png]()





2.Navigate to admin panel and upgrade user carlos and intercept the request





![0e80c903-605d-4046-89c7-6106d4a7fd31.png]()



3. Observe that the account has been upgraded to admin account 





![d6299145-2b10-4d7c-b794-e1240ff900ab.png]()







![375d7763-5482-4978-8e09-b0d972b2f7bf.png]()



4.Open incognito window and login with non-admin credentials and intercept the request 





![8f499d05-b61c-4e94-ace1-5d8e8aa73523.png]()

5. Attempt to repromote the carlos with the non admin user by copying that user's session cookie into the existing Burp Repeater request, and observe th at the response says "Unauthorized ". 



![28538923-681e-4742-8436-44c6b8139ff9.png]()



6. Change the method from `POST` to `POSTX` and observe that the response changes to "missing parameter". Convert the request to use the `GET` method by right-clicking and selecting "Change request method". 



![6db1d4ff-c196-4570-91b7-079f0fcd62a0.png]()



7.Change the username parameter to weiner username and resend the request.



![8d2e9174-255a-4e21-85e4-23fc3da58b1e.png]()



8.Observe that the request has been accpeted by the server.

## Platforms

- Web

## Tags

- [[access control]]
- [[Web Applications]]


