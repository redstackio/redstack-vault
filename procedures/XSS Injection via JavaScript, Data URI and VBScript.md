---
id: f5715436-48ed-4553-8e44-b87592f8d19e
name: XSS Injection via JavaScript, Data URI and VBScript
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.962454+00:00'
updated_at: '2023-04-10T20:21:37.431730+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Cross Site Scripting]]'
- '[[XSS in wrappers javascript and data URI]]'
---

# XSS Injection via JavaScript, Data URI and VBScript

## Summary

Cross-Site Scripting (XSS) is a type of attack that allows an attacker to inject malicious scripts into web pages viewed by other users. This can be done by exploiting vulnerabilities in web applications that allow user input to be reflected back to other users without proper sanitization. By injec

## Description

# Description

Cross-Site Scripting (XSS) is a type of attack that allows an attacker to inject malicious scripts into web pages viewed by other users. This can be done by exploiting vulnerabilities in web applications that allow user input to be reflected back to other users without proper sanitization. By injecting malicious scripts, an attacker can steal sensitive information such as session cookies, login credentials, and other personal information. This procedure covers three different methods of XSS injection: via JavaScript, Data URI and VBScript. 

In the case of JavaScript XSS injection, an attacker can inject malicious JavaScript code into a vulnerable web page. The script will then execute in the user's browser when they visit the page. Data URI XSS injection is similar, but instead of injecting JavaScript code directly into the page, an attacker can encode the script in a data URI and inject it into the page as an image or other resource. Finally, XSS with VBScript uses the same technique as JavaScript injection, but instead injects VBScript code. 

The business value of understanding and mitigating XSS attacks is to prevent data breaches, protect user privacy, and maintain the integrity of web applications.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of XSS injection techniques

1. Tools such as Burp Suite or OWASP ZAP to automate the injection process

## Defense

1. Sanitize user input in web applications to prevent XSS vulnerabilities

1. Implement Content Security Policy (CSP) to restrict the execution of scripts from unknown sources

1. Regularly scan web applications for vulnerabilities and apply security patches as needed

## Objectives

1. Inject malicious scripts into vulnerable web pages

1. Steal sensitive information from other users

1. Compromise web applications for persistence and further exploitation

# Instructions

1. This command demonstrates how an attacker can inject malicious JavaScript code into a vulnerable web application using various techniques such as encoding, newline characters, escape characters, and comments. The injected code can then be executed in the victim's browser, leading to various attacks such as stealing user credentials, performing unauthorized actions, and more.

**Code**: [[javascript:prompt(1)

%26%23106%26%2397%26%23118%2]]

> The 'data' field contains examples of how an attacker can inject JavaScript code using various techniques. The 'lang' field specifies the language used for the injection. The 'text' field provides a brief description of the vulnerability. The 'instruction' field gives an overview of the command and how it can be used. The 'explain' field provides additional details on the vulnerability and the techniques used for injection.

2. To execute a cross-site scripting attack with data URIs, an attacker can craft a malicious HTML payload and encode it as a data URI. This payload can then be injected into vulnerable web applications through various means, such as input fields or URLs.

**Code**: [[data:text/html,<script>alert(0)</script>
data:text]]

> The 'data' field in the provided JSON object contains two different data URIs, separated by a newline character. The first URI simply executes a JavaScript alert box when loaded. The second URI is base64-encoded HTML that contains a script tag which executes a JavaScript payload when loaded. The 'lang' field specifies that the payload is written in JavaScript.

3. This command demonstrates how to execute a cross-site scripting (XSS) attack using VBScript. The VBScript code is executed in Internet Explorer only.

**Code**: [[vbscript:msgbox("XSS")]]

> The 'data' field contains the VBScript code that will be executed when the user visits a page containing this code. The 'lang' field specifies that the code is written in JavaScript. The 'text' field provides a brief description of the attack. The 'instruction' field provides step-by-step instructions on how to use this command. The 'explain' field provides additional information on the attack and its potential impact.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Cross Site Scripting]]
- [[XSS in wrappers javascript and data URI]]
