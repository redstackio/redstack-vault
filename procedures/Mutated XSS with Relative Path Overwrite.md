---
id: 14c670f1-36d3-4323-9358-e230354ebf15
name: Mutated XSS with Relative Path Overwrite
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.916452+00:00'
updated_at: '2023-04-06T03:56:43.929388+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Mutated XSS for Browser IE8/IE9]]'
- '[[XSS with Relative Path Overwrite - IE 8/9 and lower]]'
---

# Mutated XSS with Relative Path Overwrite

## Summary

Mutated XSS with Relative Path Overwrite is a technique that exploits a vulnerability in the Listing ID parameter of an application. This technique targets Internet Explorer versions 8 and 9. The attack works by injecting malicious code into the parameter, which is then executed by the browser. The

## Description

# Description

Mutated XSS with Relative Path Overwrite is a technique that exploits a vulnerability in the Listing ID parameter of an application. This technique targets Internet Explorer versions 8 and 9. The attack works by injecting malicious code into the parameter, which is then executed by the browser. The attack is called 'mutated' because it uses a combination of techniques to bypass security measures put in place to prevent XSS attacks.

Technical Explanation: The attack works by manipulating the path of the URL to include a malicious script. This script is then executed in the context of the vulnerable page, allowing the attacker to steal sensitive information or take control of the user's session. This technique is effective because it bypasses traditional XSS defenses, such as input validation and output encoding.

Business Value: This technique can be used by attackers to gain unauthorized access to sensitive information, such as user credentials and financial data. It can also be used to take control of user sessions, allowing the attacker to perform actions on behalf of the user.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of the Listing ID parameter vulnerability

1. Internet Explorer 8 or 9

## Defense

1. Implement input validation and output encoding on all user input fields

1. Use a Content Security Policy (CSP) to restrict the sources of executable scripts

1. Regularly update and patch web applications to prevent known vulnerabilities

## Objectives

1. Inject and execute malicious code on a vulnerable web application

1. Gain unauthorized access to sensitive information

1. Take control of user sessions

# Instructions

1. To exploit this vulnerability, an attacker can inject malicious code into the Listing ID parameter. This can be done by inserting a script tag with a payload that executes arbitrary code.

**Code**: [[<listing id=x>&lt;img src=1 onerror=alert(1)&gt;</]]

> The Listing ID parameter is vulnerable to a cross-site scripting (XSS) attack. This occurs when an attacker is able to inject malicious code into a vulnerable web page, which is then executed by unsuspecting users who visit the page. In this case, an attacker can inject a script tag with a payload that executes arbitrary code. When the page is loaded, the script is executed and the payload is executed, allowing the attacker to steal sensitive information or perform other malicious actions on the user's behalf.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Tags

- [[Mutated XSS for Browser IE8/IE9]]
- [[XSS with Relative Path Overwrite - IE 8/9 and lower]]
