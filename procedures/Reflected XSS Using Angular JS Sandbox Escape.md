---
id: eeb8e4ff-45db-4769-b2c6-3cae7221a210
name: Reflected XSS Using Angular JS Sandbox Escape
type: procedure
verified: true
submitted: true
created_at: '2020-08-26T07:03:16.684782+00:00'
updated_at: '2023-05-26T18:08:43.878378+00:00'
platforms:
- Web
tags:
- '[[Angular JS XSS]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xss]]'
---

# Reflected XSS Using Angular JS Sandbox Escape

**Status**: ✓ Verified

## Summary

Reflected XSS can be performed through the user input fields in the application. It is also possible to escape Angular JS Sandbox by customising the payload. 

## Description

# Description

Reflected XSS can be performed through the user input fields in the application. It is also possible to escape Angular JS Sandbox by customising the payload.

# Procedure

1. Search for any string through the input field

2. In the response page, check the view source and see that the searched string is not reflected in any JavaScript template string.

3. XSS payload can now be created using ng-focus event in Angular JS to bypass CSP. The constructed payload would look like:

*<input id=x ng-focus=$event.path|orderBy:'(z=alert)(document.cookie)'>#x*

4. Now use the above payload to execute the script.

## Platforms

- Web

## Tags

- [[Angular JS XSS]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xss]]
