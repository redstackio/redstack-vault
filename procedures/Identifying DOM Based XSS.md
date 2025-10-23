---
id: 92232eff-af88-4e5c-a0f5-a8e60204e826
name: Identifying DOM Based XSS
type: procedure
verified: true
submitted: true
created_at: '2020-07-28T15:23:15.697101+00:00'
updated_at: '2023-05-26T01:06:17.603794+00:00'
platforms:
- Web
tags:
- '[[DOM XSS]]'
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xss]]'
---

# Identifying DOM Based XSS

**Status**: ✓ Verified

## Summary

DOM (Document Object Model) XSS can be tested in the cases where the user input does not reach the server but gets executed in the browser with the response. 

## Description

# Description

DOM (Document Object Model) XSS can be tested in the cases where the user input does not reach the server but gets executed in the browser with the response.

# Instructions



1. In the below screenshot, *Page 1* value which is after *#* symbol can be modified and added with Javascript.





![696fc0a6-4198-4ff8-98c8-0d96dbca9c25.jpg](_assets/images/Mash/696fc0a6-4198-4ff8-98c8-0d96dbca9c25.jpg)







2. Following payload is added after the # symbol in the URL.



*<script>alert("XSS");</script>*



![c924d20c-4bd3-456f-939c-75cf17878d5f.jpg](_assets/images/Mash/c924d20c-4bd3-456f-939c-75cf17878d5f.jpg)







3. The request is intercepted in Burp to check if the payload is sent to the server. It can be observed that the payload is not part of the GET request.







![312accd7-2bad-477e-a690-c8f8bd51a5ae.jpg](_assets/images/Mash/312accd7-2bad-477e-a690-c8f8bd51a5ae.jpg)





4. Payload gets executed in the browser.





![61c468e2-93a5-4396-8f85-c1f854696a1d.jpg](_assets/images/Mash/61c468e2-93a5-4396-8f85-c1f854696a1d.jpg)





## Platforms

- Web

## Tags

- [[DOM XSS]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xss]]


