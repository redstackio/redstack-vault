---
id: ecb3f6c4-feae-41e5-b184-1be9518e4026
name: Cloudflare XSS Bypass via SVG Onload Alert
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.346853+00:00'
updated_at: '2023-04-10T20:21:53.022762+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Group Policy Modification|T1484 - Group Policy Modification]]'
tags:
- '[[22nd August 2019]]'
- '[[Cloudflare XSS Bypasses by [@Bohdan Korzhynskyi](https://twitter.com/bohdansec)]]'
- '[[Common WAF Bypass]]'
- '[[Cross Site Scripting]]'
---

# Cloudflare XSS Bypass via SVG Onload Alert

## Summary

Cloudflare is a popular web application firewall (WAF) used to protect websites and web applications from attacks. However, it's not infallible and can be bypassed in certain scenarios. One such scenario is when an attacker can inject malicious code, such as a cross-site scripting (XSS) payload, in

## Description

# Description

Cloudflare is a popular web application firewall (WAF) used to protect websites and web applications from attacks. However, it's not infallible and can be bypassed in certain scenarios. One such scenario is when an attacker can inject malicious code, such as a cross-site scripting (XSS) payload, into a web page. This can be done via various vectors, including a specially crafted SVG image. By using the SVG Onload Alert command, an attacker can execute arbitrary JavaScript code on the victim's browser, bypassing the Cloudflare WAF and potentially compromising sensitive data. This technique can be used for various malicious purposes, such as stealing credentials, spreading malware or ransomware, or conducting further attacks.

## Requirements

1. Ability to inject malicious code into a web page

1. Knowledge of the SVG Onload Alert command

1. Access to a web page protected by Cloudflare WAF

## Defense

1. Use input validation and sanitization techniques to prevent injection attacks

1. Implement Content Security Policy (CSP) to restrict the sources of content that can be loaded by a web page

1. Regularly update and patch web servers and web applications to prevent known vulnerabilities

## Objectives

1. Inject a malicious payload into a web page via an SVG image

1. Bypass the Cloudflare WAF to execute arbitrary JavaScript code on the victim's browser

1. Potentially compromise sensitive data, steal credentials, spread malware or ransomware, or conduct further attacks

# Instructions

1. The SVG Onload Alert Command is a malicious code injection attack that exploits a vulnerability in SVG images. When an SVG image containing this code is loaded, it executes the alert function with the message 'bohdan'.

**Code**: [[<svg/onload=%26nbsp;alert`bohdan`+]]

> The 'onload' attribute in SVG is used to specify a script to be run when the image is loaded. In this case, the script contains the 'alert' function which displays a pop-up message with the text 'bohdan'. This command can be used by attackers to steal sensitive information or install malware on a user's computer.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Group Policy Modification|T1484 - Group Policy Modification]]

## Tags

- [[22nd August 2019]]
- [[Cloudflare XSS Bypasses by [@Bohdan Korzhynskyi](https://twitter.com/bohdansec)]]
- [[Common WAF Bypass]]
- [[Cross Site Scripting]]
