---
id: c2813919-dc42-4254-93e7-85ac31a3c2bb
name: Jinjava Uppercase String and Request Object Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.941391+00:00'
updated_at: '2023-04-10T20:23:50.015759+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Jinjava]]'
- '[[Jinjava - Basic injection]]'
- '[[Server Side Template Injection]]'
commands:
- '[[Convert a to uppercase]]'
- '[[Make a request]]'
---

# Jinjava Uppercase String and Request Object Injection

## Summary

Jinjava is a powerful templating engine for Python that allows developers to integrate dynamic content into their web applications. However, it is also vulnerable to Server Side Template Injection (SSTI) attacks. In this procedure, an attacker can convert a string to uppercase and obtain a request 

## Description

# Description

Jinjava is a powerful templating engine for Python that allows developers to integrate dynamic content into their web applications. However, it is also vulnerable to Server Side Template Injection (SSTI) attacks. In this procedure, an attacker can convert a string to uppercase and obtain a request object in Jinja. By doing so, the attacker can execute arbitrary code on the server and potentially gain access to sensitive data. The technical explanation of this attack involves manipulating the Jinja syntax to execute code on the server. The business value of this attack is that it can be used to steal sensitive data, compromise user accounts, and disrupt business operations.

## Requirements

1. Access to a vulnerable web application using Jinjava templating engine

## Defense

1. Ensure that all input is properly sanitized and validated to prevent injection attacks

1. Use a web application firewall (WAF) to detect and block SSTI attacks

1. Regularly update the Jinjava templating engine to the latest version to address any known vulnerabilities

## Objectives

1. Execute arbitrary code on the server

1. Gain access to sensitive data

1. Compromise user accounts

1. Disrupt business operations

# Instructions

1. To convert a string to uppercase in Jinja, use the toUpperCase() function. To obtain a request object, use the request keyword.

**Code**: [['a'.toUpperCase() would result in 'A'
request woul]]

> The toUpperCase() function is used to convert a string to uppercase in Jinja. For example, 'a'.toUpperCase() would result in 'A'.

The request keyword is used to obtain a request object in Jinja. The request object contains information about the current request, such as the URL and headers. For example, {{ request }} would return a request object like com.[...].context.TemplateContextRequest@23548206.

**Command** ([[Convert a to uppercase]]):

```bash
'a'.toUpperCase()
```

**Command** ([[Make a request]]):

```bash
request
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Convert a to uppercase]]
- [[Make a request]]

## Tags

- [[Jinjava]]
- [[Jinjava - Basic injection]]
- [[Server Side Template Injection]]
