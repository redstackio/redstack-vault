---
id: 8f158aec-b431-4cb1-b7b8-f13067d046e0
name: Filter Bypass using UTF-7 Encoding for XSS Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.029039+00:00'
updated_at: '2023-04-10T20:21:56.208276+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Create Account|T1136 - Create Account]]'
- '[[Scripting|T1064 - Scripting]]'
sub_techniques:
- '[[Domain Account|T1136.002 - Domain Account]]'
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Bypass using UTF-7]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Filter Bypass using UTF-7 Encoding for XSS Injection

## Summary

Cross-Site Scripting (XSS) is a type of injection attack that allows an attacker to inject malicious scripts into web pages viewed by other users. Filter Bypass using UTF-7 Encoding is a technique that can be used to bypass certain types of input filters. By encoding the payload using UTF-7, the at

## Description

# Description

Cross-Site Scripting (XSS) is a type of injection attack that allows an attacker to inject malicious scripts into web pages viewed by other users. Filter Bypass using UTF-7 Encoding is a technique that can be used to bypass certain types of input filters. By encoding the payload using UTF-7, the attacker can bypass filters that are looking for specific characters or patterns. This can allow the attacker to inject malicious scripts into web pages that would otherwise be blocked. The business value of this attack is that it can be used to steal sensitive information, such as login credentials or personal data, from unsuspecting users.

## Requirements

1. Access to a vulnerable website with an input field that is not properly sanitized

1. Knowledge of XSS injection techniques

1. Knowledge of UTF-7 encoding

## Defense

1. Sanitize all user input to prevent malicious scripts from being injected

1. Use Content Security Policy (CSP) to restrict the types of content that can be loaded on a web page

1. Use a web application firewall (WAF) to detect and block malicious traffic

## Objectives

1. Inject and execute malicious scripts on a target website

1. Steal sensitive information from unsuspecting users

1. Bypass input filters that are designed to block certain characters or patterns

# Instructions

1. To perform an XSS injection, use this code snippet in a vulnerable input field. The code will execute the 'alert(1)' function when the page loads.

**Code**: [[+ADw-img src=+ACI-1+ACI- onerror=+ACI-alert(1)+ACI]]

> The 'src' attribute of the 'img' tag is set to '1', which does not exist. When the browser tries to load the image, it will fail and trigger the 'onerror' event. The 'onerror' event is set to execute the 'alert(1)' function, which will display an alert box with the message '1'. This is a simple example of an XSS injection that can be used to execute arbitrary code on a vulnerable website.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Create Account|T1136 - Create Account]]
- [[Scripting|T1064 - Scripting]]

### Sub-Techniques

- [[Domain Account|T1136.002 - Domain Account]]
- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Bypass using UTF-7]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
