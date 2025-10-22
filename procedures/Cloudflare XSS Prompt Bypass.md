---
id: 8c691c95-8c33-462f-bbd6-21b19f8fd238
name: Cloudflare XSS Prompt Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.393499+00:00'
updated_at: '2023-04-10T20:21:56.617683+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Password Policy Discovery|T1201 - Password Policy Discovery]]'
tags:
- '[[3rd June 2019]]'
- '[[Cloudflare XSS Bypasses by [@Bohdan Korzhynskyi](https://twitter.com/bohdansec)]]'
- '[[Common WAF Bypass]]'
- '[[Cross Site Scripting]]'
---

# Cloudflare XSS Prompt Bypass

## Summary

This procedure involves using the XSS Prompt Command to bypass Cloudflare's XSS protection. This technique is used to evade detection and execute malicious code on a target system. The XSS Prompt Command allows an attacker to bypass the Cloudflare WAF by prompting the user to enter a payload that w

## Description

# Description

This procedure involves using the XSS Prompt Command to bypass Cloudflare's XSS protection. This technique is used to evade detection and execute malicious code on a target system. The XSS Prompt Command allows an attacker to bypass the Cloudflare WAF by prompting the user to enter a payload that will bypass the protection. This technique is highly effective and can be used to gain access to sensitive information or to execute unauthorized code.

## Requirements

1. Access to a target system

1. Knowledge of the target system's vulnerabilities

1. Ability to execute the XSS Prompt Command

## Defense

1. Implement strict input validation and sanitization to prevent malicious code injection

1. Regularly update and patch software to prevent known vulnerabilities

1. Implement a WAF that can detect and block XSS attacks

## Objectives

1. Bypass Cloudflare's XSS protection

1. Execute malicious code on a target system

1. Gain access to sensitive information

# Instructions

1. This command is used for Cross-Site Scripting (XSS) attacks. It prompts the user for input and executes the code with the user's input as a parameter.

**Code**: [[<svg onload=prompt%26%230000000040document.domain)]]

> The 'onload' attribute of the 'svg' tag is used to execute the 'prompt' function. The function is called with the 'document.domain' parameter, which will prompt the user to enter a value. The entered value will be executed as JavaScript code. The 'iframe' tag is used to load the entered value as 'srcdoc' attribute, which will execute the code within the tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Password Policy Discovery|T1201 - Password Policy Discovery]]

## Tags

- [[3rd June 2019]]
- [[Cloudflare XSS Bypasses by [@Bohdan Korzhynskyi](https://twitter.com/bohdansec)]]
- [[Common WAF Bypass]]
- [[Cross Site Scripting]]
