---
id: 1a2fed98-34a8-44d9-937a-021971e1ac84
name: Hidden Input XSS Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.872756+00:00'
updated_at: '2023-04-10T20:21:31.538401+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[JavaScript|T1059.007 - JavaScript]]'
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Cross Site Scripting]]'
- '[[XSS in hidden input]]'
- '[[XSS in HTML/Applications]]'
---

# Hidden Input XSS Attack

## Summary

A Hidden Input XSS Attack is a type of Cross Site Scripting (XSS) attack that exploits hidden input fields in HTML forms. The attacker injects malicious code into the hidden input field, which is then executed by unsuspecting users who interact with the form. This can lead to the attacker gaining a

## Description

# Description

A Hidden Input XSS Attack is a type of Cross Site Scripting (XSS) attack that exploits hidden input fields in HTML forms. The attacker injects malicious code into the hidden input field, which is then executed by unsuspecting users who interact with the form. This can lead to the attacker gaining access to sensitive information, such as login credentials or credit card numbers. From an offensive standpoint, this attack can be used to bypass security controls and gain access to a target's network.

Technically, this attack works by injecting malicious code into the value attribute of the hidden input field. When the user submits the form, the code is executed in the context of the vulnerable application. This can allow the attacker to steal cookies, perform actions on behalf of the user, or redirect the user to a malicious website.

From a business perspective, this attack can result in stolen customer data, loss of reputation, and potential legal liabilities.

 

## Requirements

1. Access to a vulnerable application with hidden input fields

1. Knowledge of HTML and JavaScript

1. Possibly a web proxy or other tool to intercept and modify HTTP requests

 

## Defense

1. Use input validation and sanitization techniques to prevent malicious code injection

1. Implement Content Security Policy (CSP) to limit the sources of executable scripts

1. Regularly scan web applications for vulnerabilities and patch them promptly

 

## Objectives

1. Inject malicious code into the hidden input field of a vulnerable application

1. Execute the malicious code in the context of the vulnerable application

1. Gain access to sensitive information or perform actions on behalf of the user

 

# Instructions

1. To use this command, insert the provided code snippet into an HTML document where you want to create a hidden input field that triggers an alert when clicked. Press CTRL+SHIFT+X to trigger the onclick event and see the alert message.

 



**Code**: [[<input type="hidden" accesskey="X" onclick="alert(]]



> This command creates a hidden input field that executes a JavaScript alert function when clicked. The accesskey attribute sets a keyboard shortcut for the input field, and the onclick attribute specifies the JavaScript code to execute when the input field is clicked. The text field is not used in this command.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[JavaScript|T1059.007 - JavaScript]]
- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Cross Site Scripting]]
- [[XSS in hidden input]]
- [[XSS in HTML/Applications]]


