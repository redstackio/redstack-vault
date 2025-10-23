---
id: 3c5cc7a3-cf40-4d0e-97e4-518a5f8f738f
name: 'Web Cache Deception - Methodology 2: Un-keyed Input Cache Poisoning'
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:41.278214+00:00'
updated_at: '2023-04-06T03:56:41.293010+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Internal Spearphishing|T1534 - Internal Spearphishing]]'
- '[[Virtualization/Sandbox Evasion|T1497 - Virtualization/Sandbox Evasion]]'
tags:
- '[[Methodology 2]]'
- '[[Web Cache Deception]]'
commands:
- '[[Extract HTTP headers]]'
---

# Web Cache Deception - Methodology 2: Un-keyed Input Cache Poisoning

## Summary

Web Cache Deception is a technique that allows an attacker to bypass a victim's cache and interact with a web server directly. In this methodology, the attacker uses un-keyed input to poison the victim's cache. When the victim requests a resource that has been poisoned, the attacker can then execut

## Description

# Description

Web Cache Deception is a technique that allows an attacker to bypass a victim's cache and interact with a web server directly. In this methodology, the attacker uses un-keyed input to poison the victim's cache. When the victim requests a resource that has been poisoned, the attacker can then execute a Cache Poisoning attack, which will allow them to serve malicious content to the victim. This technique can be used to perform a variety of attacks, including phishing, malware delivery, and man-in-the-middle attacks.

To perform this attack, the attacker must first identify a vulnerable web application that uses caching. They then send a request to the application, including un-keyed input that will be cached by the victim's browser. When the victim requests the same resource, the attacker can then execute a Cache Poisoning attack, serving malicious content to the victim.

 

## Requirements

1. Access to a vulnerable web application that uses caching

1. Ability to send requests to the web application with un-keyed input

 

## Defense

1. Implement input validation on the web application to prevent un-keyed input from being cached

1. Implement secure caching policies that prevent malicious content from being served to users

1. Monitor for suspicious activity, such as multiple requests for the same resource from the same IP address

 

## Objectives

1. Poison the victim's cache with un-keyed input

1. Execute a Cache Poisoning attack to serve malicious content to the victim

 

# Instructions

1. To perform a cache poisoning attack, look for un-keyed inputs in the specified headers and values. These inputs can be manipulated to inject malicious content into the cache.

 



**Code**: [[Values: User-Agent
Values: Cookie
Header: X-Forwar]]



> Cache poisoning attacks involve manipulating a cache to serve malicious content to unsuspecting users. By finding un-keyed inputs, an attacker can inject their own content into the cache and potentially compromise the security of the system. The specified headers and values are common areas where un-keyed inputs can be found, and should be thoroughly checked for vulnerabilities.



**Command** ([[Extract HTTP headers]]):

```bash
Values: User-Agent
Values: Cookie
Header: X-Forwarded-Host
Header: X-Host
Header: X-Forwarded-Server
Header: X-Forwarded-Scheme (header; also in combination with X-Forwarded-Host)
Header: X-Original-URL (Symfony)
Header: X-Rewrite-URL (Symfony)
```



2. To perform a cache poisoning attack using un-keyed input, follow these steps: 
1. Craft a GET request with the target URL and a buster parameter. 
2. In the Host header, specify the domain name of the target website. 
3. In the X-Forwarded-Host header, inject a script tag with a malicious payload. 
4. Send the request to the target server. 
5. If the server is vulnerable, it will cache the response and include the malicious payload. 
6. When a user visits the cached page, the payload will execute and the attacker can potentially steal sensitive information or perform other malicious actions.

 



**Code**: [[GET /test?buster=123 HTTP/1.1
Host: target.com
X-F]]



> The `X-Forwarded-Host` header is used to indicate the original host name or IP address of the client in a proxied environment. In this attack, the attacker injects a script tag with a malicious payload into the `X-Forwarded-Host` header. When the server processes the request, it will cache the response including the malicious payload. When a user visits the cached page, the payload will execute and the attacker can potentially steal sensitive information or perform other malicious actions. It is important to note that using a buster parameter in the request can help ensure that only the targeted webpage is cached and not the entire website.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Internal Spearphishing|T1534 - Internal Spearphishing]]
- [[Virtualization/Sandbox Evasion|T1497 - Virtualization/Sandbox Evasion]]

## Commands Used

- [[Extract HTTP headers]]

## Tags

- [[Methodology 2]]
- [[Web Cache Deception]]


