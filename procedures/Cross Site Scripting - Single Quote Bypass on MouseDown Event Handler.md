---
id: 5e63251e-69c8-4edd-9315-2adc1e9d7d64
name: Cross Site Scripting - Single Quote Bypass on MouseDown Event Handler
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.475708+00:00'
updated_at: '2023-04-10T20:21:38.129078+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Bypass quotes in mousedown event]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Cross Site Scripting - Single Quote Bypass on MouseDown Event Handler

## Summary

Cross Site Scripting (XSS) is a type of injection attack where an attacker injects malicious code into a web page viewed by other users. This particular XSS attack involves bypassing quotes in a mousedown event handler. This can be done by using single quotes instead of double quotes. By doing so, 

## Description

# Description

Cross Site Scripting (XSS) is a type of injection attack where an attacker injects malicious code into a web page viewed by other users. This particular XSS attack involves bypassing quotes in a mousedown event handler. This can be done by using single quotes instead of double quotes. By doing so, an attacker can inject malicious code into the web page and execute it when the user clicks on a certain element. This attack can be used to steal sensitive information such as session cookies or login credentials.

From a technical perspective, this attack takes advantage of the fact that some web applications do not properly sanitize user input. By injecting malicious code into a web page, an attacker can exploit vulnerabilities in the web application and gain access to sensitive data. From a business perspective, this attack can result in reputational damage, loss of customer trust, and financial losses.


 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of the specific event handler being used

1. Knowledge of the syntax for bypassing quotes

 

## Defense

1. Properly sanitize user input to prevent injection attacks

1. Implement Content Security Policy (CSP) to limit the sources of executable scripts

1. Regularly scan web applications for vulnerabilities and patch them as needed

 

## Objectives

1. Inject malicious code into a web page

1. Execute the code when the user clicks on a certain element

1. Steal sensitive information such as session cookies or login credentials

 

# Instructions

1. To bypass a single quote in an on mousedown event handler, use the HTML entity &#39; instead of the single quote character.

 



**Code**: [[<a href="" onmousedown="var name = '&#39;;alert(1)]]



> In this example, the onmousedown event handler is setting a variable named 'name' to the value '&#39;;alert(1)//'. The HTML entity &#39; represents a single quote character. By using this entity instead of the actual single quote character, the code is able to bypass any input validation or filtering that may be in place to prevent the use of single quotes. This technique can be used to execute arbitrary code or inject malicious payloads into a vulnerable application.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Bypass quotes in mousedown event]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


