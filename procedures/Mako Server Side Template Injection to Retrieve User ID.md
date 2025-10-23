---
id: ea739c3c-93a8-4f6c-ab1a-e601d94f253f
name: Mako Server Side Template Injection to Retrieve User ID
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.072248+00:00'
updated_at: '2023-04-10T20:23:34.070074+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
sub_techniques:
- '[[Unix Shell|T1059.004 - Unix Shell]]'
tags:
- '[[Mako]]'
- '[[Server Side Template Injection]]'
---

# Mako Server Side Template Injection to Retrieve User ID

## Summary

Mako is a server-side template engine that allows developers to build dynamic web applications. However, if not properly secured, Mako can be vulnerable to Server Side Template Injection (SSTI) attacks. An attacker can use SSTI to execute arbitrary code on the server and potentially gain access to 

## Description

# Description

Mako is a server-side template engine that allows developers to build dynamic web applications. However, if not properly secured, Mako can be vulnerable to Server Side Template Injection (SSTI) attacks. An attacker can use SSTI to execute arbitrary code on the server and potentially gain access to sensitive information. In this case, the attacker is using SSTI to retrieve the user ID of the target. By injecting code into a Mako template, the attacker can retrieve the user ID and potentially use it to further their attack. This attack can be particularly dangerous in cases where the user ID is used as a primary key or is otherwise used to authenticate the user.

 

## Requirements

1. Access to a vulnerable Mako template on the target server

 

## Defense

1. Ensure that Mako templates are properly secured and do not allow for arbitrary code execution

1. Implement input validation and sanitization to prevent injection attacks

1. Regularly update and patch Mako and other web application components to ensure that known vulnerabilities are addressed

 

## Objectives

1. Retrieve the user ID of the target

1. Potentially use the user ID to further the attack

 

# Instructions

1. This command retrieves the user ID of the current user.

 



**Code**: [[<%
import os
x=os.popen('id').read()
%>
${x}]]



> The `os.popen('id').read()` function is used to execute the `id` command in the terminal and capture its output. The captured output is then returned as the value of the `x` variable. The `${x}` syntax is used to insert the value of `x` into the response. This command can be useful for identifying the current user and determining their permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

### Sub-Techniques

- [[Unix Shell|T1059.004 - Unix Shell]]

## Tags

- [[Mako]]
- [[Server Side Template Injection]]


