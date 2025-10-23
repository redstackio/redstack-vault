---
id: 5137b7c0-55b4-43b6-badb-3004fe95ebbe
name: Web Cache Poisoning via GET Request
type: procedure
verified: true
submitted: true
created_at: '2020-09-06T09:28:04.235350+00:00'
updated_at: '2023-05-26T15:55:00.482110+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[web cache posioning]]'
- '[[xss]]'
---

# Web Cache Poisoning via GET Request

**Status**: ✓ Verified

## Summary

Web cache poisoning can be performed if the requests are cached in the browser. It is possible to perform XSS attacks using cache poisoning via GET method. 

## Description

# Description

Web cache poisoning can be performed if the requests are cached in the browser. It is possible to perform XSS attacks using cache poisoning via GET method.



# Procedure



1. Access the application as shown below.



![9b38f0ef-1956-469d-b8d7-c1959f394201.png]()





2. Intercept the request and in HTTP History, right-click on *geolocate.js* request and send it to repeater.





![6e840e04-6b37-480e-8c9f-81fc2e49cab3.png]()



3. In the repeater, observe the request to *geolocate.js* with *callback* value as *setCountryCookie* in URL and an additional *callback* value is set to *myfunction *in the body.





![2095e754-e2f9-4975-9c8b-fdd7b3854e2e.png]()



4. Send the request again to see the cache hit in the response.





![b6d38d86-4810-44fb-9a77-af37f1274028.png]()



5. Send the request in the repeater with callback value set to *myfunction* in the body and observe the *myfunction* in the response.



![9ebbe08e-6013-4af2-83f1-b86541e0ffaf.png]()



6. Now, try with the *callback* value as *alert(1)* which is XSS payload.



![d34844b6-3f44-4997-bf64-3913a5e7f021.png]()



7. Resend the request in the repeater and observe the payload alert(1) in the response which gets executed in the browser showing an alert box.



![187949df-451c-4384-9048-d98eac9359d3.png]()











## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[web cache posioning]]
- [[xss]]


