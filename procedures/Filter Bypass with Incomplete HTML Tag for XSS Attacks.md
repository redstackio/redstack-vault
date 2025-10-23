---
id: f296e1af-922d-4985-a0a2-d9c4a9262b09
name: Filter Bypass with Incomplete HTML Tag for XSS Attacks
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:42.401403+00:00'
updated_at: '2023-04-10T20:21:49.532695+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Bootkit|T1067 - Bootkit]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
tags:
- '[[Bypass with incomplete html tag]]'
- '[[Cross Site Scripting]]'
- '[[Filter Bypass and exotic payloads]]'
---

# Filter Bypass with Incomplete HTML Tag for XSS Attacks

## Summary

Filter Bypass with Incomplete HTML Tag is a technique used to bypass input filters that are designed to prevent Cross-Site Scripting (XSS) attacks. This technique involves inserting an incomplete HTML tag into the input field, which causes the filter to fail and allows the attacker to inject malici

## Description

# Description

Filter Bypass with Incomplete HTML Tag is a technique used to bypass input filters that are designed to prevent Cross-Site Scripting (XSS) attacks. This technique involves inserting an incomplete HTML tag into the input field, which causes the filter to fail and allows the attacker to inject malicious JavaScript code into the web page. This technique is effective against filters that only check for complete HTML tags, and can be used to execute arbitrary code on the victim's browser.

From an offensive perspective, this technique can be used to steal sensitive information such as login credentials, session tokens, and personal data. It can also be used to perform actions on behalf of the victim, such as making unauthorized purchases or sending malicious emails. From a technical standpoint, this technique relies on the fact that some input filters are not designed to handle incomplete HTML tags, which can be exploited by the attacker to bypass the filter and inject malicious code into the web page. From a business perspective, this technique can result in reputational damage, loss of revenue, and legal liability for organizations that fail to protect their web applications from XSS attacks.

 

## Requirements

1. Access to a vulnerable web application with input filters that are not designed to handle incomplete HTML tags

 

## Defense

1. Implement strict input validation and filtering mechanisms to prevent the insertion of incomplete HTML tags

1. Use Content Security Policy (CSP) to restrict the execution of untrusted JavaScript code

1. Educate users and developers about the risks of XSS attacks and how to prevent them

 

## Objectives

1. Inject and execute malicious JavaScript code on the victim's browser

1. Steal sensitive information such as login credentials and personal data

1. Perform actions on behalf of the victim, such as making unauthorized purchases or sending malicious emails

 

# Instructions

1. To prevent Cross-Site Scripting (XSS) attacks, make sure to properly sanitize and validate all user input. Additionally, use Content Security Policy (CSP) to restrict the sources of content that can be loaded by your web application.

 



**Code**: [[<img src='1' onerror='alert(0)' <]]



> The 'onerror' attribute in the provided code is a common technique used by attackers to inject malicious code into a web page. By properly sanitizing and validating user input, you can prevent these types of attacks. CSP is an additional layer of security that can be used to restrict the sources of content that can be loaded by your web application, further reducing the risk of XSS attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Bootkit|T1067 - Bootkit]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]

## Tags

- [[Bypass with incomplete html tag]]
- [[Cross Site Scripting]]
- [[Filter Bypass and exotic payloads]]


