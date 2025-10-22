---
id: df575cbf-d6ea-4bbe-ab44-2bf1e42f31c6
name: Server Side Template Injection with Groovy HTTP Request
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.178564+00:00'
updated_at: '2023-04-10T20:23:32.537259+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Groovy]]'
- '[[Groovy - HTTP request:]]'
- '[[Server Side Template Injection]]'
commands:
- '[[Retrieve text from Google homepage using Groovy String]]'
- '[[Retrieve text from Google homepage using Groovy URL]]'
---

# Server Side Template Injection with Groovy HTTP Request

## Summary

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a server-side template, which is then executed by the server. In this case, we are using Groovy to perform an HTTP request that triggers SSTI. Groovy is a scripting language that is often 

## Description

# Description

Server Side Template Injection (SSTI) is a vulnerability that allows an attacker to inject malicious code into a server-side template, which is then executed by the server. In this case, we are using Groovy to perform an HTTP request that triggers SSTI. Groovy is a scripting language that is often used in Java applications. By using Groovy to make an HTTP request, we can inject malicious code into the server-side template and execute it. This can allow us to gain access to sensitive information or even take control of the server.

The technical explanation of this procedure is that we are exploiting a vulnerability in the server-side template engine. By injecting malicious code into the template, we can execute arbitrary code on the server. This can allow us to read or modify sensitive files, execute commands on the server, or even take control of the server.

The business value of this procedure is that it allows an attacker to gain access to sensitive information or take control of a server. This can be used for corporate espionage, data theft, or even ransomware attacks.

## Requirements

1. Access to a vulnerable server-side template engine

1. Groovy installed on the attacking machine

## Defense

1. Keep all software up to date with the latest security patches

1. Implement input validation and sanitization to prevent injection attacks

1. Implement access controls to limit the impact of successful attacks

## Objectives

1. Inject malicious code into the server-side template

1. Execute arbitrary code on the server

# Instructions

1. To retrieve the Google homepage, use the following commands:

**Code**: [[${"http://www.google.com".toURL().text}
${new URL(]]

> 1. ${"http://www.google.com".toURL().text} - This command will retrieve the HTML content of the Google homepage by converting the URL string into a URL object and then using the 'text' method to retrieve the content as a string.
2. ${new URL("http://www.google.com").getText()} - This command will retrieve the HTML content of the Google homepage by creating a new URL object and then using the 'getText' method to retrieve the content as a string.

**Command** ([[Retrieve text from Google homepage using Groovy String]]):

```bash
${"http://www.google.com".toURL().text}
```

**Command** ([[Retrieve text from Google homepage using Groovy URL]]):

```bash
${new URL("http://www.google.com").getText()}
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Retrieve text from Google homepage using Groovy String]]
- [[Retrieve text from Google homepage using Groovy URL]]

## Tags

- [[Groovy]]
- [[Groovy - HTTP request:]]
- [[Server Side Template Injection]]
