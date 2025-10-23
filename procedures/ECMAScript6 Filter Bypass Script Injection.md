---
id: 97d40b7a-67ac-447b-93c5-f12ea1ca23ce
name: ECMAScript6 Filter Bypass Script Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.958753+00:00'
updated_at: '2023-04-10T20:21:36.375102+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Code Signing|T1116 - Code Signing]]'
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[Bypass using ECMAScript6]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# ECMAScript6 Filter Bypass Script Injection

## Summary

ECMAScript6 Filter Bypass Script Injection is a technique used by attackers to bypass filters that are in place to prevent cross-site scripting attacks. This technique is used when the attacker is unable to inject their payload directly into the target site, and must instead inject it into a third-

## Description

# Description

ECMAScript6 Filter Bypass Script Injection is a technique used by attackers to bypass filters that are in place to prevent cross-site scripting attacks. This technique is used when the attacker is unable to inject their payload directly into the target site, and must instead inject it into a third-party site that is trusted by the target site. The attacker uses ECMAScript6 to create a script that is executed in the context of the target site, allowing them to execute arbitrary code and take control of the victim's browser. This technique is highly effective and can be used to steal sensitive information, perform actions on behalf of the victim, or spread malware.

Technical Explanation: ECMAScript6, also known as ES6 or ECMAScript 2015, is a version of the JavaScript programming language that was standardized in 2015. It introduced many new features and improvements to the language, including new syntax for defining functions, classes, and variables. One of the new features introduced in ES6 is the ability to use template literals, which allow developers to embed expressions inside strings using the ${} syntax. This feature can be used by attackers to inject malicious code into a trusted third-party site, which is then executed in the context of the target site.

Business Value: This technique allows attackers to bypass filters that are in place to prevent cross-site scripting attacks, and take control of the victim's browser. This can lead to the theft of sensitive information, the spread of malware, or the execution of actions on behalf of the victim. This can have serious consequences for businesses, including loss of reputation, legal liability, and financial losses.

 

## Requirements

1. Access to a trusted third-party site

1. Knowledge of ECMAScript6 syntax

 

## Defense

1. Implement input validation and output encoding to prevent XSS attacks

1. Implement Content Security Policy (CSP) to restrict the types of content that can be loaded on a page

1. Implement Subresource Integrity (SRI) to verify that resources loaded on a page have not been tampered with

 

## Objectives

1. Inject malicious code into a trusted third-party site

1. Execute arbitrary code in the context of the target site

1. Take control of the victim's browser

 

# Instructions

1. This command injects a script that displays an alert message with the text '1'.

 



**Code**: [[<script>alert('1');</script>]]



> The 'data' field should be modified to display a different message in the alert. Be careful when using script injection as it can be used maliciously to steal user data or perform other harmful actions.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Code Signing|T1116 - Code Signing]]
- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Tags

- [[Bypass using ECMAScript6]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


