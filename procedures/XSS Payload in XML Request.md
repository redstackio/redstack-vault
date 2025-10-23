---
id: be471ff8-6c7c-4d5e-9f9b-01abbc9c0af7
name: XSS Payload in XML Request
type: procedure
verified: true
submitted: true
created_at: '2020-09-05T19:47:45.073202+00:00'
updated_at: '2023-05-26T01:14:33.662061+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xss]]'
---

# XSS Payload in XML Request

**Status**: ✓ Verified

## Summary

XSS (cross-site scripting) attack can be performed by executing javascript through user input fields. XSS payload can also be inserted in XML request and it gets executed when the input is reflected in the web response. 

## Description

# Description

XSS (cross-site scripting) attack can be performed by executing javascript through user input fields. XSS payload can also be inserted in XML request and it gets executed when the input is reflected in the web response.



# Procedure



1. Enter the search string in the application





![027ee6a7-3f99-4855-abff-94559684ddc6.png]()



2. Intercept the request using Burp







![7b2ebefb-d86c-4f54-9fee-fa66849d2b74.png]()



3. Modify the search string and replace with the XSS payload *%3E%3Cscript%3Ealert(‚123‛)%3C/script%3E*



![90bdc35b-c738-4750-9f56-1a9f2ff73a93.png]()



4. Observe the response with an alert box as the script is executed





![c3070c0c-bf42-4ab0-a8e0-5b302f716e5d.png]()



## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xss]]


