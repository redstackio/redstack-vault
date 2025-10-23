---
id: be08b9fb-0599-4696-ad43-7ad124d771d6
name: CORS Misconfiguration - Expanding the Origin / Regex Issues
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:55.226962+00:00'
updated_at: '2023-04-06T03:55:55.240117+00:00'
tags:
- '[[CORS Misconfiguration]]'
- '[[Exploitation]]'
- '[[Vulnerable Example: Expanding the Origin / Regex Issues]]'
- '[[Vulnerable Implementation (Example 2)]]'
commands:
- '[[GET request to /endpoint]]'
---

# CORS Misconfiguration - Expanding the Origin / Regex Issues

## Summary

CORS (Cross-Origin Resource Sharing) is a security feature implemented in web browsers that allows web pages to make AJAX requests to a different domain than the one that served the web page. A misconfiguration in CORS allows attackers to bypass the Same-Origin Policy and perform Cross-Site Request

## Description

# Description

CORS (Cross-Origin Resource Sharing) is a security feature implemented in web browsers that allows web pages to make AJAX requests to a different domain than the one that served the web page. A misconfiguration in CORS allows attackers to bypass the Same-Origin Policy and perform Cross-Site Request Forgery (CSRF) attacks. In this scenario, the server utilizes a regex where the dot was not escaped correctly, which results in a vulnerability that can be exploited by an attacker to perform unauthorized actions on behalf of the victim. The impact of this vulnerability can range from data theft to complete compromise of the victim's account.

 

## Requirements

1. Access to a vulnerable web application with a CORS misconfiguration.

 

## Defense

1. Implement proper input validation and sanitization to prevent regex issues.

1. Implement proper CORS configuration to prevent unauthorized access to sensitive resources.

1. Use the Content-Security-Policy (CSP) header to prevent the execution of malicious scripts on the web page.

 

## Objectives

1. Exploit the CORS misconfiguration to perform unauthorized actions on behalf of the victim.

1. Perform Cross-Site Request Forgery (CSRF) attacks.

 

# Instructions

1. Replace the vulnerable regex with a more secure one that properly escapes the dot character.

 



**Code**: [[^api.example.com$]]



> The regex used by the server is vulnerable to regex issues. The dot character is used to match any character except newline, but it needs to be escaped to match a literal dot. An attacker can bypass the CORS protection by using a domain name that matches the vulnerable regex, which allows them to perform unauthorized actions on behalf of the victim.

2. Replace the vulnerable regex with a more secure one that properly escapes the dot character.

 



**Code**: [[^api\.example.com$]]



> The secure regex properly escapes the dot character, which makes it match only the literal dot character. This prevents an attacker from bypassing the CORS protection by using a domain name that matches the vulnerable regex.

3. Craft an HTTP request that exploits the CORS misconfiguration.

 



**Code**: [[GET /endpoint HTTP/1.1
Host: api.example.com
Origi]]



> The HTTP request includes a valid Origin header that matches the vulnerable regex, which allows an attacker to bypass the CORS protection and perform unauthorized actions on behalf of the victim. The server responds with a valid Access-Control-Allow-Origin header that matches the attacker's Origin header, which allows the attacker to read the response from the server.



**Command** ([[GET request to /endpoint]]):

```bash
GET /endpoint HTTP/1.1
Host: api.example.com
Origin: https://apiiexample.com


```



## Commands Used

- [[GET request to /endpoint]]

## Tags

- [[CORS Misconfiguration]]
- [[Exploitation]]
- [[Vulnerable Example: Expanding the Origin / Regex Issues]]
- [[Vulnerable Implementation (Example 2)]]


