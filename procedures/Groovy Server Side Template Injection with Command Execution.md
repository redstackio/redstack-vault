---
id: dfbb572f-9db2-4575-be12-9d03cc6fcddd
name: Groovy Server Side Template Injection with Command Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.205085+00:00'
updated_at: '2023-04-10T20:23:42.719023+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Groovy]]'
- '[[Groovy - Command Execution]]'
- '[[Server Side Template Injection]]'
---

# Groovy Server Side Template Injection with Command Execution

## Summary

Groovy Server Side Template Injection with Command Execution is an attack technique that exploits a vulnerability in server-side web applications that allows an attacker to execute arbitrary code on the server. This technique is accomplished by injecting malicious code into templates that are used 

## Description

# Description

Groovy Server Side Template Injection with Command Execution is an attack technique that exploits a vulnerability in server-side web applications that allows an attacker to execute arbitrary code on the server. This technique is accomplished by injecting malicious code into templates that are used to generate dynamic web pages. The attacker can then execute commands on the server, allowing them to gain access to sensitive data or take control of the server. This technique can be used to bypass security measures, such as firewalls or intrusion detection systems, and can be difficult to detect.

From a technical perspective, Groovy is a scripting language that is often used in server-side web applications. It is similar to Java, but with a more concise syntax and dynamic typing. Groovy templates are used to generate dynamic web pages, and they can contain code that is executed on the server. By injecting malicious code into these templates, an attacker can execute arbitrary code on the server.

From a business perspective, this technique can be used by attackers to gain access to sensitive data or take control of a server. This can result in financial loss, reputational damage, and legal liability for the affected organization.

## Requirements

1. Access to a vulnerable server-side web application

1. Knowledge of Groovy scripting language

1. Ability to inject malicious code into templates

## Defense

1. Implement input validation and sanitization to prevent injection attacks

1. Use a web application firewall to detect and block malicious requests

1. Regularly update and patch server-side web applications to address known vulnerabilities

## Objectives

1. Execute arbitrary code on the server

1. Gain access to sensitive data

1. Take control of the server

# Instructions

1. This command opens the calculator application on the system.

**Code**: [[${"calc.exe".exec()}
${"calc.exe".execute()}
${thi]]

> The 'data' field contains multiple ways to execute the 'calc.exe' command in Groovy. The 'exec()' and 'execute()' methods are used to execute the command as a separate process. The 'evaluate()' method is used to execute a script and return the result. The 'MethodClosure' class is used to call the 'execute()' method on the 'calc.exe' object. This command can be used to open the calculator application on Windows systems.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Groovy]]
- [[Groovy - Command Execution]]
- [[Server Side Template Injection]]
