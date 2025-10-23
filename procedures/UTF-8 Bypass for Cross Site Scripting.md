---
id: 6210f9ff-fc1c-48a6-9374-03978b32f6a3
name: UTF-8 Bypass for Cross Site Scripting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.057088+00:00'
updated_at: '2023-04-10T20:21:30.561332+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Indicator Removal from Tools|T1066 - Indicator Removal from Tools]]'
tags:
- '[[Bypass using UTF-8]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# UTF-8 Bypass for Cross Site Scripting

## Summary

This procedure is used to bypass input validation filters and inject malicious scripts into a web application, allowing an attacker to execute arbitrary code in a victim's browser. The attack can be carried out by encoding special characters using UTF-8 encoding, which can bypass certain input vali

## Description

# Description

This procedure is used to bypass input validation filters and inject malicious scripts into a web application, allowing an attacker to execute arbitrary code in a victim's browser. The attack can be carried out by encoding special characters using UTF-8 encoding, which can bypass certain input validation filters. This technique is commonly used in cross-site scripting (XSS) attacks where an attacker can steal sensitive information, execute malicious code, or perform other unauthorized actions on a victim's behalf. By encoding special characters, an attacker can bypass input validation filters and inject malicious scripts into a web application.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of special character encoding using UTF-8

1. Ability to execute JavaScript code

 

## Defense

1. Implement input validation techniques to prevent XSS attacks

1. Use Content Security Policy (CSP) to restrict the types of content that can be loaded on a web page

1. Implement encoding and decoding techniques to prevent malicious scripts from being executed

 

## Objectives

1. Inject malicious scripts into a web application

1. Execute arbitrary code in a victim's browser

1. Steal sensitive information from a victim's browser

 

# Instructions

1. To encode special characters in JavaScript, use the following format: '%XX' where XX is the hexadecimal representation of the character code. For characters that require more than two bytes, use the corresponding UTF-8 encoding. For example, the character '<' can be encoded as '%3C' or '%C0%BC' or '%E0%80%BC' or '%F0%80%80%BC', depending on the encoding used. Similarly, the character '"' can be encoded as '%22' or '%C0%A2' or '%E0%80%A2' or '%F0%80%80%A2' or '%CA%BA', and the character ''' can be encoded as '%27' or '%C0%A7' or '%E0%80%A7' or '%F0%80%80%A7' or '%CA%B9'.

 



**Code**: [[< = %C0%BC = %E0%80%BC = %F0%80%80%BC
> = %C0%BE =]]



> This JSON object provides the encoding for special characters in JavaScript, along with the corresponding UTF-8 encoding for characters that require more than two bytes. The 'data' field contains the special characters and their encodings, while the 'instruction' field provides instructions on how to use this encoding in JavaScript. The 'lang' field specifies the language for which this encoding is applicable, and the 'text' and 'explain' fields are not used in this object.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Indicator Removal from Tools|T1066 - Indicator Removal from Tools]]

## Tags

- [[Bypass using UTF-8]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


