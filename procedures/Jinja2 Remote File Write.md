---
id: c2551f88-2457-4c33-9c8d-2501c0e0f4fb
name: Jinja2 Remote File Write
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.709728+00:00'
updated_at: '2023-04-10T20:23:35.626269+00:00'
tags:
- '[[Jinja2]]'
- '[[Jinja2 - Write into remote file]]'
- '[[Server Side Template Injection]]'
---

# Jinja2 Remote File Write

## Summary

Jinja2 is a powerful templating engine for Python web applications. It allows developers to dynamically generate web pages by using templates, which can be modified by users. However, if an attacker is able to inject malicious code into a Jinja2 template, they can execute arbitrary code on the serv

## Description

# Description

Jinja2 is a powerful templating engine for Python web applications. It allows developers to dynamically generate web pages by using templates, which can be modified by users. However, if an attacker is able to inject malicious code into a Jinja2 template, they can execute arbitrary code on the server. This can lead to a full compromise of the web application and the underlying system. In this procedure, we will use a Jinja2 template injection vulnerability to write a file on the remote server.

To exploit this vulnerability, we will first identify a vulnerable input field that allows us to inject Jinja2 code. Then, we will craft a payload that writes a file on the remote server. The payload will use the built-in Jinja2 'write' function to write the contents of a variable to a file on the server. This technique can be used to create a backdoor or modify existing files on the server.

The business value of this procedure is that it allows an attacker to gain persistence on the server and maintain access to the compromised system.

 

## Requirements

1. Access to a web application that uses Jinja2 templates

1. Ability to inject arbitrary code into a Jinja2 template

 

## Defense

1. Ensure that input validation is in place to prevent injection attacks

1. Limit the privileges of the web server user to prevent modification of critical files

1. Implement a file integrity monitoring system to detect changes to critical files

 

## Objectives

1. Write a file on the remote server

1. Maintain persistence on the server

 

# Instructions

1. This command writes the string 'Hello here !' to a file named 'hello.txt' located in the directory '/var/www/html/myflaskapp/'. The 'w' argument specifies that the file should be opened in write mode, which will overwrite any existing content in the file. 

 



**Code**: [[{{ ''.__class__.__mro__[2].__subclasses__()[40]('/]]



> The command uses the Python language to access the file system and write to a file. The '__class__.__mro__[2].__subclasses__()' method returns a list of all subclasses of the 'type' class, which includes the 'file' class. The command then creates an instance of the 'file' class with the specified file path and mode, and uses the 'write()' method to write the string to the file. 

## Tags

- [[Jinja2]]
- [[Jinja2 - Write into remote file]]
- [[Server Side Template Injection]]


