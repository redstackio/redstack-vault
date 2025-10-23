---
id: e820d0c8-01ca-48d8-9ebc-38c1b34785c2
name: Cloudflare XSS Bypass via Common WAF and HTML Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.369532+00:00'
updated_at: '2023-04-10T20:21:30.892823+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[5th June 2019]]'
- '[[Cloudflare XSS Bypasses by [@Bohdan Korzhynskyi](https://twitter.com/bohdansec)]]'
- '[[Common WAF Bypass]]'
- '[[Cross Site Scripting]]'
---

# Cloudflare XSS Bypass via Common WAF and HTML Injection

## Summary

This procedure involves bypassing a WAF to perform a Cross Site Scripting (XSS) attack on a website protected by Cloudflare. The attacker first identifies a common WAF bypass technique that is not detected by the target website's WAF. The attacker then injects HTML code into a vulnerable input fiel

## Description

# Description

This procedure involves bypassing a WAF to perform a Cross Site Scripting (XSS) attack on a website protected by Cloudflare. The attacker first identifies a common WAF bypass technique that is not detected by the target website's WAF. The attacker then injects HTML code into a vulnerable input field on the target website to execute malicious JavaScript code. This allows the attacker to steal sensitive information, such as session cookies, and perform actions on behalf of the victim user. This attack can be used for various purposes, such as phishing, malware delivery, or website defacement.

From a technical perspective, this procedure involves crafting a payload that bypasses the WAF by encoding or obfuscating the malicious code. The attacker then injects the payload into a vulnerable input field, such as a search box or a comment form. When the victim user interacts with the input field, the payload is executed in their browser, allowing the attacker to perform the XSS attack.

From a business perspective, this attack can result in reputational damage, loss of customer trust, and legal consequences. It can also lead to theft of sensitive information, such as customer data or intellectual property.

 

## Requirements

1. Access to a vulnerable website protected by Cloudflare

1. Knowledge of common WAF bypass techniques

1. Knowledge of HTML Injection techniques

1. A web browser and a text editor

 

## Defense

1. Implement a WAF that can detect and block common WAF bypass techniques

1. Sanitize user input to prevent HTML Injection attacks

1. Use Content Security Policy (CSP) to restrict the execution of untrusted scripts

 

## Objectives

1. Perform a successful XSS attack on a website protected by Cloudflare

1. Steal sensitive information, such as session cookies or user credentials

1. Perform actions on behalf of the victim user, such as posting a malicious comment or sending a phishing email

 

# Instructions

1. The HTML Injection vulnerability allows an attacker to inject malicious code into a webpage viewed by other users. The attacker can use this vulnerability to execute arbitrary code, steal sensitive information, or perform other malicious actions.

 



**Code**: [[1'"><img/src/onerror=.1|alert``>]]



> The 'data' field contains the malicious code that will be injected into the webpage. The code is executed when the webpage is loaded by a victim's browser. The attacker can use various techniques to inject this code, such as input fields, cookies, or HTTP headers. To prevent HTML Injection vulnerabilities, input validation and output encoding should be used to ensure that user input is properly sanitized and encoded before being displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[5th June 2019]]
- [[Cloudflare XSS Bypasses by [@Bohdan Korzhynskyi](https://twitter.com/bohdansec)]]
- [[Common WAF Bypass]]
- [[Cross Site Scripting]]


