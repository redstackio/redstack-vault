---
id: 3a6c80bc-b345-428e-a0af-90e313f3dc78
name: XSS in Files and Markdown
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.080059+00:00'
updated_at: '2023-04-10T20:21:55.488517+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
- '[[User Execution|T1204 - User Execution]]'
tags:
- '[[Cross Site Scripting]]'
- '[[XSS in files]]'
- '[[XSS in Markdown]]'
---

# XSS in Files and Markdown

## Summary

XSS in files and markdown is a common attack vector that allows an attacker to inject malicious code into web pages. This attack can be used to steal sensitive information, such as session cookies, passwords, and other user data. The attack works by injecting malicious code into files or markdown c

## Description

# Description

XSS in files and markdown is a common attack vector that allows an attacker to inject malicious code into web pages. This attack can be used to steal sensitive information, such as session cookies, passwords, and other user data. The attack works by injecting malicious code into files or markdown content that is then displayed on a web page. The user's browser then executes the injected code, which can lead to a compromise of the user's system or the web server.

Technical Explanation: Cross-Site Scripting (XSS) is a type of injection attack that allows an attacker to execute malicious scripts in a victim's browser. XSS attacks occur when an attacker is able to inject malicious code into a web page that is then executed by the victim's browser. This can be achieved by injecting code into files or markdown content that is then displayed on a web page.

Business Value: XSS attacks can lead to a compromise of sensitive data, such as user credentials and financial information. This can result in reputational damage, loss of trust, and financial losses.

 

## Requirements

1. Access to a vulnerable web application

1. Ability to inject malicious code into files or markdown content

 

## Defense

1. Implement input validation and sanitization techniques to prevent injection attacks

1. Use Content Security Policy (CSP) headers to restrict the types of content that can be loaded on a web page

1. Regularly update and patch web applications to address known vulnerabilities

 

## Objectives

1. Inject malicious code into files or markdown content

1. Execute the injected code in the victim's browser

1. Steal sensitive information from the victim's browser

 

# Instructions

1. To perform a Cross-Site Scripting (XSS) attack, use one of these payloads as the input parameter for the vulnerable field on the target website. These payloads will execute JavaScript code in the context of the victim's browser, allowing the attacker to steal sensitive information or perform actions on behalf of the victim.

 



**Code**: [[[a](javascript:prompt(document.cookie))
[a](j a v ]]



> The first payload uses the `javascript:` protocol to execute the `prompt()` function, which displays a dialog box containing the value of the `document.cookie` property. The second payload uses spaces to evade filters that block the `javascript:` protocol. The third payload uses the `data:` protocol to embed a base64-encoded HTML document containing a script that executes the `alert()` function. The fourth payload uses the `throw` statement to trigger the `onerror` event, which executes the `alert()` function.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]
- [[User Execution|T1204 - User Execution]]

## Tags

- [[Cross Site Scripting]]
- [[XSS in files]]
- [[XSS in Markdown]]


