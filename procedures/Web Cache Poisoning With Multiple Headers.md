---
id: 732a2943-19ca-4cc2-bdbe-b3423d325fcf
name: Web Cache Poisoning With Multiple Headers
type: procedure
verified: true
submitted: true
created_at: '2020-08-18T17:15:11.032583+00:00'
updated_at: '2023-05-26T01:23:11.819571+00:00'
platforms:
- Web
tags:
- '[[Web Applications]]'
- '[[web cache posioning]]'
---

# Web Cache Poisoning With Multiple Headers

**Status**: ✓ Verified

## Summary

An attacker will epxloit the cache posioning by adding multiple headers to the request . 

## Description

# Description

An attacker will epxloit the cache posioning by adding multiple headers to the request .

# Instructions

1. with the burp intercept off , browse the application and observe that the* http history* tab logs all the requests and responses. Find the GET request for the JavaScript file /resources/js/tracking.js and send it to Burp Repeater by right clicking on the request.

2.Modify the reqeust in the burp repeater from step 1 . Add the x-forwarded - host header and a cache buster query parameter and send the request to the server. Observe that there is no change in the response from the server.

*x-forwarded-host:  Example.com*

3.Remove the X-Forwarded-Host header and add the X-Forwarded-Scheme header from the request in repeater tab from step 2. Observe that the response  if value included other than HTTPS,  a 302 response can be observed. The Location header shows that request is being redirected to the same URL as requested, but using https://

4.Add both *x-forwarded-host : example.com* and x-forwarded-scheme : nohttps  and send the request to the server . Observe that the location header of 302 response now redirects to *https://example.com*

5. Modiofy the cache buster in the url to response: /resources/js/tracking.js

6. Craft a malicous url with document.cookie in the body and save the exploit.

7.Modify the x-forwarded-host as shown below.

8., right-click on the request in Burp, select "Copy URL", and load this URL in the browser. A succesfull cache poisoning will show the document.cookie in the browser.

9. Send the request to the server until the cache is posioned and is accesed by the victim.

## Platforms

- Web

## Tags

- [[Web Applications]]
- [[web cache posioning]]
