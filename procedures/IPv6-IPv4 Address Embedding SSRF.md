---
id: 268ab2dd-8962-41f3-9375-b4cc7f39dd2c
name: IPv6/IPv4 Address Embedding SSRF
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.421022+00:00'
updated_at: '2023-04-10T20:24:15.495587+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Bypassing filters]]'
- '[[Bypass using IPv6/IPv4 Address Embedding]]'
- '[[Server-Side Request Forgery]]'
commands:
- '[[URL Validation]]'
---

# IPv6/IPv4 Address Embedding SSRF

## Summary

IPv6/IPv4 Address Embedding is a technique used to bypass filters in Server-Side Request Forgery attacks. This technique involves encoding an IPv4 address within an IPv6 address by embedding the IPv4 address within the last 32 bits of the IPv6 address. This can be used to bypass filters that block 

## Description

# Description

IPv6/IPv4 Address Embedding is a technique used to bypass filters in Server-Side Request Forgery attacks. This technique involves encoding an IPv4 address within an IPv6 address by embedding the IPv4 address within the last 32 bits of the IPv6 address. This can be used to bypass filters that block IPv4 addresses but allow IPv6 addresses. Attackers can use this technique to exploit vulnerable web applications and gain unauthorized access to internal resources. The business value of this technique is that it can be used to bypass network security measures and gain access to sensitive information.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of IPv6/IPv4 Address Embedding technique

 

## Defense

1. Implement input validation to prevent SSRF attacks

1. Use a web application firewall to detect and block SSRF attacks

1. Restrict network access to vulnerable web applications

 

## Objectives

1. Exploit vulnerable web applications

1. Gain unauthorized access to internal resources

 

# Instructions

1. Use this URL to access the localhost server on your machine.

 



**Code**: [[http://[0:0:0:0:0:ffff:127.0.0.1]]]



> The URL provided is used to access the localhost server on your machine. This is useful for testing and development purposes when you need to access a local server on your machine. The IP address 127.0.0.1 is the loopback address that always points to your own machine. By using this URL, you can test your server without needing to deploy it to a remote server or hosting service.



**Command** ([[URL Validation]]):

```bash
http://[0:0:0:0:0:ffff:127.0.0.1]
```



## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Commands Used

- [[URL Validation]]

## Tags

- [[Bypassing filters]]
- [[Bypass using IPv6/IPv4 Address Embedding]]
- [[Server-Side Request Forgery]]


