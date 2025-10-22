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

2. Send the request to the repeater tab. Observe that CSRF tokens are implemented in the cookie as well as in the body . Value of the CSRF token in the body parameter is validated by comparing it with CSRF toekn in the cookie.

3.Perform a search, send the resulting request to Burp Repeater, and observe that the search term gets reflected in the Set-Cookie header. Since the search function has no CSRF protection, you can use this to inject cookies into the victim user's browser.

4.Craft a URL  to inject a fake csrf cookie into the victim's browser.  Use the CSRF POC generator on this request.

***/?search=test%0d%0aSet-Cookie:%20csrf=fa*ke**

5.Add the following code to inject the cookie and submit the change email form.

***<img src="$cookie-injection-url" onerror="document.forms[0].submit();"*/>**

## Platforms

- Web

## Tags

- [[CSRF]]
- [[Web Applications]]
