---
id: 978ae2b2-45e9-4426-a1f9-2558845463d8
name: Reflected Cross Site Scripting (XSS)
type: procedure
verified: true
submitted: true
created_at: '2020-07-23T14:29:57.213789+00:00'
updated_at: '2023-05-26T01:31:43.490331+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xss]]'
---

# Reflected Cross Site Scripting (XSS)

**Status**: ✓ Verified

## Summary

An attacker will be able to execute malicious javascripts in the victim's browser if the application is vulnerable to XSS. Scripts are passed as inputs through the form fields or URL parameters. 

## Description

# Description

An attacker will be able to execute malicious *javascripts* in the victim's browser if the application is vulnerable to XSS. Scripts are passed as inputs through the form fields or URL parameters.

# Instructions

1. Script tag is passed as input to the search field.

Payload: <script>alert(1)</script>

2. The inserted script is executed and a popup is observed in the page.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xss]]
