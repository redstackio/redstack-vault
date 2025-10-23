---
id: 6f1c0fcf-cf44-4821-9280-d00f2c0a27c7
name: WAF Bypass using Chrome Auditor XSS Attack Vector
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.457340+00:00'
updated_at: '2023-04-10T20:21:42.611130+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Uncommonly Used Port|T1065 - Uncommonly Used Port]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Chrome Auditor - 9th August 2018]]'
- '[[Common WAF Bypass]]'
- '[[Cross Site Scripting]]'
---

# WAF Bypass using Chrome Auditor XSS Attack Vector

## Summary

WAF Bypass using Chrome Auditor XSS Attack Vector is a technique used to bypass Web Application Firewall (WAF) protection. This technique is based on exploiting a cross-site scripting (XSS) vulnerability in the target web application. The attacker injects malicious code into the web application, wh

## Description

# Description

WAF Bypass using Chrome Auditor XSS Attack Vector is a technique used to bypass Web Application Firewall (WAF) protection. This technique is based on exploiting a cross-site scripting (XSS) vulnerability in the target web application. The attacker injects malicious code into the web application, which is then executed in the victim's browser. The Chrome Auditor XSS Attack Vector is a specific XSS payload that can bypass certain WAFs, including those that use signature-based detection. This technique can be used to steal sensitive information, such as session cookies, or to perform other malicious actions on the victim's behalf.

Technical Description: The attacker injects a specially crafted XSS payload, such as the Chrome Auditor XSS Attack Vector, into the target web application. If the WAF does not properly detect and block the payload, the injected code will be executed in the victim's browser, allowing the attacker to perform various malicious actions. This technique is effective against WAFs that use signature-based detection, as the payload can be obfuscated to evade detection.

Business Value: This technique can be used to bypass WAF protection and gain unauthorized access to sensitive information, such as customer data or intellectual property. This can result in financial loss, reputational damage, and legal consequences.

 

## Requirements

1. Access to target web application

1. Ability to inject XSS payload

1. Knowledge of Chrome Auditor XSS Attack Vector

 

## Defense

1. Implement a WAF that uses behavior-based detection instead of signature-based detection

1. Regularly update the WAF's signature database

1. Perform regular vulnerability assessments and penetration testing on the web application

 

## Objectives

1. Bypass WAF protection

1. Execute malicious code in victim's browser

1. Steal sensitive information

 

# Instructions

1. The XSS Attack Vector command is used to test and demonstrate the vulnerability of a web application to cross-site scripting (XSS) attacks. The command injects a malicious script into the webpage, which is executed by the victim's browser when they visit the page. This script can be used to steal sensitive information or perform unauthorized actions on behalf of the victim. The injected script in this command is an example of an XSS payload that can be used to execute an alert() function.

 



**Code**: [[</script><svg><script>alert(1)-%26apos%3B]]



> The 'data' field contains the XSS payload that is injected into the webpage. The 'lang' field specifies the language of the payload, which is JavaScript in this case. The 'text' field is not used in this command. The 'instruction' field provides details on how to use this command to test for XSS vulnerabilities, and the 'explain' field provides a detailed explanation of what XSS attacks are and how they work.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Uncommonly Used Port|T1065 - Uncommonly Used Port]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Chrome Auditor - 9th August 2018]]
- [[Common WAF Bypass]]
- [[Cross Site Scripting]]


