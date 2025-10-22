---
id: 7f002325-a9bc-4074-8253-c13e21294eca
name: Information Disclosure Using Debug Page
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T11:51:05.922300+00:00'
updated_at: '2023-05-26T18:24:00.462343+00:00'
platforms:
- Web
tags:
- '[[information disclosure]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Information Disclosure Using Debug Page

**Status**: ✓ Verified

## Summary

Sensitive information can be obtained using debug pages in the application. Debug pages are meant for development environment. They can be misused to reveal information. 

## Description

# Description

Sensitive information can be obtained using debug pages in the application. Debug pages are meant for development environment. They can be misused to reveal information.

# Procedure

1. Access the application by configuring Burp Proxy.

2. Right-click and select view source. HTML comment with debug page is observed.

3. In the target tab of Burp Suite, navigate through the *phpinfo.php* page. Right click on it and send to repeater.

4. Send request and the response contains the *SECRET_KEY*

## Platforms

- Web

## Tags

- [[information disclosure]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
