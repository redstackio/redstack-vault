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

2. Intercept the request and in HTTP History, right-click on *geolocate.js* request and send it to repeater.

3. In the repeater, observe the request to *geolocate.js* with *callback* value as *setCountryCookie* in URL and an additional *callback* value is set to *myfunction *in the body.

4. Send the request again to see the cache hit in the response.

5. Send the request in the repeater with callback value set to *myfunction* in the body and observe the *myfunction* in the response.

6. Now, try with the *callback* value as *alert(1)* which is XSS payload.

7. Resend the request in the repeater and observe the payload alert(1) in the response which gets executed in the browser showing an alert box.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[web cache posioning]]
- [[xss]]
