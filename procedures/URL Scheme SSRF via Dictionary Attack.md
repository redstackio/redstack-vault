---
id: a1efe8b2-fb7a-439a-91a7-2b2586a6da71
name: URL Scheme SSRF via Dictionary Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.820400+00:00'
updated_at: '2023-04-10T20:24:12.841115+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Dict]]'
- '[[Server-Side Request Forgery]]'
- '[[SSRF exploitation via URL Scheme]]'
---

# URL Scheme SSRF via Dictionary Attack

## Summary

A URL Scheme SSRF attack is a technique where an attacker can exploit a vulnerability in a web application to make it send a request to a URL controlled by the attacker. The attacker can then use this to bypass security controls and access resources that are not normally accessible. In this case, t

## Description

# Description

A URL Scheme SSRF attack is a technique where an attacker can exploit a vulnerability in a web application to make it send a request to a URL controlled by the attacker. The attacker can then use this to bypass security controls and access resources that are not normally accessible. In this case, the attacker is using a dictionary attack to try a large number of URLs in the hopes of finding one that is vulnerable to SSRF. This attack can be used by an attacker to gain access to sensitive data or to take control of a system.

To carry out this attack, the attacker needs to have access to the web application and knowledge of the URL scheme being used. They can then use a tool to automate the process of trying different URLs until they find one that is vulnerable. This attack can be difficult to detect as it looks like normal traffic to the web application.

The business value of this attack is that an attacker can gain access to sensitive data or take control of a system, which can lead to financial loss or damage to reputation.

 

## Requirements

1. Access to the web application

1. Knowledge of the URL scheme being used

1. A tool to automate the process of trying different URLs

 

## Defense

1. Implement input validation on the web application to prevent SSRF attacks

1. Use a web application firewall to detect and block SSRF attacks

1. Monitor network traffic for suspicious activity

 

## Objectives

1. To gain access to sensitive data

1. To take control of a system

 

# Instructions

1. Use this command to perform a dictionary attack on a target using the Dictionary protocol.

 



**Code**: [[dict://<user>;<auth>@<host>:<port>/d:<word>:<datab]]



> This command can be used to perform a dictionary attack on a target using the Dictionary protocol. The 'data' field should be filled in with the necessary parameters for the attack, including the user, authentication, host, port, word, database, and n values. The 'text' field provides a visual representation of what an SSRF stream may look like. The 'instruction' field provides guidance on how to use this command, while the 'explain' field provides additional information on the purpose and functionality of the command.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Tags

- [[Dict]]
- [[Server-Side Request Forgery]]
- [[SSRF exploitation via URL Scheme]]


