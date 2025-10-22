---
id: 86284845-39ad-4aa5-b785-e6a452a4810d
name: Ruby Server Side Template Injection - Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.228212+00:00'
updated_at: '2023-04-10T20:23:29.563698+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Signed Script Proxy Execution|T1216 - Signed Script Proxy Execution]]'
tags:
- '[[Ruby]]'
- '[[Ruby - Code execution]]'
- '[[Server Side Template Injection]]'
---

# Ruby Server Side Template Injection - Code Execution

## Summary

Ruby Server Side Template Injection is a technique that allows an attacker to inject and execute arbitrary code on the server-side. This can be used to achieve remote code execution and gain access to sensitive data. The vulnerability arises when user input is not properly sanitized and is included

## Description

# Description

Ruby Server Side Template Injection is a technique that allows an attacker to inject and execute arbitrary code on the server-side. This can be used to achieve remote code execution and gain access to sensitive data. The vulnerability arises when user input is not properly sanitized and is included in a server-side template. This can lead to the execution of arbitrary code on the server.

From a technical standpoint, Ruby Server Side Template Injection is a vulnerability that arises when Ruby code is embedded within a template. When this Ruby code is executed, it can perform any action that the server is capable of. This can include accessing the file system, executing system commands, and accessing sensitive data.

The business value of this technique is that it can be used to gain access to sensitive data and execute arbitrary code on the server. This can lead to a complete compromise of the server and can result in significant damages to the organization.

## Requirements

1. Access to a vulnerable server

## Defense

1. Ensure that all user input is properly sanitized before being included in server-side templates

1. Disable server-side template execution in production environments

1. Use a web application firewall to detect and block attempts at exploiting server-side template injection vulnerabilities

## Objectives

1. Execute arbitrary code on the server

1. Gain access to sensitive data

# Instructions

1. This command executes code on the server using Server-Side Template Injection (SSTI) for ERB engine. The command retrieves the contents of the /etc/passwd file and lists the contents of the root directory. The command also retrieves the current user using the Open3 and Open4 libraries.

**Code**: [[<%= system('cat /etc/passwd') %>
<%= `ls /` %>
<%=]]

> The 'system' command executes a shell command and returns the output. The 'popen' method opens a pipe to or from a command and returns an IO object. The 'readlines' method reads all lines from the IO object and returns an array of strings. The 'require' method loads a library. The 'popen3' method opens a pipe to a command and returns four IO objects: stdin, stdout, stderr, and a thread object. The 'readline' method reads a line from the IO object. The 'popen4' method opens a pipe to a command and returns four IO objects: stdin, stdout, stderr, and a process ID.

2. To retrieve environment variables using Slim engine and SSTI, use the following command:

**Code**: [[#{ %x|env| }]]

> The `env` command is used to display all environment variables currently set on the system. The `%x|` syntax is used to execute a system command and return the output as a string. This command can be used to retrieve sensitive information such as API keys or database credentials stored in environment variables.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Signed Script Proxy Execution|T1216 - Signed Script Proxy Execution]]

## Tags

- [[Ruby]]
- [[Ruby - Code execution]]
- [[Server Side Template Injection]]
