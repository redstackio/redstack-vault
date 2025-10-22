---
id: 54536d94-3f0c-4ff4-a13c-69377e574eeb
name: Twig Template Injection - Arbitrary File Reading
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:40.337269+00:00'
updated_at: '2023-04-10T20:23:50.814255+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Server Side Template Injection]]'
- '[[Twig]]'
- '[[Twig - Arbitrary File Reading]]'
---

# Twig Template Injection - Arbitrary File Reading

## Summary

Twig is a popular template engine used in many PHP applications. It allows developers to create reusable templates for their web pages. However, if Twig is not properly configured, it can be vulnerable to Server Side Template Injection attacks. An attacker can use this vulnerability to execute arbi

## Description

# Description

Twig is a popular template engine used in many PHP applications. It allows developers to create reusable templates for their web pages. However, if Twig is not properly configured, it can be vulnerable to Server Side Template Injection attacks. An attacker can use this vulnerability to execute arbitrary code on the server, including reading sensitive files.

In this specific case, the attacker is able to read the first 30 lines of the /etc/passwd file and include the wp-config.php file. This can provide the attacker with valuable information, such as user accounts and passwords, and potentially allow them to gain access to the target's WordPress site.

Business value: An attacker can use this vulnerability to gain unauthorized access to sensitive information, such as user credentials, and potentially take over a website. This can result in reputational damage, loss of revenue, and legal consequences.

## Requirements

1. Access to a vulnerable PHP application that uses Twig templates

1. Knowledge of the file system structure of the target server

## Defense

1. Ensure that Twig is properly configured and up-to-date

1. Implement proper input validation and sanitization in the application

1. Restrict access to sensitive files on the server

## Objectives

1. Read sensitive files on the server

1. Gather information about the target's environment

1. Potentially gain access to the target's WordPress site

# Instructions

1. The 'file_excerpt' command is used to extract a specified number of lines from a file. In this case, the first 30 lines of the '/etc/passwd' file are extracted. The 'include' command is used to include the 'wp-config.php' file.

**Code**: [["{{'/etc/passwd'|file_excerpt(1,30)}}"@
{{include(]]

> The first argument of the 'file_excerpt' command is the file path and the second argument is the number of lines to extract. The 'include' command takes a file path as its argument and includes the file content in the current document. This command can be used to include configuration files, libraries, or any other files required for the execution of the program.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[Template Injection|T1221 - Template Injection]]

## Tags

- [[Server Side Template Injection]]
- [[Twig]]
- [[Twig - Arbitrary File Reading]]
