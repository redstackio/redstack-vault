---
id: 16126e3b-de51-4d40-a4cf-a3cd7b76d6ff
name: Filter Bypass with Exotic Payloads for Cross Site Scripting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.577470+00:00'
updated_at: '2023-04-10T20:21:36.019997+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Install Root Certificate|T1130 - Install Root Certificate]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Bypass onxxxx= blacklist]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Filter Bypass with Exotic Payloads for Cross Site Scripting

## Summary

Cross Site Scripting (XSS) is a type of web vulnerability that allows an attacker to inject malicious code into a web page viewed by other users. This procedure focuses on bypassing filters that are in place to prevent XSS attacks by using exotic payloads that can evade detection. The attacker can 

## Description

# Description

Cross Site Scripting (XSS) is a type of web vulnerability that allows an attacker to inject malicious code into a web page viewed by other users. This procedure focuses on bypassing filters that are in place to prevent XSS attacks by using exotic payloads that can evade detection. The attacker can use this technique to execute arbitrary code on the victim's browser, steal user credentials, or perform other malicious actions. The technical explanation involves crafting payloads that can bypass filters and execute JavaScript code. The business value of this procedure is that it allows an attacker to gain access to sensitive user information, which can be used for financial gain or other malicious purposes.

## Requirements

1. Ability to inject payloads into a web page

1. Knowledge of exotic payloads that can bypass filters

## Defense

1. Implement input validation to prevent the injection of malicious code

1. Use Content Security Policy (CSP) to restrict the types of content that can be loaded on a web page

1. Regularly update web application firewalls to detect and block new types of attacks

## Objectives

1. Bypass filters that are in place to prevent XSS attacks

1. Inject malicious code into a web page viewed by other users

1. Execute arbitrary code on the victim's browser

1. Steal user credentials or perform other malicious actions

# Instructions

1. To bypass onxxx= filter in JavaScript, use a null byte/vertical tab or a '/' in the onerror attribute of an image tag.

**Code**: [[<object onafterscriptexecute=confirm(0)>
<object o]]

> The onxxx= filter in JavaScript is used to prevent certain events from being triggered, such as onerror. However, this filter can be bypassed by using a null byte/vertical tab or a '/' in the onerror attribute of an image tag. This allows the onerror event to be triggered, even with the filter in place.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Install Root Certificate|T1130 - Install Root Certificate]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Tags

- [[Bypass onxxxx= blacklist]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
