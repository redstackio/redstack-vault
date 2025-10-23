---
id: c288905d-f95e-48e7-bce9-2268cdece4c5
name: Filter Bypass with Exotic Payloads for Case Sensitive XSS
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.321398+00:00'
updated_at: '2023-04-10T20:21:39.528380+00:00'
tags:
- '[[Bypass case sensitive]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Filter Bypass with Exotic Payloads for Case Sensitive XSS

## Summary

This procedure is used to bypass filters that are designed to prevent Cross Site Scripting (XSS) attacks. The attacker uses exotic payloads to evade the filters and inject malicious scripts into a vulnerable web application. In this case, the attacker is targeting a case sensitive filter. The attac

## Description

# Description

This procedure is used to bypass filters that are designed to prevent Cross Site Scripting (XSS) attacks. The attacker uses exotic payloads to evade the filters and inject malicious scripts into a vulnerable web application. In this case, the attacker is targeting a case sensitive filter. The attacker can use various techniques to bypass the filter, such as encoding the payload or using a different character set. The business value of this attack is to gain unauthorized access to sensitive information, such as user credentials or personal data.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of the filter being used

1. Ability to craft exotic payloads

 

## Defense

1. Implement input validation and output encoding to prevent XSS attacks

1. Use a web application firewall (WAF) to detect and block malicious traffic

1. Regularly update and patch the web application and server software to prevent known vulnerabilities

 

## Objectives

1. Inject malicious scripts into a vulnerable web application

1. Bypass the case sensitive filter

1. Gain unauthorized access to sensitive information

 

# Instructions

1. Use encoding techniques to prevent Cross-Site Scripting (XSS) attacks.

 



**Code**: [[<sCrIpt>alert(1)</ScRipt>]]



> XSS attacks occur when an attacker injects malicious code into a web page, which is then executed by unsuspecting users who visit the page. To prevent XSS attacks, it is important to properly encode user input before displaying it on a web page. This can be done using encoding techniques such as HTML encoding, JavaScript encoding, and URL encoding. By encoding user input, special characters are converted to their corresponding HTML entities, preventing them from being interpreted as code by the browser. Additionally, it is important to sanitize user input by removing any potentially harmful characters or scripts before displaying it on a web page.

## Tags

- [[Bypass case sensitive]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


