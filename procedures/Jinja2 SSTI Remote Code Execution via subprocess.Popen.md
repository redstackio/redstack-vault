---
id: 1f0fdded-613f-488f-b9d9-e2074db5e985
name: Jinja2 SSTI Remote Code Execution via subprocess.Popen
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.819825+00:00'
updated_at: '2023-04-10T20:23:47.419749+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Exploit the SSTI by calling subprocess.Popen]]'
- '[[Jinja2]]'
- '[[Jinja2 - Remote Code Execution]]'
- '[[Server Side Template Injection]]'
---

# Jinja2 SSTI Remote Code Execution via subprocess.Popen

## Summary

Jinja2 is a popular templating engine used for web applications. It allows developers to dynamically generate web pages by embedding variables and expressions within HTML templates. However, if user input is not properly sanitized, it can lead to Server Side Template Injection (SSTI) vulnerabilitie

## Description

# Description

Jinja2 is a popular templating engine used for web applications. It allows developers to dynamically generate web pages by embedding variables and expressions within HTML templates. However, if user input is not properly sanitized, it can lead to Server Side Template Injection (SSTI) vulnerabilities. Attackers can exploit these vulnerabilities to execute arbitrary code on the server. In this case, the attacker can use the subprocess.Popen function to execute shell commands and list files in the current directory.

This attack can be used to gain access to sensitive information, modify or delete data, or launch further attacks against the network. The technical explanation of this attack is that the attacker can inject malicious code into the Jinja2 template, which is then executed by the server. The business value of this attack is that it can lead to reputational damage, financial losses, and legal liabilities for the targeted organization.

## Requirements

1. Access to a vulnerable web application that uses Jinja2 templating engine

1. Knowledge of the vulnerable parameter and how to inject malicious code

## Defense

1. Properly sanitize user input to prevent SSTI vulnerabilities

1. Implement input validation and output encoding to prevent injection attacks

1. Monitor web application logs for suspicious activity and anomalous behavior

## Objectives

1. Execute arbitrary shell commands on the server

1. List files in the current directory

# Instructions

1. This command allows the user to execute shell commands and list files in the current directory. To execute a command, replace 'cat flag.txt' with the desired command in the first set of curly braces. To list files in the current directory, simply leave the second set of curly braces as is.

**Code**: [[{{''.__class__.mro()[1].__subclasses__()[396]('cat]]

> The first set of curly braces executes the specified shell command using Python's subprocess module. The second set of curly braces lists the files in the current directory using Python's os module. This command can be used for various purposes such as retrieving sensitive information, modifying files, or executing other commands on the system.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Exploit the SSTI by calling subprocess.Popen]]
- [[Jinja2]]
- [[Jinja2 - Remote Code Execution]]
- [[Server Side Template Injection]]
