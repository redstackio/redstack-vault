---
id: 3cb3ecaf-63f0-4a4c-85a0-ee194fac5a34
name: DNS Rebinding to Localhost
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:57.659791+00:00'
updated_at: '2023-04-10T20:22:11.050487+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[DNS Rebinding]]'
- '[[localhost]]'
- '[[Protection Bypasses]]'
commands:
- '[[DNS Lookup for www.example.com]]'
---

# DNS Rebinding to Localhost

## Summary

DNS rebinding to localhost is a technique that can be used to bypass filters blocking DNS responses containing 127.0.0.1. An attacker can use this technique to communicate with a service running on localhost that is not accessible from the internet. This technique can be used to bypass security con

## Description

# Description

DNS rebinding to localhost is a technique that can be used to bypass filters blocking DNS responses containing 127.0.0.1. An attacker can use this technique to communicate with a service running on localhost that is not accessible from the internet. This technique can be used to bypass security controls and gain access to sensitive information or systems.

To perform DNS rebinding to localhost, the attacker first sends a DNS response to the victim's computer with a TTL value of 0. This causes the victim's computer to send a new DNS request to the attacker's server, which can then respond with a DNS response containing the IP address of localhost. The attacker can then use this IP address to communicate with a service running on localhost that is not accessible from the internet.

 

## Requirements

1. Access to a DNS server

1. Ability to send and receive DNS responses

 

## Defense

1. Configure firewalls and other security controls to block DNS responses with TTL values of 0.

1. Monitor DNS traffic for signs of DNS rebinding attacks.

 

## Objectives

1. Bypass DNS filters to communicate with a service running on localhost

1. Gain access to sensitive information or systems

 

# Instructions

1. 

 



**Code**: [[$ dig www.example.com +noall +answer
; <<>> DiG 9.]]



> The command uses the dig utility to create a CNAME record for "localhost.example.com" that points to "localhost".



**Command** ([[DNS Lookup for www.example.com]]):

```bash
$ dig www.example.com +noall +answer
```



## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Commands Used

- [[DNS Lookup for www.example.com]]

## Tags

- [[DNS Rebinding]]
- [[localhost]]
- [[Protection Bypasses]]


