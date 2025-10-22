---
id: d49c36a2-6044-4549-97f4-998de41abe81
name: URL Normalisation - XSS
type: procedure
verified: true
submitted: true
created_at: '2020-09-06T08:43:55.549862+00:00'
updated_at: '2023-05-26T18:52:26.216623+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xss]]'
---

# URL Normalisation - XSS

**Status**: ✓ Verified

## Summary

XSS (cross-site scripting) attack is performed by inserting javascript payloads through the user input fields. If the payload is encoded, cache's normalisation process can be used to exploit. 

## Description

# Description

XSS (cross-site scripting) attack is performed by inserting javascript payloads through the user input fields. If the payload is encoded, cache's normalisation process can be used to exploit.

# Procedure

1. Access the application

2. Intercept the request in Burp and in the HTTP history select a request and right-click on send to repeater.

3. In the repeater, send the request to /.

4. Request some random path in the Burp repeater. Observe the response with 404 status code.

5. Append XSS payload *`</p><script>alert(1)</script><p>fo*o `to the random path as shown in the below screenshot.

6. In Burp repeater, poison the cache and load the URL in the browser. The payload gets executed as it gets URL-decoded by the cache. 

7. Observe the alert box as the payload is executed.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xss]]
