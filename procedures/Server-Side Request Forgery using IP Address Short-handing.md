---
id: a6eec382-5ac1-445c-96b6-28b448039a58
name: Server-Side Request Forgery using IP Address Short-handing
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.466621+00:00'
updated_at: '2023-04-10T20:24:05.350243+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Bypassing filters]]'
- '[[Bypass using rare address]]'
- '[[Server-Side Request Forgery]]'
---

# Server-Side Request Forgery using IP Address Short-handing

## Summary

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to send requests from the server-side application to any domain. In this attack, the attacker can bypass filters by using rare IP address short-handing techniques. This technique can be used to bypass filters that block c

## Description

# Description

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to send requests from the server-side application to any domain. In this attack, the attacker can bypass filters by using rare IP address short-handing techniques. This technique can be used to bypass filters that block certain domains or IP addresses. The attacker can use this to gain access to internal systems or to perform actions on behalf of the server. The business value of this attack is that it can be used to steal sensitive data or to perform unauthorized actions on the server.

## Requirements

1. Access to the server-side application

1. Knowledge of IP address short-handing techniques

## Defense

1. Implement input validation to prevent SSRF attacks

1. Block access to sensitive internal systems

1. Use a Web Application Firewall (WAF) to block malicious requests

## Objectives

1. Gain access to internal systems

1. Perform actions on behalf of the server

# Instructions

1. To shorten an IP address, drop any leading zeros in each octet of the IP address. For example, instead of writing 127.0.0.1, you can simply write 127.1.

**Code**: [[http://0/
http://127.1
http://127.0.1]]

> This is a useful shortcut for writing IP addresses, as it can save time and make the addresses easier to read. However, it's important to note that this shortcut only works for IPv4 addresses, not IPv6 addresses.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[Bypassing filters]]
- [[Bypass using rare address]]
- [[Server-Side Request Forgery]]
