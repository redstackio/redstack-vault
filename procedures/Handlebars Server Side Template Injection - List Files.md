---
id: 9efafce9-2e85-4234-aa1d-f9eabd6ee4ea
name: Handlebars Server Side Template Injection - List Files
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.253027+00:00'
updated_at: '2023-04-10T20:23:36.702275+00:00'
tags:
- '[[Handlebars]]'
- '[[Handlebars - Command Execution]]'
- '[[Server Side Template Injection]]'
---

# Handlebars Server Side Template Injection - List Files

## Summary

Handlebars is a popular templating engine used in web applications. It allows developers to create reusable templates with dynamic content. However, if user input is not properly sanitized, it can lead to server-side template injection vulnerabilities. An attacker can exploit this vulnerability to 

## Description

# Description

Handlebars is a popular templating engine used in web applications. It allows developers to create reusable templates with dynamic content. However, if user input is not properly sanitized, it can lead to server-side template injection vulnerabilities. An attacker can exploit this vulnerability to execute arbitrary commands on the server. In this procedure, we will leverage Handlebars template injection to list all files in the current directory of the server. This can be used to gather information about the server's file system.

## Requirements

1. Access to the web application with Handlebars templating engine

1. Ability to inject malicious code into the Handlebars template

1. Knowledge of the file system structure of the server

## Defense

1. Properly sanitize user input to prevent server-side template injection vulnerabilities

1. Implement input validation and output encoding to prevent injection attacks

1. Restrict access to sensitive files and directories on the server

## Objectives

1. List all files in the current directory of the server

# Instructions

1. To list all files in the current directory, use this command:

**Code**: [[{{#with "s" as |string|}}
  {{#with "e"}}
    {{#w]]

> This command will execute the 'ls -la' command using the 'child_process' module of Node.js and return the output. The 'ls' command is used to list the files and directories in a directory. The '-la' option is used to display the files and directories in a long listing format, which includes additional information such as permissions, owner, size, and modification time.

## Tags

- [[Handlebars]]
- [[Handlebars - Command Execution]]
- [[Server Side Template Injection]]
