---
id: a71b608c-40e0-4150-b2a1-c81eaea441c4
name: Cross Site Scripting - Javascript Keylogger
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.729605+00:00'
updated_at: '2023-04-10T20:21:46.399936+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Cross Site Scripting]]'
- '[[Exploit code or POC]]'
- '[[Javascript keylogger]]'
---

# Cross Site Scripting - Javascript Keylogger

## Summary

Cross Site Scripting (XSS) is a type of vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. In this case, the attacker is using a Javascript keylogger to capture keystrokes entered by the victim. This can lead to the theft of sensitive information s

## Description

# Description

Cross Site Scripting (XSS) is a type of vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. In this case, the attacker is using a Javascript keylogger to capture keystrokes entered by the victim. This can lead to the theft of sensitive information such as login credentials, credit card numbers, and other personal data. From an offensive perspective, this technique can be used to gain access to sensitive data and compromise user accounts. From a technical standpoint, the attacker is exploiting a vulnerability in the web application to inject the malicious script. From a business perspective, this type of attack can result in reputational damage, legal liability, and financial losses.

 

## Requirements

1. Access to a vulnerable web application

1. Ability to inject malicious Javascript code

 

## Defense

1. Implement input validation to prevent injection attacks

1. Use content security policies to restrict the sources of executable scripts

1. Monitor network traffic for suspicious activity and implement anomaly detection mechanisms

 

## Objectives

1. Capture keystrokes entered by the victim

1. Steal sensitive information such as login credentials and credit card numbers

 

# Instructions

1. To use this keylogger, simply add the provided code to an image tag's 'onerror' attribute. Once the image fails to load, the keylogger will begin collecting and sending all keystrokes to the specified URL.

 



**Code**: [[<img src=x onerror='document.onkeypress=function(e]]



> This command uses a JavaScript keylogger to collect sensitive data by intercepting and sending all keystrokes to a specified URL. The keylogger is activated when an image fails to load, triggering the 'onerror' attribute which contains the keylogging code. This method can be used to collect passwords, credit card numbers, and other sensitive information entered by the user.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Cross Site Scripting]]
- [[Exploit code or POC]]
- [[Javascript keylogger]]


