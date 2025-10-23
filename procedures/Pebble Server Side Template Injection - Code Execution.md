---
id: 92253551-0d51-49fa-b07e-425c7aa547d1
name: Pebble Server Side Template Injection - Code Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.142815+00:00'
updated_at: '2023-04-10T20:23:38.888233+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Pebble]]'
- '[[Pebble - Code execution]]'
- '[[Server Side Template Injection]]'
---

# Pebble Server Side Template Injection - Code Execution

## Summary

Pebble is a Java-based server-side template engine that allows developers to define and render dynamic web pages. Unfortunately, it is vulnerable to Server Side Template Injection (SSTI) attacks, which allow an attacker to execute arbitrary code on the server. Attackers can use this technique to ga

## Description

# Description

Pebble is a Java-based server-side template engine that allows developers to define and render dynamic web pages. Unfortunately, it is vulnerable to Server Side Template Injection (SSTI) attacks, which allow an attacker to execute arbitrary code on the server. Attackers can use this technique to gain access to sensitive data, escalate privileges, or even take control of the entire system. 

To exploit this vulnerability, an attacker can use the 'List Files and Directories' and 'Get Current User ID' commands to gather information about the system and identify potential targets for further attacks. Once they have identified a vulnerable endpoint, they can use SSTI to execute arbitrary code and achieve their objectives.

 

## Requirements

1. Access to a vulnerable endpoint that uses the Pebble template engine

 

## Defense

1. Ensure that all input is properly sanitized and validated to prevent injection attacks

1. Implement strict access controls to limit the impact of successful attacks

1. Regularly monitor and analyze system logs for signs of suspicious activity

 

## Objectives

1. Execute arbitrary code on the server

1. Gain access to sensitive data

1. Escalate privileges

1. Take control of the entire system

 

# Instructions

1. This command lists all the files and directories in the current directory.

 



**Code**: [[{{ variable.getClass().forName('java.lang.Runtime']]



> The 'ls' command stands for 'list' and it is used to display the contents of a directory. The '-la' option is used to display the contents in a long listing format, which includes additional details such as file permissions, ownership, size, and date modified. This command can be useful for checking the contents of a directory, verifying the existence of a file, or troubleshooting file permissions. Note that the output of this command may vary depending on the operating system and the user's permissions.

2. This command retrieves the current user ID of the system.

 



**Code**: [[{% set cmd = 'id' %}
{% set bytes = (1).TYPE
     ]]



> The 'id' command is used to retrieve the current user ID of the system. The command is executed using the 'java.lang.Runtime' class and its 'exec' method. The output of the command is read using the 'inputStream' of the process and converted to a string using the 'java.lang.String' class. The resulting string contains the user ID of the current user.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Pebble]]
- [[Pebble - Code execution]]
- [[Server Side Template Injection]]


