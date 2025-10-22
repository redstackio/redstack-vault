---
id: 96b7933e-805e-4b45-8188-ce1989ae8563
name: Exotic Payloads for Bypassing Filters in JavaScript
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.846676+00:00'
updated_at: '2023-04-10T20:21:41.591307+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Uncommonly Used Port|T1065 - Uncommonly Used Port]]'
tags:
- '[[Bypass ";" using another character]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Exotic Payloads for Bypassing Filters in JavaScript

## Summary

Exotic payloads are a technique used to bypass filters in JavaScript. The use of exotic payloads can help an attacker bypass filters that are used to block certain characters or strings from being entered into a web application. This can be used to exploit a cross-site scripting (XSS) vulnerability

## Description

# Description

Exotic payloads are a technique used to bypass filters in JavaScript. The use of exotic payloads can help an attacker bypass filters that are used to block certain characters or strings from being entered into a web application. This can be used to exploit a cross-site scripting (XSS) vulnerability in a web application. The technique involves using a character that looks similar to the forbidden character, but is not blocked by the filter. In this case, the technique is to bypass the semicolon (;) character using another character.

An attacker can use this technique to execute arbitrary JavaScript code on a victim's browser, which can result in the theft of sensitive information or the takeover of the victim's session. This technique is commonly used by attackers to exploit vulnerabilities in web applications and can be very effective if the filter bypass is successful.

The business value of understanding and mitigating against this technique is to ensure that web applications are secure and that sensitive data is not compromised.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of JavaScript and exotic payloads

## Defense

1. Implement input validation and output encoding to prevent XSS attacks

1. Use Content Security Policy (CSP) to restrict the sources of content that can be loaded by a web page

1. Implement a Web Application Firewall (WAF) to detect and block malicious requests

## Objectives

1. Bypass filters that are used to block certain characters or strings from being entered into a web application

1. Execute arbitrary JavaScript code on a victim's browser

1. Exploit vulnerabilities in web applications

# Instructions

1. This command demonstrates the various operators in JavaScript and their usage.

**Code**: [['te' * alert('*') * 'xt';
'te' / alert('/') / 'xt']]

> The above code demonstrates the usage of different operators in JavaScript. The '*' operator is used for multiplication, '/' for division, '%' for modulus, '-' for subtraction, '+' for addition, '^' for exponentiation, '>' for greater than, '<' for less than, '==' for equality, '&' for bitwise AND, ',' for sequence, '|' for bitwise OR, '?' for conditional (ternary) operator, 'in' for checking if a property exists in an object, and 'instanceof' for checking if an object is an instance of a particular class. Each operator is used between the string 'te' and 'xt' and an alert is displayed with the respective operator used. This helps in understanding the working of each operator in JavaScript.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Uncommonly Used Port|T1065 - Uncommonly Used Port]]

## Tags

- [[Bypass ";" using another character]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
