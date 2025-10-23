---
id: f71fd21a-1581-4f29-a23e-669af0fa55a7
name: Incapsula WAF Bypass via Common Cross-Site Scripting (XSS) Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.480594+00:00'
updated_at: '2023-04-10T20:21:53.368069+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]'
tags:
- '[[Common WAF Bypass]]'
- '[[Cross Site Scripting]]'
- '[[Incapsula WAF Bypass by [@Alra3ees](https://twitter.com/Alra3ees/status/971847839931338752)-
  8th March 2018]]'
---

# Incapsula WAF Bypass via Common Cross-Site Scripting (XSS) Attack

## Summary

The Incapsula WAF Bypass via Common Cross-Site Scripting (XSS) Attack is a technique used by attackers to bypass the Incapsula Web Application Firewall (WAF). This attack is performed by exploiting a common Cross-Site Scripting (XSS) vulnerability in the target application, which allows the attacke

## Description

# Description

The Incapsula WAF Bypass via Common Cross-Site Scripting (XSS) Attack is a technique used by attackers to bypass the Incapsula Web Application Firewall (WAF). This attack is performed by exploiting a common Cross-Site Scripting (XSS) vulnerability in the target application, which allows the attacker to inject malicious code into the application. The malicious code can then be used to bypass the Incapsula WAF and perform unauthorized actions on the target system.

From a technical perspective, this attack works by using the XSS vulnerability to inject a payload that bypasses the Incapsula WAF. The payload is designed to evade detection by the WAF and execute the desired actions on the target system. This technique can be used to steal sensitive data, perform unauthorized actions, or gain access to the target system.

The business value of this attack is that it allows attackers to bypass the Incapsula WAF and perform unauthorized actions on the target system. This can lead to data theft, system compromise, and other serious security incidents.

 

## Requirements

1. Access to the target application

1. Knowledge of the XSS vulnerability

 

## Defense

1. Regularly scan for and patch XSS vulnerabilities

1. Implement strict input validation and output encoding to prevent XSS attacks

1. Use a combination of WAF and other security measures to protect against attacks

 

## Objectives

1. Bypass Incapsula WAF

1. Perform unauthorized actions on target system

 

# Instructions

1. The Cross-Site Scripting (XSS) attack is a type of security vulnerability that allows an attacker to inject malicious code into a web page viewed by other users. This code can be used to steal sensitive information, such as login credentials or personal data, or to perform other malicious actions. To prevent XSS attacks, it is important to properly validate and sanitize user input on both the client and server sides.

 



**Code**: [[anythinglr00</script><script>alert(document.domain]]



> In this example, the attacker has injected JavaScript code into the 'c1' parameter of the URL, which is then executed by the victim's browser. The code in this example displays an alert box containing the domain of the current page, but it could just as easily be used to steal cookies or perform other malicious actions. To prevent this type of attack, developers should always validate and sanitize user input before displaying it on a web page, and use security measures such as Content Security Policy (CSP) to limit the types of content that can be executed on a page.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Use Alternate Authentication Material|T1550 - Use Alternate Authentication Material]]

## Tags

- [[Common WAF Bypass]]
- [[Cross Site Scripting]]
- [[Incapsula WAF Bypass by [@Alra3ees](https://twitter.com/Alra3ees/status/971847839931338752)- 8th March 2018]]


