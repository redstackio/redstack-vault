---
id: 235ed1e6-f0b7-4fcb-8f55-092ee852c78e
name: XSS in HTML and JS Context
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.941823+00:00'
updated_at: '2023-04-10T20:21:47.103144+00:00'
tags:
- '[[Cross Site Scripting]]'
- '[[XSS in HTML/Applications]]'
- '[[XSS in JS Context]]'
---

# XSS in HTML and JS Context

## Summary

Cross-site scripting (XSS) is a type of attack that injects malicious code into a web page viewed by other users. In the HTML context, this can occur when an attacker is able to inject script tags or other HTML elements that execute arbitrary code. In the JS context, this can occur when an attacker

## Description

# Description

Cross-site scripting (XSS) is a type of attack that injects malicious code into a web page viewed by other users. In the HTML context, this can occur when an attacker is able to inject script tags or other HTML elements that execute arbitrary code. In the JS context, this can occur when an attacker is able to inject code that is executed by the JavaScript interpreter. This type of attack can be used to steal sensitive information, such as session cookies, or to perform actions on behalf of the victim. From a technical standpoint, XSS attacks can be launched using a variety of techniques, including reflected, stored, and DOM-based XSS. Businesses can protect themselves from XSS attacks by ensuring that input validation and output encoding are in place, and by using Content Security Policy (CSP) to restrict the types of content that can be loaded on a web page.

 

## Requirements

1. Access to a vulnerable web application

1. Ability to inject malicious code into the web application

 

## Defense

1. Implement input validation and output encoding to prevent malicious code injection

1. Use Content Security Policy (CSP) to restrict the types of content that can be loaded on a web page

1. Regularly scan web applications for vulnerabilities and patch them as necessary

 

## Objectives

1. Inject malicious code into a web page viewed by other users

1. Steal sensitive information, such as session cookies

1. Perform actions on behalf of the victim

 

# Instructions

1. To perform a Cross-Site Scripting (XSS) attack using this payload, follow the steps below:

1. Inject the payload into a vulnerable field on the target website.
2. When the victim visits the page, the script will execute and the attacker will be able to steal sensitive information or perform actions on behalf of the victim.

Note: This payload is designed to bypass certain types of input sanitization that may be in place on the target website.

 



**Code**: [[-(confirm)(document.domain)//
; alert(1);//
// (pa]]



> The payload consists of the following components:

1. '-(confirm)': This is a trick to bypass certain types of input sanitization that may be in place on the target website.
2. '(document.domain)': This retrieves the domain of the current page.
3. '//': This is a comment to ensure that the rest of the payload is not interpreted as code.
4. '; alert(1);//': This is the actual payload that will be executed. It displays an alert box with the number 1.

The payload can be modified to perform other types of attacks, such as stealing cookies or performing actions on behalf of the victim.

## Tags

- [[Cross Site Scripting]]
- [[XSS in HTML/Applications]]
- [[XSS in JS Context]]


