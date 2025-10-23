---
id: fd093192-2fde-4c93-8e65-92a7c30dfd60
name: URL Blacklist Bypass using URL encoding
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:37.486135+00:00'
updated_at: '2023-04-10T20:24:05.711222+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Bypassing filters]]'
- '[[Bypass using URL encoding]]'
- '[[Server-Side Request Forgery]]'
---

# URL Blacklist Bypass using URL encoding

## Summary

URL Blacklist Bypass using URL encoding is a technique used to bypass URL blacklists that are implemented to prevent Server-Side Request Forgery (SSRF) attacks. This technique is used when the attacker wants to access a resource that is blocked by the server. The attacker encodes the URL of the res

## Description

# Description

URL Blacklist Bypass using URL encoding is a technique used to bypass URL blacklists that are implemented to prevent Server-Side Request Forgery (SSRF) attacks. This technique is used when the attacker wants to access a resource that is blocked by the server. The attacker encodes the URL of the resource using URL encoding and sends the request to the server. The server then decodes the URL and processes the request, allowing the attacker to access the blocked resource.

This technique is possible because many URL blacklists only check for the presence of certain keywords in the URL, and do not check for encoded versions of those keywords. This makes it easy for an attacker to bypass the blacklist by encoding the blocked keywords in the URL.

The business value of this technique is that it allows an attacker to bypass security measures and access resources that they should not be able to access. This can lead to the theft of sensitive information or the compromise of the server.

 

## Requirements

1. Access to a vulnerable web application

1. Knowledge of URL encoding

1. Ability to send HTTP requests

 

## Defense

1. Implement a whitelist-based approach to URL filtering instead of a blacklist-based approach

1. Regularly update and patch web applications to prevent vulnerabilities that can be exploited for SSRF attacks

1. Monitor network traffic for suspicious activity, such as requests to internal resources

 

## Objectives

1. Bypass URL blacklists to access blocked resources

1. Conduct SSRF attacks to access sensitive information or compromise the server

 

# Instructions

1. To use this command, specify the URL that you want to bypass the blacklist for. You can encode the URL either once or twice using the % symbol followed by the hexadecimal representation of the character. For example, %61 represents the letter 'a'.

 



**Code**: [[http://127.0.0.1/%61dmin
http://127.0.0.1/%2561dmi]]



> This command allows you to bypass a blacklist that is in place to prevent certain URLs from being accessed. By encoding the URL using the % symbol followed by the hexadecimal representation of the character, you can trick the system into thinking that the URL is different from the one that is blacklisted. This can be useful in situations where you need to access a blocked URL for legitimate purposes.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Tags

- [[Bypassing filters]]
- [[Bypass using URL encoding]]
- [[Server-Side Request Forgery]]


