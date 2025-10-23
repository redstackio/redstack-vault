---
id: c2b76110-bd9e-4d96-a7b3-805a6131f081
name: 'Reflected XSS Protected By CSP - Bypass CSP '
type: procedure
verified: true
submitted: true
created_at: '2020-08-23T18:30:15.550627+00:00'
updated_at: '2023-05-26T18:37:11.340921+00:00'
platforms:
- Web
tags:
- '[[bypass CSP]]'
- '[[CSP]]'
- '[[injection]]'
- '[[owasp top 10]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# Reflected XSS Protected By CSP - Bypass CSP 

**Status**: ✓ Verified

## Summary

Description CSP(COntent Security Policy is a standard policy introduced to prevent XSS attacks. CSP is enabled by configuring the application server to return CSP header in the response. An attcker can  bypass in secure CSP configuration to deliver XSS attacks and steal sensitive information. Instr

## Description

Description

CSP(COntent Security Policy is a standard policy introduced to prevent XSS attacks. CSP is enabled by configuring the application server to return CSP header in the response. An attcker can  bypass in secure CSP configuration to deliver XSS attacks and steal sensitive information.



Instructions







1. Enter the paylaod ***<imgsrc=1 onerror=alert(1*)> in the search box of the applciation as shown**



![f0ba3a3d-aedf-47d3-9014-5b48fcea2dd2.png]()





2. Intercept the request using burp suite proxy tab. Send the request with payload to the server.





![6814e324-274d-4454-9c73-d4781cfa59af.png]()







3. Observe that the paylaod gets reflected but CSP prevents the payload from executing.







![90a4b303-5275-4867-bc10-f7d75648a8f0.png]()



4. Observe the response from the request in step 2. CSP header can be seen in the response headers.







![50257bac-6d92-48c3-b797-9538b7713a00.png]()







5.To bypass CSP header , craft the malicious url in the following way and load the url in the browser.

[***https://your-lab-id.web-security-academy.net/?search=%3Cscript%3Ealert%281%29%3C%2Fscript%3E&token=;script-src-elem%20%27unsafe-inline](https://your-lab-id.web-security-academy.net/?search=%3Cscript%3Ealert%281%29%3C%2Fscript%3E&token=;script-src-elem%20%27unsafe-inline%27)%*27**



![38dd28f3-84be-4257-8429-992168e13a00.png]()







6. The url in the step 5 uses **script-src-elem** directive in CSP .  Using this directive, you can overwrite existing **script-src** rules enabling you to inject **unsafe-inline**, which allows you to use inline scripts.







![2ebbfbf0-9e7c-473b-a645-2d34c9d1856b.png]()



## Platforms

- Web

## Tags

- [[bypass CSP]]
- [[CSP]]
- [[injection]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]


