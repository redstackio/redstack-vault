---
id: 4f1e2c41-fcc7-4f71-954c-d6391bbfd498
name: 'CSRF To Change Victim Password '
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T15:22:16.095479+00:00'
updated_at: '2023-05-26T01:35:18.100053+00:00'
platforms:
- Web
tags:
- '[[CSRF]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# CSRF To Change Victim Password 

**Status**: ✓ Verified

## Summary

CSRF can be performed by placing a hidden FORM request in a web page and sharing it with the victim. If the victim access the page, the request gets submitted using the existing session ID in the browser. 

## Description

# Description

CSRF can be performed by placing a hidden FORM request in a web page and sharing it with the victim. If the victim access the page, the request gets submitted using the existing session ID in the browser.

# Instructions

1. Identify any operation in the application. Here we have selected change password page.

2. Create a HTML page with the request that is submitted when a password is changed.

**Code**: [[<html>
  <body onload="document.getElementById('x]]

3. Save the page and open it in  the browser. The change password request gets submitted and the password of current user gets changed.

## Platforms

- Web

## Tags

- [[CSRF]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
