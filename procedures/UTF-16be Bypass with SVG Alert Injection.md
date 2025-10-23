---
id: 7fc92ec9-b7fd-498f-92e3-a5e57d2fd842
name: UTF-16be Bypass with SVG Alert Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.078673+00:00'
updated_at: '2023-04-10T20:21:44.993577+00:00'
tags:
- '[[Bypass using UTF-16be]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# UTF-16be Bypass with SVG Alert Injection

## Summary

This procedure utilizes a bypass technique that leverages UTF-16be encoding to evade filters and inject an SVG alert payload. This can be used to bypass input filtering and execute a successful Cross Site Scripting (XSS) attack. By encoding the payload in UTF-16be, it can bypass filters that are no

## Description

# Description

This procedure utilizes a bypass technique that leverages UTF-16be encoding to evade filters and inject an SVG alert payload. This can be used to bypass input filtering and execute a successful Cross Site Scripting (XSS) attack. By encoding the payload in UTF-16be, it can bypass filters that are not designed to detect this type of encoding. The SVG alert payload can be used to test for the presence of an XSS vulnerability or to execute an attack against the user's browser.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of the target's input filtering mechanisms

1. Ability to encode payloads in UTF-16be format

 

## Defense

1. Implement input filtering that can detect and block UTF-16be encoded payloads

1. Use Content Security Policy (CSP) to restrict the sources of content that can be loaded by the browser

1. Educate users on the risks of XSS attacks and how to identify them

 

## Objectives

1. Inject and execute an SVG alert payload using UTF-16be encoding

1. Bypass input filtering to successfully perform a Cross Site Scripting attack

 

# Instructions

1. This command is used to inject an SVG alert into a web page.

 



**Code**: [[%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=]]



> The 'data' field contains the SVG code that will be injected into the web page. The 'lang' field specifies the language used for the injection (in this case, JavaScript). The injected code will trigger an alert message to be displayed when the web page is loaded.

## Tags

- [[Bypass using UTF-16be]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


