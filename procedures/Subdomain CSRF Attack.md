---
id: 5b23425a-8211-4a61-868e-20e3beab5696
name: Subdomain CSRF Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:55.682795+00:00'
updated_at: '2023-04-06T03:55:55.692985+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Impact|TA0040 - Impact]]'
techniques:
- '[[Control Panel Items|T1196 - Control Panel Items]]'
- '[[Endpoint Denial of Service|T1499 - Endpoint Denial of Service]]'
tags:
- '[[Bypass referer header validation]]'
- '[[Cross-Site Request Forgery]]'
- '[[With subdomain payload]]'
commands:
- '[[Modify Referer header with subdomain payload]]'
---

# Subdomain CSRF Attack

## Summary

A Subdomain CSRF attack is a type of attack where an attacker can execute unauthorized actions on a website on behalf of an authenticated user. This attack is possible when a subdomain is not properly configured and has been taken over by the attacker. By crafting a malicious payload and including 

## Description

# Description

A Subdomain CSRF attack is a type of attack where an attacker can execute unauthorized actions on a website on behalf of an authenticated user. This attack is possible when a subdomain is not properly configured and has been taken over by the attacker. By crafting a malicious payload and including it in the Referer header, an attacker can bypass referer header validation and trick the server into executing the unauthorized actions. This attack can result in data theft, account takeover, and other serious consequences. From an offensive perspective, this attack can be used to gain access to sensitive data or to take over user accounts.

 

## Requirements

1. Access to a subdomain that has not been properly configured.

1. Ability to craft a malicious payload.

1. Ability to include the payload in the Referer header.

 

## Defense

1. Properly configure subdomains to prevent subdomain takeover.

1. Implement referer header validation to prevent unauthorized actions.

1. Use multi-factor authentication to prevent account takeover.

 

## Objectives

1. To execute unauthorized actions on a website on behalf of an authenticated user.

1. To gain access to sensitive data.

1. To take over user accounts.

 

# Instructions

1. To execute the Subdomain CSRF Attack, follow these steps:

 

Step 1 - Open the target website in the browser.
Step 2 - Modify the Referer header to include the subdomain payload.



**Command** ([[Modify Referer header with subdomain payload]]):

```bash
Open https://trusted.domain.com.attacker.com/csrf.html
The Referer header is modified to include the subdomain payload.

Referer: https://trusted.domain.com.attacker.com/csrf.html
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Impact|TA0040 - Impact]]

### Techniques

- [[Control Panel Items|T1196 - Control Panel Items]]
- [[Endpoint Denial of Service|T1499 - Endpoint Denial of Service]]

## Commands Used

- [[Modify Referer header with subdomain payload]]

## Tags

- [[Bypass referer header validation]]
- [[Cross-Site Request Forgery]]
- [[With subdomain payload]]


