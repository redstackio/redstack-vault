---
id: 96157cad-182b-49bb-8bfa-45cabb942cd6
name: Domain Redirection SSRF
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.330097+00:00'
updated_at: '2023-04-10T20:24:12.051464+00:00'
tags:
- '[[Bypassing filters]]'
- '[[Bypass localhost with a domain redirection]]'
- '[[Server-Side Request Forgery]]'
commands:
- '[[NIP.IO Mapping]]'
---

# Domain Redirection SSRF

## Summary

Domain Redirection SSRF is a technique used to bypass filters and exploit Server-Side Request Forgery vulnerabilities. This technique involves redirecting requests from localhost to a domain that resolves to the attacker's IP address. This can be achieved by using a service like NIP.IO to map a dom

## Description

# Description

Domain Redirection SSRF is a technique used to bypass filters and exploit Server-Side Request Forgery vulnerabilities. This technique involves redirecting requests from localhost to a domain that resolves to the attacker's IP address. This can be achieved by using a service like NIP.IO to map a domain name to the attacker's IP address. By using a domain name instead of an IP address, the request can bypass filters that block requests to IP addresses. This technique can be used to exfiltrate data, perform reconnaissance, or even execute arbitrary code on the vulnerable server.

From a technical standpoint, this technique takes advantage of the fact that many SSRF filters only block requests to IP addresses, not domain names. By redirecting requests to a domain name that resolves to the attacker's IP address, the attacker can bypass these filters and execute their attack. 

Business value of this technique is that it can be used to gain unauthorized access to sensitive data, such as customer information, financial data, or intellectual property. It can also be used to launch further attacks against the target organization, such as lateral movement or privilege escalation.

 

## Requirements

1. Access to a vulnerable server with a SSRF vulnerability

1. Ability to redirect requests to a domain that resolves to the attacker's IP address

1. Knowledge of NIP.IO or similar services

 

## Defense

1. Implement input validation and sanitization to prevent SSRF vulnerabilities

1. Block requests to external domains or IP addresses at the firewall or network level

1. Implement access controls and authentication to prevent unauthorized access to sensitive data

 

## Objectives

1. Bypass filters and exploit SSRF vulnerabilities

1. Exfiltrate data, perform reconnaissance, or execute arbitrary code on the vulnerable server

 

# Instructions

1. To use NIP.IO for DNS mapping, simply append the desired hostname to the IP address you want to map, followed by .nip.io. For example, to map the IP address 192.168.0.1 to the hostname myserver.nip.io, you would use the DNS name 192.168.0.1.myserver.nip.io.

 



**Code**: [[NIP.IO maps <anything>.<IP Address>.nip.io to the ]]



> The NIP.IO service allows for easy DNS mapping of IP addresses without the need for a dedicated DNS server. This can be useful in situations where you need to access a server by hostname, but do not have a DNS server available or do not want to set up DNS for a small network. The service works by interpreting the hostname as a subdomain of the IP address, and returning the IP address as the DNS resolution for that hostname.



**Command** ([[NIP.IO Mapping]]):

```bash
127.0.0.1.nip.io
```



## Commands Used

- [[NIP.IO Mapping]]

## Tags

- [[Bypassing filters]]
- [[Bypass localhost with a domain redirection]]
- [[Server-Side Request Forgery]]


