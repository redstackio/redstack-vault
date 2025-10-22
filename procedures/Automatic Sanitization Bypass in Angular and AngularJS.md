---
id: 90371963-b4e8-46d4-b1fa-3b524dbea002
name: Automatic Sanitization Bypass in Angular and AngularJS
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:43.801708+00:00'
updated_at: '2023-04-10T20:24:52.243088+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Regsvr32|T1117 - Regsvr32]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Automatic Sanitization]]'
- '[[XSS in Angular and AngularJS]]'
commands:
- '[[Sanitize URL]]'
---

# Automatic Sanitization Bypass in Angular and AngularJS

## Summary

This procedure exploits a vulnerability in Angular and AngularJS that allows an attacker to bypass automatic sanitization of user input. This vulnerability can be used to inject malicious scripts into web pages, which can then be executed in the context of the victim's browser. This can be used to 

## Description

# Description

This procedure exploits a vulnerability in Angular and AngularJS that allows an attacker to bypass automatic sanitization of user input. This vulnerability can be used to inject malicious scripts into web pages, which can then be executed in the context of the victim's browser. This can be used to steal sensitive information, such as login credentials, or to perform actions on behalf of the victim.

The technical explanation of this procedure involves the use of the 'Bypass Security Trust URL' and 'Angular Security' commands. These commands allow an attacker to bypass the automatic sanitization of user input by Angular and AngularJS. By crafting a specially-crafted URL, an attacker can inject malicious scripts into a web page that will be executed in the context of the victim's browser.

The business value of this procedure is that it allows an attacker to steal sensitive information or perform actions on behalf of the victim. This can lead to financial loss, reputational damage, and legal liability for the victim.

## Requirements

1. Access to a vulnerable version of Angular or AngularJS

1. Ability to craft a specially-crafted URL

## Defense

1. Always use the latest version of Angular or AngularJS

1. Implement input validation and sanitization on the server-side

1. Use Content Security Policy (CSP) to restrict the execution of scripts

## Objectives

1. Inject malicious scripts into web pages

1. Steal sensitive information, such as login credentials

1. Perform actions on behalf of the victim

# Instructions

1. The bypassSecurityTrustUrl method allows you to bypass Angular's built-in security and trust a URL. This is useful when you need to display content from an untrusted source, such as a third-party website or a user-generated URL.

**Code**: [[bypassSecurityTrustUrl]]

> The method takes a single argument, which is the URL you want to trust. This URL will be marked as safe by Angular, meaning that it can be used in an iframe or other context where untrusted content would normally be blocked. However, it's important to note that using this method can introduce security vulnerabilities into your application if you're not careful. Make sure you trust the source of the URL before using this method.

2. To ensure security in Angular, use the DomSanitizer to sanitize untrusted URLs. In this example, the DomSanitizer is injected into the component and used to bypass security for a potentially dangerous URL. The sanitized URL can then be used in the template to create a trusted link.

**Code**: [[import { Component, OnInit } from '@angular/core';]]

> The `DomSanitizer` is a security service that sanitizes and escapes values to prevent cross-site scripting (XSS) attacks. In this example, the `dangerousUrl` is set to a potentially dangerous JavaScript URL that could execute malicious code. To make the URL safe, we pass it through the `DomSanitizer`'s `bypassSecurityTrustUrl` method, which returns a sanitized version of the URL that can be used safely in the template. The sanitized URL is then bound to the `href` attribute of the `<a>` tags in the template, creating trusted links that can be clicked without risk of XSS attacks.

**Command** ([[Sanitize URL]]):

```bash
this.sanitizer.bypassSecurityTrustUrl(this.dangerousUrl)
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Regsvr32|T1117 - Regsvr32]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Commands Used

- [[Sanitize URL]]

## Tags

- [[Automatic Sanitization]]
- [[XSS in Angular and AngularJS]]
