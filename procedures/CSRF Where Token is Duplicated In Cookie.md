---
id: eadecda5-082d-4b14-8fd9-2379f9de39a3
name: CSRF Where Token is Duplicated In Cookie
type: procedure
verified: true
submitted: true
created_at: '2020-08-23T17:44:14.740568+00:00'
updated_at: '2023-05-26T15:58:14.233109+00:00'
platforms:
- Web
tags:
- '[[CSRF]]'
- '[[Web Applications]]'
---

# CSRF Where Token is Duplicated In Cookie

**Status**: ✓ Verified

## Summary

Descritpion CSRF token can be implemented inside cookie or inside the body of the request . Few applications use double CSRF token implementation wherein csrf tokens are implemented both in cookies and body. But only one of them gets validated by the server. Instructions 1.With browser proxying req

## Description

# Descritpion

CSRF token can be implemented inside cookie or inside the body of the request . Few applications use double CSRF token implementation wherein csrf tokens are implemented both in cookies and body. But only one of them gets validated by the server. 



# Instructions





1.With browser proxying requests through burp and burp intercept off, log into the application and submit the* change email* form . Identify the submit request under *http history.*







![a466b740-dcc8-49c2-ba28-f59bc0e166c3.png]()





2. Send the request to the repeater tab. Observe that CSRF tokens are implemented in the cookie as well as in the body . Value of the CSRF token in the body parameter is validated by comparing it with CSRF toekn in the cookie.







![f0eea56b-6ecb-4087-b6f0-635718976bf3.png]()





3.Perform a search, send the resulting request to Burp Repeater, and observe that the search term gets reflected in the Set-Cookie header. Since the search function has no CSRF protection, you can use this to inject cookies into the victim user's browser.





![8a789ba0-2176-4793-83b0-b5e2a6eb727b.png]()







4.Craft a URL  to inject a fake csrf cookie into the victim's browser.  Use the CSRF POC generator on this request.



***/?search=test%0d%0aSet-Cookie:%20csrf=fa*ke**









![8f2eac4d-11bb-46f7-b500-d3c3df7e2aa0.png]()





5.Add the following code to inject the cookie and submit the change email form.

***<img src="$cookie-injection-url" onerror="document.forms[0].submit();"*/>**







![a941b434-4539-4a4f-b881-937561f04e16.png]()



## Platforms

- Web

## Tags

- [[CSRF]]
- [[Web Applications]]


