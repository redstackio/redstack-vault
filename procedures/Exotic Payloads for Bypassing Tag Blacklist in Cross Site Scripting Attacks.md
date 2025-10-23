---
id: 3f1ac115-238c-4245-9f82-2303f586a097
name: Exotic Payloads for Bypassing Tag Blacklist in Cross Site Scripting Attacks
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.342130+00:00'
updated_at: '2023-04-10T20:21:51.600397+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[PowerShell|T1059.001 - PowerShell]]'
- '[[Python|T1059.006 - Python]]'
- '[[Visual Basic|T1059.005 - Visual Basic]]'
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Bypass tag blacklist]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Exotic Payloads for Bypassing Tag Blacklist in Cross Site Scripting Attacks

## Summary

Exotic payloads are used to bypass tag blacklist filters in Cross Site Scripting (XSS) attacks. An attacker can use these payloads to evade detection and execute malicious scripts on a victim's browser. The technical explanation is that the attacker crafts a payload that is not recognized by the fi

## Description

# Description

Exotic payloads are used to bypass tag blacklist filters in Cross Site Scripting (XSS) attacks. An attacker can use these payloads to evade detection and execute malicious scripts on a victim's browser. The technical explanation is that the attacker crafts a payload that is not recognized by the filter and can bypass it. The business value of this attack is that an attacker can steal sensitive information, such as login credentials or personal data, from the victim's browser.

 

## Requirements

1. Access to a vulnerable web application

 

## Defense

1. Implement input validation and output encoding on web application inputs to prevent XSS attacks

1. Use a Content Security Policy (CSP) to restrict the types of content that can be loaded on a web page

1. Educate users on how to identify and avoid phishing attacks that may lead to XSS attacks

 

## Objectives

1. Execute malicious scripts on a victim's browser

1. Steal sensitive information from the victim's browser

 

# Instructions

1. To execute this script, simply inject it into a vulnerable web page using a web vulnerability scanner or by manually modifying the page's HTML code. Once injected, the script will execute and display an alert message with the text 'XSS'.

 



**Code**: [[<script x>
<script x>alert('XSS')<script y>]]



> This JSON object contains an example of an XSS attack script. The 'data' field contains the actual script code, which is designed to exploit a web page vulnerability and execute malicious code on the user's browser. The 'lang' field specifies that the script is written in JavaScript. The 'instruction' field provides guidance on how to use this script to perform an XSS attack. The 'explain' field provides additional information about the purpose and function of this script.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[PowerShell|T1059.001 - PowerShell]]
- [[Python|T1059.006 - Python]]
- [[Visual Basic|T1059.005 - Visual Basic]]
- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Bypass tag blacklist]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


