---
id: 5365a6d0-3423-4ce0-a7f9-0422588ba46d
name: Reflected XSS Into a JavaScript String With Angle Brackets HTML Encoded
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T12:10:12.564535+00:00'
updated_at: '2023-05-26T18:23:26.725060+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# Reflected XSS Into a JavaScript String With Angle Brackets HTML Encoded

**Status**: ✓ Verified

## Summary

In Some application's search functionality , the searh term gets reflected inside the JavaSript string. In order for an attacker to execute the JS code ,the code needs to be escaped from the JavaSrcipt string. 

## Description

# Description

In Some application's search functionality , the searh term gets reflected inside the JavaSript string. In order for an attacker to execute the JS code ,the code needs to be escaped from the JavaSrcipt string.

# Instructions

1. Navigate to the search box and enter random alpha numeric string.

2.Observe that the random string has been reflected inside a JavaScript string 

3.Use the below payload to check how the response. Observe that the  payload is not breaking the JavaScript.

4. Since the payload from above step didnt escape the javascript string , try with the following payload:

*`'-alert(1)-*'`

5. Observe a alert popup triggered by the payload.

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]
