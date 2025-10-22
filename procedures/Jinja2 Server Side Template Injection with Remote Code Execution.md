---
id: 037a9f1c-e367-4716-b931-af4278db0d17
name: Jinja2 Server Side Template Injection with Remote Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.758140+00:00'
updated_at: '2023-04-10T20:23:48.895384+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Create Account|T1136 - Create Account]]'
sub_techniques:
- '[[PowerShell|T1059.001 - PowerShell]]'
tags:
- '[[Jinja2]]'
- '[[Jinja2 - Forcing output on blind RCE]]'
- '[[Jinja2 - Remote Code Execution]]'
- '[[Server Side Template Injection]]'
---

# Jinja2 Server Side Template Injection with Remote Code Execution

## Summary

Jinja2 is a popular template engine for Python web applications. It allows developers to create templates that can be used to generate dynamic HTML pages. However, if user input is not properly sanitized, it can lead to Server Side Template Injection (SSTI) vulnerabilities. Attackers can exploit th

## Description

# Description

Jinja2 is a popular template engine for Python web applications. It allows developers to create templates that can be used to generate dynamic HTML pages. However, if user input is not properly sanitized, it can lead to Server Side Template Injection (SSTI) vulnerabilities. Attackers can exploit these vulnerabilities to execute arbitrary code on the server. In this case, we focus on exploiting a Jinja2 SSTI vulnerability to achieve Remote Code Execution (RCE).

To execute RCE, we use the Flask Hook Command. This command forces the server to execute arbitrary code by injecting it into the Jinja2 template. The injected code can be used to create a reverse shell, which can be used to execute commands on the server. The business value of this attack is that it allows attackers to gain full control of the server and steal sensitive data.

## Requirements

1. Access to a vulnerable web application that uses Jinja2 templates

1. Knowledge of Flask Hook Command and its usage

## Defense

1. Ensure that all user input is properly sanitized to prevent SSTI vulnerabilities

1. Limit the functionality of the application to only what is necessary

1. Implement a web application firewall to detect and prevent SSTI attacks

## Objectives

1. Exploit a Jinja2 SSTI vulnerability to achieve Remote Code Execution

1. Inject arbitrary code into the Jinja2 template using Flask Hook Command

1. Create a reverse shell to execute commands on the server

# Instructions

1. Use this command to execute a Flask hook function to return an output from the vulnerable page.

**Code**: [[{{
x.__init__.__builtins__.exec("from flask import]]

> This command allows you to import Flask functions and execute a hook function to return an output from the vulnerable page. The hook function is executed after the request is processed and can be used to modify the response, set headers or cookies, or perform other actions. The `current_app` object is used to access the Flask application instance, and the `after_this_request` decorator is used to register the hook function. The `make_response` function is used to create a response object with the specified content, and the response object is returned by the hook function. This command can be used to demonstrate the vulnerability of the Flask application and to test the effectiveness of security measures.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Create Account|T1136 - Create Account]]

### Sub-Techniques

- [[PowerShell|T1059.001 - PowerShell]]

## Tags

- [[Jinja2]]
- [[Jinja2 - Forcing output on blind RCE]]
- [[Jinja2 - Remote Code Execution]]
- [[Server Side Template Injection]]
