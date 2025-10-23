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





![fe292b17-f6d8-4cd2-9b8a-81d7065164b7.png]()



2.Modify the reqeust in the burp repeater from step 1 . Add the x-forwarded - host header and a cache buster query parameter and send the request to the server. Observe that there is no change in the response from the server.



*x-forwarded-host:  Example.com*









![c48d5a59-69ac-41ea-bc8f-d419919ea34a.png]()







3.Remove the X-Forwarded-Host header and add the X-Forwarded-Scheme header from the request in repeater tab from step 2. Observe that the response  if value included other than HTTPS,  a 302 response can be observed. The Location header shows that request is being redirected to the same URL as requested, but using https://





![0443deeb-fde1-4729-913f-66b33c7e3534.png]()







4.Add both *x-forwarded-host : example.com* and x-forwarded-scheme : nohttps  and send the request to the server . Observe that the location header of 302 response now redirects to *https://example.com*





![96259dbb-bb0d-4857-a314-b001b8315318.png]()







5. Modiofy the cache buster in the url to response: /resources/js/tracking.js







![aab1da47-51a8-4de4-b2c3-8b349ed6f1a6.png]()





6. Craft a malicous url with document.cookie in the body and save the exploit.







![7638e59d-d870-4608-b3ac-47d028dd25b4.png]()





7.Modify the x-forwarded-host as shown below.





![99bd4fa5-3617-4203-838f-8076b596f1a2.png]()





8., right-click on the request in Burp, select "Copy URL", and load this URL in the browser. A succesfull cache poisoning will show the document.cookie in the browser.







![2a6ca2dc-93bb-4250-8e02-72455d96f7ba.png]()





9. Send the request to the server until the cache is posioned and is accesed by the victim.







![b46d5b00-ff4d-4c0a-8af3-f5fcc8128417.png]()





## Platforms

- Web

## Tags

- [[Web Applications]]
- [[web cache posioning]]


