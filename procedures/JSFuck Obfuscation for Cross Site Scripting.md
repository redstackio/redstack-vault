---
id: 81070ae6-4695-45ee-825b-4502c86c2a5d
name: JSFuck Obfuscation for Cross Site Scripting
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.169586+00:00'
updated_at: '2023-04-10T20:21:33.937827+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Bypass using jsfuck]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# JSFuck Obfuscation for Cross Site Scripting

## Summary

JSFuck is a technique that allows attackers to obfuscate their JavaScript payloads in a way that bypasses certain filters and detection mechanisms. This can be particularly useful in the context of Cross Site Scripting (XSS) attacks, where the attacker wants to inject malicious JavaScript code into

## Description

# Description

JSFuck is a technique that allows attackers to obfuscate their JavaScript payloads in a way that bypasses certain filters and detection mechanisms. This can be particularly useful in the context of Cross Site Scripting (XSS) attacks, where the attacker wants to inject malicious JavaScript code into a vulnerable web page. By using JSFuck, the attacker can make it more difficult for defenders to detect and block their payload.

From a technical perspective, JSFuck works by using a limited set of characters and operators to represent all of the functionality of JavaScript. This allows the attacker to write code that looks like gibberish, but is actually valid JavaScript that can be executed by the browser. This can make it difficult for defenders to distinguish between legitimate and malicious code, and can make it harder to write filters that block the attacker's payload.

From a business perspective, this technique can be used by attackers to steal sensitive information, such as login credentials or personal data, from users of a vulnerable website. By injecting malicious JavaScript code into the website, the attacker can execute arbitrary code in the context of the victim's browser, giving them access to any data that the victim has access to.

## Requirements

1. Access to a vulnerable web page with a Cross Site Scripting vulnerability

1. Knowledge of JavaScript and JSFuck obfuscation techniques

## Defense

1. Implement input validation and output encoding to prevent Cross Site Scripting vulnerabilities

1. Use a web application firewall (WAF) to block known JSFuck payloads

1. Regularly scan web applications for vulnerabilities and apply patches as needed

## Objectives

1. Inject malicious JavaScript code into a vulnerable web page

1. Bypass filters and detection mechanisms

1. Steal sensitive information from users of the vulnerable website

# Instructions

1. Copy and paste the jsfuck code into the browser console and execute it to bypass any JavaScript filters

**Code**: [[[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+]]

> JSFuck is an esoteric and educational programming style based on the atomic parts of JavaScript. It uses only six different characters to write and execute code. This technique can be used to bypass JavaScript filters that are in place to protect against malicious code.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Tags

- [[Bypass using jsfuck]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]
