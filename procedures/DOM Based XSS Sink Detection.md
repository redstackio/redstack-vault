---
id: a0d963b1-8e2f-4de1-b363-3d5128dcaa4a
name: DOM Based XSS Sink Detection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.918842+00:00'
updated_at: '2023-04-10T20:21:46.744354+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Cross Site Scripting]]'
- '[[DOM based XSS]]'
- '[[XSS in HTML/Applications]]'
---

# DOM Based XSS Sink Detection

## Summary

DOM Based XSS Sink Detection is a technique used to detect and prevent DOM-based cross-site scripting attacks. This technique involves analyzing the application's client-side code to identify potential sources of user input that could be used to inject malicious scripts. Once these sources are iden

## Description

# Description

DOM Based XSS Sink Detection is a technique used to detect and prevent DOM-based cross-site scripting attacks. This technique involves analyzing the application's client-side code to identify potential sources of user input that could be used to inject malicious scripts. Once these sources are identified, the code is modified to sanitize user input and prevent the injection of malicious scripts. This technique is effective in preventing XSS attacks that are executed on the client-side of the application. The business value of this technique is that it helps to protect sensitive data and prevent unauthorized access to critical systems.

## Requirements

1. Access to the client-side code of the application.

1. Knowledge of the application's architecture and potential sources of user input.

1. Ability to modify the code and implement sanitization measures.

## Defense

1. Implement input validation and sanitization measures to prevent the injection of malicious scripts.

1. Use Content Security Policy (CSP) to restrict the types of content that can be loaded by the application.

1. Regularly test the application for vulnerabilities and apply security patches as needed.

## Objectives

1. To detect and prevent DOM-based cross-site scripting attacks.

1. To identify potential sources of user input that could be used to inject malicious scripts.

1. To sanitize user input and prevent the injection of malicious scripts.

# Instructions

1. To detect a DOM XSS sink, you can perform the following steps:
1. Identify the DOM elements that are being used to render user input.
2. Check if the input is being used in an unsafe manner, such as being directly concatenated with HTML tags or attributes.
3. If the input is being used in an unsafe manner, sanitize the input before rendering it on the page.
4. Use a tool such as a DOM XSS scanner to detect any potential vulnerabilities in the page.

**Code**: [[#"><img src=/ onerror=alert(2)>]]

> The 'data' field in this JSON object contains a sample payload that can trigger a DOM XSS vulnerability. The 'lang' field specifies the programming language being used. The 'text' field provides a brief description of the vulnerability. The 'instruction' field provides steps on how to detect this vulnerability. The 'explain' field provides additional information on the vulnerability and its impact.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Cross Site Scripting]]
- [[DOM based XSS]]
- [[XSS in HTML/Applications]]
