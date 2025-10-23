---
id: 6ae50f95-ebee-4e8e-8b61-cad7c32f90c1
name: Server-Side Request Forgery via Bypassing Filters with HTTPS
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.241475+00:00'
updated_at: '2023-04-10T20:23:57.114075+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Connection Proxy|T1090 - Connection Proxy]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Bypassing filters]]'
- '[[Bypass using HTTPS]]'
- '[[Server-Side Request Forgery]]'
commands:
- '[[Accessing Localhost]]'
---

# Server-Side Request Forgery via Bypassing Filters with HTTPS

## Summary

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to send crafted requests from a vulnerable web application. The attacker can use this vulnerability to bypass filters that are in place to prevent unauthorized requests. By using HTTPS, the attacker can bypass filters tha

## Description

# Description

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to send crafted requests from a vulnerable web application. The attacker can use this vulnerability to bypass filters that are in place to prevent unauthorized requests. By using HTTPS, the attacker can bypass filters that are designed to prevent requests to localhost or other internal network resources. This technique can be used to exfiltrate data from the target network or to evade detection by hiding the attacker's IP address.

Technical Explanation: The attacker sends a request to the vulnerable web application, which then makes a request to the target server. The attacker can craft the request to include a URL that points to an internal network resource. By using HTTPS, the attacker can bypass filters that would normally block requests to internal network resources. The attacker can then use this technique to exfiltrate data from the target network or to evade detection by hiding their IP address.

Business Value: This technique can be used by attackers to steal sensitive data from a target network. By using HTTPS, the attacker can bypass filters that would normally prevent unauthorized requests to internal network resources.

 

## Requirements

1. Access to a vulnerable web application

 

## Defense

1. Implement input validation to prevent SSRF attacks

1. Use a web application firewall to block malicious requests

1. Monitor network traffic for unusual activity

 

## Objectives

1. Bypass filters that are in place to prevent unauthorized requests

1. Exfiltrate data from the target network

1. Evade detection by hiding the attacker's IP address

 

# Instructions

1. To access the local server, use the following URLs:

 



**Code**: [[https://127.0.0.1/
https://localhost/]]



> The 'data' field contains the URLs for accessing the local server. These URLs can be used to access the server from a web browser or through other applications. The 'lang' field specifies the language used for executing the commands, which in this case is PowerShell. The 'instruction' field provides guidance on how to use the URLs, and the 'explain' field provides additional details about the command and its purpose.



**Command** ([[Accessing Localhost]]):

```bash
https://127.0.0.1/
https://localhost/
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Connection Proxy|T1090 - Connection Proxy]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Accessing Localhost]]

## Tags

- [[Bypassing filters]]
- [[Bypass using HTTPS]]
- [[Server-Side Request Forgery]]


