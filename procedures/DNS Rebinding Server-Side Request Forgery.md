---
id: e1a4a31c-0f47-4a11-9073-b87dcf3f7d7d
name: DNS Rebinding Server-Side Request Forgery
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.719322+00:00'
updated_at: '2023-04-10T20:24:13.635405+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
- '[[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Bypassing filters]]'
- '[[Bypassing using DNS Rebinding (TOCTOU)]]'
- '[[Server-Side Request Forgery]]'
commands:
- '[[Create rotating domain with two IPs]]'
---

# DNS Rebinding Server-Side Request Forgery

## Summary

DNS Rebinding Server-Side Request Forgery is a technique used to bypass filters and exploit vulnerabilities in a server to gain unauthorized access. This technique involves exploiting a server-side request forgery vulnerability to make requests to internal systems, and then using DNS rebinding to b

## Description

# Description

DNS Rebinding Server-Side Request Forgery is a technique used to bypass filters and exploit vulnerabilities in a server to gain unauthorized access. This technique involves exploiting a server-side request forgery vulnerability to make requests to internal systems, and then using DNS rebinding to bypass any filters or firewalls that are in place. By creating a domain name that resolves to an internal IP address, an attacker can use the victim's browser to make requests to internal systems, effectively bypassing any security measures that are in place.

This technique can be used to gain access to sensitive data, such as customer information or financial data. It can also be used to compromise the entire network, as an attacker can use the compromised server to launch further attacks.

 

## Requirements

1. Access to a vulnerable server

1. Ability to create a domain name that resolves to an internal IP address

1. Victim's browser must be used to make requests to internal systems

 

## Defense

1. Use a web application firewall that can detect and block server-side request forgery attacks

1. Ensure that internal systems are not accessible from the public internet

1. Use DNS filtering to block requests to known malicious domains

 

## Objectives

1. Gain unauthorized access to internal systems

1. Bypass filters and firewalls

1. Steal sensitive data

1. Compromise the entire network

 

# Instructions

1. To create a rotating IP domain, follow these steps:
1. Visit http://1u.ms/.
2. Enter the IPs you want to rotate between in the format 'make-IP1-rebind-IP2-rr.1u.ms'.
3. Save the generated domain name for use in your application.
Note: The IPs must be separated by '-rebind-' and the domain must end with '-rr.1u.ms'.

 



**Code**: [[Create a domain that rotates between two IPs. For ]]



> The 'make' keyword in the domain name indicates that this is a rotating IP domain. The first IP specified before '-rebind-' is the initial IP that will be used. The second IP specified after '-rebind-' is the IP that will be used after the initial IP. The '-rr' at the end of the domain name indicates that the rotation should be round-robin, meaning that the IPs will be used in alternating order.



**Command** ([[Create rotating domain with two IPs]]):

```bash
make-1.2.3.4-rebind-169.254-169.254-rr.1u.ms
```



## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]
- [[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Create rotating domain with two IPs]]

## Tags

- [[Bypassing filters]]
- [[Bypassing using DNS Rebinding (TOCTOU)]]
- [[Server-Side Request Forgery]]


