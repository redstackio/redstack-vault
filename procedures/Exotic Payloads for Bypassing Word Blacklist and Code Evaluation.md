---
id: 3b230502-b8e4-47c9-bb62-3ab28940f8cf
name: Exotic Payloads for Bypassing Word Blacklist and Code Evaluation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.375593+00:00'
updated_at: '2023-04-10T20:21:43.922055+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Bypass word blacklist with code evaluation]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Exotic Payloads for Bypassing Word Blacklist and Code Evaluation

## Summary

Exotic payloads can be used to bypass word blacklist and execute code in the context of the vulnerable application. This technique can be used for various purposes, such as stealing user credentials, defacing web pages, or performing other malicious actions. By using code evaluation, an attacker ca

## Description

# Description

Exotic payloads can be used to bypass word blacklist and execute code in the context of the vulnerable application. This technique can be used for various purposes, such as stealing user credentials, defacing web pages, or performing other malicious actions. By using code evaluation, an attacker can execute arbitrary code in the context of the application, allowing them to take full control of the system. To perform this attack, the attacker needs to find a vulnerable input field that is not properly sanitized and inject their payload. This can be done through various means, such as URL parameters, cookies, or form inputs.

 

## Requirements

1. Access to vulnerable web application

1. Knowledge of exotic payload techniques

 

## Defense

1. Validate and sanitize all user input to prevent code injection

1. Implement a content security policy (CSP) to restrict the use of inline scripts and other potentially dangerous features

1. Regularly audit and update the application to address any known vulnerabilities

 

## Objectives

1. Execute arbitrary code in the context of the vulnerable application

1. Steal user credentials

1. Deface web pages

1. Perform other malicious actions

 

# Instructions

1. This command is used to display an alert message on a web page using JavaScript.

 



**Code**: [[eval('ale'+'rt(0)');
Function("ale"+"rt(1)")();
ne]]



> The command contains multiple ways to execute an alert command in JavaScript. The first method is using the `eval` function, which evaluates the string `alert(0)` and displays an alert message with the number 0. The second method is using the `Function` constructor to create a new function that displays an alert message with the number 1. The third method is using a template literal to create a new function that displays an alert message with the string 'alert'. The fourth method is using the `setTimeout` function to delay the execution of the alert message by 2 milliseconds. The fifth method is using the `setInterval` function to repeatedly execute the alert message every 10 milliseconds. The sixth method is using the `Set` constructor to create a new set and immediately execute a function that displays an alert message with the number 13. The seventh method is similar to the third method, but uses hexadecimal escape sequences to create the string 'alert'.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Bypass word blacklist with code evaluation]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


