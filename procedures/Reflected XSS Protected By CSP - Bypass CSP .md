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

2. Intercept the request using burp suite proxy tab. Send the request with payload to the server.

3. Observe that the paylaod gets reflected but CSP prevents the payload from executing.

4. Observe the response from the request in step 2. CSP header can be seen in the response headers.

5.To bypass CSP header , craft the malicious url in the following way and load the url in the browser.

[***https://your-lab-id.web-security-academy.net/?search=%3Cscript%3Ealert%281%29%3C%2Fscript%3E&token=;script-src-elem%20%27unsafe-inline](https://your-lab-id.web-security-academy.net/?search=%3Cscript%3Ealert%281%29%3C%2Fscript%3E&token=;script-src-elem%20%27unsafe-inline%27)%*27**

6. The url in the step 5 uses **script-src-elem** directive in CSP .  Using this directive, you can overwrite existing **script-src** rules enabling you to inject **unsafe-inline**, which allows you to use inline scripts.

## Platforms

- Web

## Tags

- [[bypass CSP]]
- [[CSP]]
- [[injection]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]
