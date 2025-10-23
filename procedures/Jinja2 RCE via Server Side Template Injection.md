---
id: 36b1af86-ea35-42bc-ae24-c63cfcc6b9ba
name: Jinja2 RCE via Server Side Template Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.733501+00:00'
updated_at: '2023-04-10T20:23:46.293869+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Jinja2]]'
- '[[Jinja2 - Remote Code Execution]]'
- '[[Server Side Template Injection]]'
commands:
- '[[Start netcat listener on port 8000]]'
---

# Jinja2 RCE via Server Side Template Injection

## Summary

Jinja2 is a widely used templating engine for Python-based web applications. It allows developers to dynamically generate HTML pages by rendering templates with user-provided data. However, if the application is not properly secured, attackers can inject malicious code into the templates. This can 

## Description

# Description

Jinja2 is a widely used templating engine for Python-based web applications. It allows developers to dynamically generate HTML pages by rendering templates with user-provided data. However, if the application is not properly secured, attackers can inject malicious code into the templates. This can lead to remote code execution (RCE) on the server, allowing the attacker to execute arbitrary commands and gain full control of the system.

To exploit this vulnerability, an attacker can inject malicious code into a template file, which will then be executed by the server when the template is rendered. This can be achieved by using various techniques such as string formatting, function calls, and object injection. Once the attacker has achieved RCE, they can perform various malicious activities such as stealing sensitive data, installing backdoors, and launching further attacks.

 

## Requirements

1. Access to the target web application

1. Knowledge of the application's templating engine (Jinja2)

1. Ability to inject malicious code into the application's templates

 

## Defense

1. Ensure that the web application is up-to-date with the latest security patches

1. Implement proper input validation and sanitization to prevent template injection attacks

1. Implement least privilege access control to limit the impact of a successful attack

 

## Objectives

1. Gain remote code execution on the target server

1. Maintain persistence on the compromised system

1. Steal sensitive data from the target system

 

# Instructions

1. This command sets up a listener on port 8000 using the netcat utility. It waits for incoming connections and displays any data that is received.

 



**Code**: [[nc -lnvp 8000]]



> The 'nc' command is used to establish a network connection. The '-l' flag is used to specify that the command should listen for incoming connections. The '-n' flag disables DNS lookups, which can speed up the connection process. The '-v' flag enables verbose output, which displays more information about the connection. The '-p' flag is used to specify the port number to listen on. In this case, port 8000 is used. Once a connection is established, any data that is received will be displayed in the terminal window.



**Command** ([[Start netcat listener on port 8000]]):

```bash
nc -lnvp 8000
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Start netcat listener on port 8000]]

## Tags

- [[Jinja2]]
- [[Jinja2 - Remote Code Execution]]
- [[Server Side Template Injection]]


