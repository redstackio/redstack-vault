---
id: c4c8512c-9634-400c-ac08-fa126ac48006
name: HTTP Request Smuggling CL TE
type: procedure
verified: true
submitted: true
created_at: '2020-08-11T17:14:00.296169+00:00'
updated_at: '2023-05-26T01:06:44.183021+00:00'
platforms:
- Web
tags:
- '[[http request smuggling]]'
- '[[Web Applications]]'
---

# HTTP Request Smuggling CL TE

**Status**: ✓ Verified

## Summary

In CL TE HTTP Request smuggling attack, the front end server uses the content Lenght(CL) header and backe end server uses Transfer-Encoding header while parsing the request. 

## Description

# Description

In CL TE HTTP Request smuggling attack, the front end server uses the content Lenght(CL) header and backe end server uses Transfer-Encoding header while parsing the request.



# Instructions



1.Turn on the *intercept *under *proxy *tab in Burp Suite tool to intercept the request as shown .





![afce7a76-24d2-4141-b518-b1852f5de60c.jpg](_assets/images/Mash/afce7a76-24d2-4141-b518-b1852f5de60c.jpg)







2. Right click on the intercepted request and click on *send to repeater* to send the request to *repeater tab*.









![0d97b95a-4aed-4c2f-bb81-96795bed6ed8.jpg](_assets/images/Mash/0d97b95a-4aed-4c2f-bb81-96795bed6ed8.jpg)





3. Change the request in repeater tab to the following .







**Code**: [[POST / HTTP/1.1
Host: your-lab-id.web-security-ac]]









4. After replacing the request in step2 to step3, send the request to the server couple of times. Observe the response for the request. The request is getting parsed by the server and the last letter in the request is appended to the next request and is being displayed as *Unrecognized method GPOST.*





![8e53013f-4541-4478-ae74-79bc1141f8d9.png](_assets/images/Mash/8e53013f-4541-4478-ae74-79bc1141f8d9.png)



## Platforms

- Web

## Tags

- [[http request smuggling]]
- [[Web Applications]]


