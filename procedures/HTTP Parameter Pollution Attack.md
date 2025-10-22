---
id: a9206879-33db-4794-9deb-045653b3b1a6
name: HTTP Parameter Pollution Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.026991+00:00'
updated_at: '2023-04-10T20:22:28.716927+00:00'
tags:
- '[[How to test]]'
- '[[HTTP Parameter Pollution]]'
commands:
- '[[Injection attack]]'
- '[[Injection happens]]'
- '[[Read first parameter]]'
- '[[Read second parameter]]'
- '[[WAF passes on]]'
---

# HTTP Parameter Pollution Attack

## Summary

The HTTP Parameter Pollution (HPP) attack is a web attack evasion technique that allows an attacker to manipulate web logics or retrieve hidden information by crafting a HTTP request. This attack is based on splitting an attack vector between multiple instances of a parameter with the same name. As

## Description

# Description

The HTTP Parameter Pollution (HPP) attack is a web attack evasion technique that allows an attacker to manipulate web logics or retrieve hidden information by crafting a HTTP request. This attack is based on splitting an attack vector between multiple instances of a parameter with the same name. As there is no formal way of parsing HTTP parameters, individual web technologies have their own unique way of parsing and reading URL parameters with the same name. Some taking the first occurrence, some taking the last occurrence, and some reading it as an array. This behavior is abused by the attacker in order to bypass pattern-based security mechanisms. In this example scenario, the attacker uses HPP to inject malicious code into the second 'search' parameter, which is not properly checked by the origin service.

## Requirements

1. Access to the target web application.

## Defense

1. Implement input validation and sanitization techniques to check for malicious characters or code in HTTP requests.

1. Implement pattern-based security mechanisms to detect and block HPP attacks.

1. Use a Web Application Firewall (WAF) to detect and block malicious HTTP requests.

## Objectives

1. To manipulate web logics or retrieve hidden information by injecting malicious code into HTTP requests.

1. To bypass pattern-based security mechanisms and evade detection.

# Instructions

1. Craft a HTTP request with multiple instances of a parameter with the same name. Manipulate the value of the parameter to inject malicious code into the request.

The attacker can use various techniques to inject malicious code into the HTTP request, such as SQL injection, cross-site scripting (XSS), or command injection.

**Command** ([[Read first parameter]]):

```bash
WAF reads first param
```

**Command** ([[Read second parameter]]):

```bash
Origin Service reads second param
```

**Command** ([[Injection attack]]):

```bash
http://example.com?search=Beth&search=' OR 1=1;
```

**Command** ([[WAF passes on]]):

```bash
WAF reads first 'search' param, looks innocent. passes on
```

**Command** ([[Injection happens]]):

```bash
Origin Service reads second 'search' param, injection happens if no checks are done here.
```

## Commands Used

- [[Injection attack]]
- [[Injection happens]]
- [[Read first parameter]]
- [[Read second parameter]]
- [[WAF passes on]]

## Tags

- [[How to test]]
- [[HTTP Parameter Pollution]]
