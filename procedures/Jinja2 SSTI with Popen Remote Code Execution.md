---
id: be168a30-cf39-4e97-9a7f-b65a052d70d3
name: Jinja2 SSTI with Popen Remote Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.854934+00:00'
updated_at: '2023-04-10T20:23:43.537689+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
tags:
- '[[Exploit the SSTI by calling Popen without guessing the offset]]'
- '[[Jinja2]]'
- '[[Jinja2 - Remote Code Execution]]'
- '[[Server Side Template Injection]]'
---

# Jinja2 SSTI with Popen Remote Code Execution

## Summary

Jinja2 is a widely used template engine for Python. Server Side Template Injection (SSTI) in Jinja2 allows an attacker to execute arbitrary code on the server. This specific procedure exploits the SSTI vulnerability by calling Popen without guessing the offset. The attacker can then retrieve sensit

## Description

# Description

Jinja2 is a widely used template engine for Python. Server Side Template Injection (SSTI) in Jinja2 allows an attacker to execute arbitrary code on the server. This specific procedure exploits the SSTI vulnerability by calling Popen without guessing the offset. The attacker can then retrieve sensitive information or execute arbitrary commands on the target server.

This procedure can be used for offensive purposes to gain unauthorized access to a target server. From a technical perspective, the attacker can inject malicious code into a template file, which is then executed by the server. This can lead to data exfiltration, privilege escalation, and other malicious activities. From a business perspective, this procedure highlights the importance of securing web applications and servers to prevent unauthorized access and data breaches.

## Requirements

1. Access to a vulnerable web application that uses Jinja2 template engine

1. Knowledge of the SSTI vulnerability and how to exploit it

1. Access to a command line interface

## Defense

1. Keep all software up to date with the latest security patches

1. Implement input validation and sanitization on the server side to prevent SSTI attacks

1. Implement access controls and limit privileges to prevent unauthorized access to sensitive data

## Objectives

1. Retrieve sensitive information from the target server

1. Execute arbitrary commands on the target server

# Instructions

1. To retrieve the flag, execute this command on the target machine in a Python environment.

**Code**: [[{% for x in ().__class__.__base__.__subclasses__()]]

> This command uses Python to establish a socket connection to an IP address on port 4444. It then redirects standard input, output, and error to the socket and uses subprocess to execute the command '/bin/cat flag.txt', which reads and outputs the contents of the 'flag.txt' file. The output is then padded with zeros to a length of 417 characters to avoid detection by some intrusion detection systems.

2. To execute an operating system command, include a variable named "input" in the GET parameter and set its value to the command you want to run.

**Code**: [[{% for x in ().__class__.__base__.__subclasses__()]]

> This payload can be used to exploit a vulnerability in a web application that allows for operating system command injection. The payload uses Python code to execute the command specified in the "input" variable. The output of the command is then returned in the response. It is important to note that this vulnerability can be used by an attacker to execute any command on the system with the privileges of the web server process.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]

## Tags

- [[Exploit the SSTI by calling Popen without guessing the offset]]
- [[Jinja2]]
- [[Jinja2 - Remote Code Execution]]
- [[Server Side Template Injection]]
